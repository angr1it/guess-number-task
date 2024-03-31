import gzip
import io
import os
import tarfile
from collections import defaultdict
from typing import Literal
import logging
import pathlib

import luigi
import pandas as pd
import requests
from bs4 import BeautifulSoup

from config import tsv_folder, process_folder, download_host, link_download_dataset

logger = logging.getLogger(__name__)


class GetDatasetFromEndpointTask(luigi.Task):

    def run(self):
        logger.info("Running GetDatasetFromEndpointTask...")
        start_page = self._get_download_page()
        download_endpoint = self._get_download_endpoint(start_page)

        logger.info(f"Downloading archive from {download_endpoint}...")
        response = requests.get(url=download_endpoint, allow_redirects=True)
        response.raise_for_status()

        with open(self.output().path, "wb") as file:
            file.write(response.content)
            logger.info(f"Saved archive to {self.output().path}")

    def output(self):
        archive_name = "NCBI_GEO_Data.tar"
        archive_file_path = f"{process_folder}/{archive_name}"

        return luigi.LocalTarget(archive_file_path)

    def complete(self):
        return self.output().exists()

    def _get_download_endpoint(self, page: BeautifulSoup) -> str:
        a_tags = page.find_all("a")
        download_link = None
        for a_tag in a_tags:
            if a_tag.text == "(http)":
                download_link = a_tag["href"]
                break

        if not download_link:
            raise ValueError("No download link found!")

        return f"{download_host}/{download_link}"

    def _get_download_page(self) -> BeautifulSoup:
        page_url = link_download_dataset
        response = requests.get(page_url)
        response.raise_for_status()
        return BeautifulSoup(response.text, "html.parser")


class ExtractTarFileTask(luigi.Task):

    def requires(self):
        return GetDatasetFromEndpointTask()

    def run(self):
        with tarfile.open(self.input().path, "r") as tar:
            tar.extractall(path=process_folder)
            logger.info(f"Extracted archive {self.input().path} to {process_folder}!")

        datasets_gz_files = self._get_txt_gx_files_names(directory_path=process_folder)
        unzip_files_paths = self._unzip_gz_files(gz_files=datasets_gz_files)
        self._drop_gz_files(gz_files=datasets_gz_files)

        with open(self.output().path, "w") as f:
            f.write("\n".join(unzip_files_paths))
            logger.info(f"Saved extracted files to {self.output().path}")

    def output(self):
        return luigi.LocalTarget(f"{process_folder}/extracted_files.txt")

    @classmethod
    def _get_txt_gx_files_names(cls, directory_path: str) -> tuple[str, ...]:
        return tuple(
            file_name
            for file_name in os.listdir(directory_path)
            if file_name.endswith(".txt.gz")
        )

    @classmethod
    def _unzip_gz_files(cls, gz_files: tuple[str, ...]) -> list[str]:
        unzip_files = []
        for gz_file in gz_files:
            file_path = f"{process_folder}/{gz_file}"

            with gzip.open(file_path, "rb") as file_input:
                unzip_file = gz_file.replace(".gz", "")
                unzip_file_path = f"{process_folder}/{unzip_file}"
                with open(unzip_file_path, "wb") as file_output:
                    file_output.write(file_input.read())

                unzip_files.append(unzip_file_path)

        return unzip_files

    @classmethod
    def _drop_gz_files(cls, gz_files: tuple[str, ...]):
        for gz_file in gz_files:
            os.remove(f"{process_folder}/{gz_file}")


class ProcessDataTask(luigi.Task):

    def requires(self):
        return ExtractTarFileTask()

    def run(self):

        raw_datasets = self._get_raw_datasets()
        datasets = defaultdict(list)
        for raw_dataset in raw_datasets:
            raw_dataset_file_path = f"{process_folder}/{raw_dataset}"
            dfs = self._process_raw_datasets(raw_dataset_file_path)

            for key, df in dfs.items():
                datasets[key].append(df)

        processed_datasets = {}
        for key, dfs in datasets.items():
            df = pd.concat(dfs)
            processed_datasets[key] = df

        self._save_dataframes(processed_datasets=processed_datasets)
        self._process_dfs(processed_datasets=processed_datasets)

    def output(self):
        return tuple(
            luigi.LocalTarget(f"{tsv_folder}/{file_name}")
            for file_name in os.listdir(tsv_folder)
            if file_name.endswith(".tsv")
        )

    @classmethod
    def _get_raw_datasets(cls):
        return tuple(
            file_name
            for file_name in os.listdir(process_folder)
            if file_name.endswith(".txt")
            and not file_name.startswith("extracted_files")
        )

    @classmethod
    def _process_raw_datasets(
        cls, raw_dataset_file_path: str
    ) -> dict[str, pd.DataFrame]:
        dfs = {}
        write_key = None

        with open(raw_dataset_file_path) as file:
            fio = io.StringIO()

            for raw_line in file.readlines():
                if raw_line.startswith("["):
                    if write_key:
                        fio.seek(0)
                        header = None if write_key == "Heading" else "infer"
                        dfs[write_key] = pd.read_csv(fio, sep="\t", header=header)
                    fio = io.StringIO()
                    write_key = raw_line.strip("[]\n")
                    continue

                if write_key:
                    fio.write(raw_line)
            fio.seek(0)

            dfs[write_key] = pd.read_csv(fio, sep="\t")
        return dfs

    @classmethod
    def _save_dataframes(
        cls,
        processed_datasets: dict[str, pd.DataFrame],
        type_: Literal["FULL", "PARTIAL"] = "FULL",
    ) -> None:
        for key, df in processed_datasets.items():
            file_name = f"{key}_{type_}.tsv"
            file_name = file_name.replace(" ", "_")
            file_path = pathlib.Path(f"{tsv_folder}/{file_name}")
            df.to_csv(file_path, sep="\t", index=False)
            logger.info(f"Saved processed dataset to {file_path}")

    @classmethod
    def _process_dfs(cls, processed_datasets: dict[str, pd.DataFrame]) -> None:
        special_key = "Probes"
        special_df = processed_datasets[special_key]

        special_df.drop(
            columns=[
                "Definition",
                "Ontology_Component",
                "Ontology_Process",
                "Obsolete_Probe_Id",
                "Probe_Sequence",
                "Synonyms",
                "Ontology_Function",
            ],
            inplace=True,
        )

        cls._save_dataframes(
            processed_datasets={special_key: special_df}, type_="PARTIAL"
        )
