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
    task_id="transform_profit_table", execution_timeout=timedelta(minutes=5), retries=2
)
def transform_profit_table(profit_table: DataFrame, current_date: date) -> DataFrame:
    """Собирает таблицу флагов активности по продуктам
    на основании прибыли и количеству совершёных транзакций

    :param profit_table: таблица с суммой и кол-вом транзакций
    :param date: дата расчёта флагоа активности

    :return df_tmp: pandas-датафрейм флагов за указанную дату
    """
    logger = logging.getLogger("airflow.task")

    current_date = pd.to_datetime(current_date)
    start_date = current_date - pd.DateOffset(months=2)
    end_date = current_date + pd.DateOffset(months=1)

    date_list = pd.date_range(start=start_date, end=end_date, freq="M").strftime(
        "%Y-%m-01"
    )

    df_tmp = (
        profit_table[profit_table["date"].isin(date_list)]
        .drop("date", axis=1)
        .groupby("id")
        .sum()
    )

    product_list = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    for product in product_list:
        df_tmp[f"flag_{product}"] = df_tmp.apply(
            lambda x: x[f"sum_{product}"] != 0 and x[f"count_{product}"] != 0, axis=1
        ).astype(int)

    df_tmp = df_tmp.filter(regex="flag").reset_index()
    logger.info(f"Transformed profit table for {current_date}")
    return df_tmp


@task(
    task_id="get_activity_table",
    execution_timeout=timedelta(minutes=5),
    retries=2,
)
def get_activity_table(
    profit_table: tuple[DataFrame, ...],
    csv_target: Path = Path("data/activity_table.csv"),
) -> None:
    """
    Функция для сохранения таблицы флагов активности в CSV-файл.

    Аргументы:
        profit_tables (tuple[DataFrame, ...]): таблица с флагами активности.
        csv_target (Path): путь к CSV-файлу.
    """
    logger.info("Сохранение таблицы флагов активности...")

    if os.path.exists(csv_target):
        profit_table.to_csv(csv_target, index=False)
    else:
        profit_table.to_csv(csv_target, mode="a", header=False, index=False)
    logger.info("Таблица флагов активности сохранена.")


@dag(
    description='ETL пайплайн для "Инжиниринг данных. Итоговый проект (PJ)", выполнено Гриценко Андреем',
    catchup=False,
    start_date=now,
    schedule="0 0 5 * *",
    tags=["mfti"],
)
def etl_by_Gritsenko_Andrey():
    """
    DAG для ETL-пайплайна.

    Задачи:
        1. Чтение данных из CSV-файла.
        2. Подготовка таблицы прибыли для расчета флагов активности.
        3. Преобразование таблицы прибыли в таблицу флагов активности для каждого продукта.
        4. Сохранение таблицы флагов активности в CSV-файл.
    """
    logger.info("Запуск ETL-пайплайна...")

    profit_table = transform_profit_table(extract_csv(), date.today())
    load = get_activity_table(profit_table)

    profit_table >> load


dag_etl = etl_by_Gritsenko_Andrey()


if __name__ == "__main__":
    dag_etl.test()
