-- Task 1
-- Вывести распределение (количество) клиентов по сферам деятельности, отсортировав результат по убыванию количества. — (1 балл)
SELECT job_industry_category, COUNT(*) as customer_count
FROM customer
GROUP BY job_industry_category
ORDER BY customer_count DESC;

-- Task 2
-- Найти сумму транзакций за каждый месяц по сферам деятельности, отсортировав по месяцам и по сфере деятельности. — (1 балл)
SELECT to_char(t.transaction_date, 'MM-YYYY') as transaction_month, c.job_industry_category, SUM(t.list_price)
FROM transaction t
LEFT JOIN customer c ON t.customer_id = c.customer_id
GROUP BY transaction_month, c.job_industry_category
ORDER BY transaction_month, c.job_industry_category;



-- Task 3
-- Вывести количество онлайн-заказов для всех брендов в рамках подтвержденных заказов клиентов из сферы IT. — (1 балл)
SELECT t.brand, COUNT(*) as order_count
FROM customer c
INNER JOIN transaction t on c.customer_id = t.customer_id
WHERE   t.online_order = 'True'
        and c.job_industry_category = 'IT'
        and t.order_status = 'Approved'
GROUP BY t.brand;



-- Task 4
-- Найти по всем клиентам сумму всех транзакций (list_price), максимум, минимум и количество транзакций, отсортировав результат по убыванию суммы транзакций и количества клиентов.
-- Выполните двумя способами: используя только group by и используя только оконные функции. Сравните результат. — (2 балла)

-- GRPUP BY
SELECT  t.customer_id,
        SUM(t.list_price) as total_sum,
        MAX(t.list_price) as max_price,
        MIN(t.list_price) as min_price,
        COUNT(t.list_price) as count
from transaction t
GROUP BY t.customer_id
ORDER BY total_sum DESC, count DESC;

-- window functions only
SELECT DISTINCT t.customer_id,
        SUM(t.list_price) OVER (PARTITION by t.customer_id) as total_sum,
        MAX(t.list_price) OVER (PARTITION by t.customer_id) as max_price,
        MIN(t.list_price) OVER (PARTITION by t.customer_id) as min_price,
        COUNT(t.list_price) OVER (PARTITION by t.customer_id) as count
from transaction t
ORDER BY total_sum DESC, count DESC;
-- Если убрать DISTINCT, то видно, что для каждой оконной функции формируется своя группировка... 



-- Task 5
-- Найти имена и фамилии клиентов с минимальной/максимальной суммой транзакций за весь период (сумма транзакций не может быть null). Напишите отдельные запросы для минимальной и максимальной суммы. — (2 балла)
SELECT c.first_name , c.last_name, SUM(t.list_price) as min_price
FROM transaction t
INNER JOIN customer c ON c.customer_id = t.customer_id
GROUP BY c.customer_id
ORDER BY min_price
limit 1;

SELECT c.first_name , c.last_name, SUM(t.list_price) as max_price
FROM transaction t
INNER JOIN customer c ON c.customer_id = t.customer_id
GROUP BY c.customer_id
ORDER BY max_price DESC
limit 1;



-- Task 6
-- Вывести только самые первые транзакции клиентов. Решить с помощью оконных функций. — (1 балл)
SELECT DISTINCT
        FIRST_VALUE(customer_id) OVER (PARTITION BY customer_id ORDER BY transaction_date) as customer_id,
        FIRST_VALUE(transaction_id) OVER (PARTITION BY customer_id ORDER BY transaction_date) as transaction_id,
        FIRST_VALUE(transaction_date) OVER (PARTITION BY customer_id ORDER BY transaction_date) as transaction_date
FROM transaction;



-- Task 7
-- Вывести имена, фамилии и профессии клиентов, между транзакциями которых был максимальный интервал (интервал вычисляется в днях) — (2 балла).
WITH lag_prev_transaction AS (
    SELECT
        customer_id,
        transaction_date,
        LAG(transaction_date) OVER (PARTITION BY customer_id ORDER BY transaction_date) AS prev_transaction_date
    FROM transaction
),
interval_transaction AS (
    SELECT
        customer_id, 
        transaction_date - prev_transaction_date AS interval
    FROM lag_prev_transaction
    WHERE prev_transaction_date IS NOT NULL
),
max_interval_customer AS (
    SELECT
        customer_id, 
        MAX(interval) AS max_interval
    FROM interval_transaction
    GROUP BY customer_id
)
SELECT
    c.first_name,
    c.last_name,
    c.job_title,
    m.max_interval
FROM customer c
INNER JOIN max_interval_customer m ON c.customer_id = m.customer_id
ORDER BY m.max_interval DESC;