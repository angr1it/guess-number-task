import logging
import os
from datetime import date, timedelta
from pathlib import Path

import pendulum
import pandas as pd
from pandas import DataFrame
from airflow.decorators import dag, task

logger = logging.getLogger(__name__)

now = pendulum.now()


@task(
    task_id="extract_csv",
    execution_timeout=timedelta(minutes=5),
    retries=2,
)
def extract_csv(csv_path: Path = Path("data/profit_table.csv")) -> DataFrame:
    """
    Функция для чтения данных из CSV-файла.

    Аргументы:
        csv_path (Path, optional): путь к CSV-файлу. По умолчанию "data/profit_table.csv".

    Возвращает:
        pd.DataFrame: прочтенные данные из CSV-файла.
    """
    return pd.read_csv(csv_path)


@task(
    task_id="prepare_profit_table",
    execution_timeout=timedelta(minutes=5),
    retries=2,
)
def prepare_profit_table(profit_table: DataFrame, current_date: date) -> DataFrame:
    """
    Функция для подготовки таблицы прибыли для расчета флагов активности.

    Аргументы:
        profit_table (DataFrame): таблица с суммой и количеством транзакций.
        current_date (date): дата расчета флагов активности.

    Возвращает:
        DataFrame: таблица прибыли для расчета флагов активности за указанную дату.
    """
    logger.info("Подготовка таблицы прибыли...")
    current_date = pd.to_datetime(current_date)
    start_date = current_date - pd.DateOffset(months=2)
    end_date = current_date + pd.DateOffset(months=1)

    date_list = pd.date_range(start=start_date, end=end_date, freq="M").strftime(
        "%Y-%m-01"
    )

    result_table = (
        profit_table[profit_table["date"].isin(date_list)]
        .drop("date", axis=1)
        .groupby("id")
        .sum()
    )
    logger.info(f"Таблица прибыли подготовлена для {current_date}")
    return result_table


@task(
    task_id="transform_profit_table",
    retries=2,
)
def transform_profit_table(profit_table: DataFrame, product_name: str) -> DataFrame:
    """
    Функция для преобразования таблицы прибыли в таблицу флагов активности.

    Аргументы:
        profit_table (DataFrame): таблица с суммой и количеством транзакций.
        product_name (str): название продукта.

    Возвращает:
        DataFrame: таблица с флагами активности.
    """
    logger.info("Преобразование таблицы прибыли...")
    profit_table = profit_table.copy()

    product_field = f"flag_{product_name}"
    profit_table[product_field] = profit_table.apply(
        lambda row: row[f"sum_{product_name}"] != 0
        and row[f"count_{product_name}"] != 0,
        axis=1,
    ).astype(int)

    logger.info(f"Таблица прибыли преобразована для {profit_table}")
    return profit_table.filter(regex="flag").reset_index()


@task(
    task_id="get_activity_table",
    execution_timeout=timedelta(minutes=5),
    retries=2,
)
def get_activity_table(
    profit_tables: tuple[DataFrame, ...],
    csv_target: Path = Path("data/activity_table.csv"),
) -> None:
    """
    Функция для сохранения таблицы флагов активности в CSV-файл.

    Аргументы:
        profit_tables (tuple[DataFrame, ...]): таблицы с флагами активности.
        csv_target (Path): путь к CSV-файлу.

    Возвращает:
        None
    """
    logger.info("Сохранение таблицы флагов активности...")
    df_merged = reduce(
        lambda left, right: pd.merge(left, right, on="id", how="outer"), profit_tables
    )

    if os.path.exists(csv_target):
        df_merged.to_csv(csv_target, index=False)
    else:
        df_merged.to_csv(csv_target, mode="a", header=False, index=False)
    logger.info("Таблица флагов активности сохранена.")


@dag(
    description='ETL пайплайн для "Инжиниринг данных. Итоговый проект (PJ)", выполнено Гриценко Андреем',
    catchup=False,
    start_date=now,
    schedule="0 0 5 * *",
    tags=["mfti"],
)
def etl_parallel_by_Gritsenko_Andrey():
    """
    DAG для ETL-пайплайна.

    Задачи:
        1. Чтение данных из CSV-файла.
        2. Подготовка таблицы прибыли для расчета флагов активности.
        3. Преобразование таблицы прибыли в таблицу флагов активности для каждого продукта.
        4. Сохранение таблицы флагов активности в CSV-файл.
    """
    logger.info("Запуск ETL-пайплайна...")

    profit_table = prepare_profit_table(extract_csv(), date.today())

    transformation_by_product = tuple(
        transform_profit_table.override(task_id=f"transform_product_{product}")(
            profit_table=profit_table,
            product_name=product,
        )
        for product in ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    )

    (
        profit_table
        >> transformation_by_product
        >> get_activity_table(profit_tables=transformation_by_product)
    )


dag_etl = etl_parallel_by_Gritsenko_Andrey()


if __name__ == "__main__":
    dag_etl.test()
