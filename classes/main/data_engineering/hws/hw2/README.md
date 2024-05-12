# 1/1   Инжиниринг данных. Итоговый проект (PJ)

## Запуск

Из папки с проектом задания (classes\main\data_engineering\hws\hw2 относительно корня репозитория):
```
docker-compose up
```
и дождаться пока airflow поднимется. 

Файл для обработки ```profit_table.csv``` добавлять в ```data``` в данном проекте -- настроен docker volume для чтения оттуда. Туда-же записывается результат.

p.s. т.к. ```profit_table.csv``` требует lfs его не стал добавлять в коммит.

## Скрины результатов

#### Основное задание
![alt text](imgs/image.png)

![alt text](imgs/image-1.png)

![alt text](imgs/image-2.png)

#### Дополнительное

![alt text](imgs/image-3.png)

![alt text](imgs/image-4.png)