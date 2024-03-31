import os
import logging

import luigi

from pipelines import (
    GetDatasetFromEndpointTask,
    ExtractTarFileTask,
    ProcessDataTask,
)
from config import data_folder, process_folder, tsv_folder

logger = logging.getLogger(__name__)


def create_folder_structure():
    logger.info("Creating folder structure...")
    os.makedirs(os.path.abspath(data_folder), exist_ok=True)
    os.makedirs(os.path.abspath(process_folder), exist_ok=True)
    os.makedirs(os.path.abspath(tsv_folder), exist_ok=True)
    logger.info("Done.")


if __name__ == "__main__":
    create_folder_structure()

    luigi.build(
        [
            GetDatasetFromEndpointTask(),
            ExtractTarFileTask(),
            ProcessDataTask(),
        ],
        workers=1,
        local_scheduler=True,
        no_lock=False,
    )
