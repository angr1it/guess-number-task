### Решение домашнего задания 2 (Системы хранения и обработки данных)
см. [notebook](notebook.ipynb)

#### SQL в jupyter

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
%sql SELECT * FROM customers
```
#### Запуск контейнера с бд:
```
docker-compose --profile hw_dbs up
```