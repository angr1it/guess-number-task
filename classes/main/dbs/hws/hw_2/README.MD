### Решение домашнего задания 2 (Системы хранения и обработки данных)
1. [Notebook](notebook.ipynb) решения с ipython-sql
2. [Скрипт sql запросов](queries.sql)
3. [Скриншоты dbeaver](screenshots.md)


### SQL в jupyter

```
!pip install ipython-sql
```
Далее, установить sql-расширение внутри ipython командой (в ячейке):
```
%load_ext sql
```

Подключаемся к db:
```
%sql sqlite:///example.db
```

Выполнение sql-запроса:
```
%sql SELECT * FROM customer
```



### Запуск контейнера с бд:
```
docker-compose --profile hw_dbs up
```