-- Task 1
-- (1 балл) Вывести все уникальные бренды, у которых стандартная стоимость выше 1500 долларов.
SELECT DISTINCT brand
FROM transaction
WHERE standard_cost > 1500;


-- Task 2
-- (1 балл) Вывести все подтвержденные транзакции за период '2017-04-01' по '2017-04-09' включительно.
SELECT *
FROM transaction
WHERE transaction_date BETWEEN '2017-04-01' AND '2017-04-09'
    AND order_status = 'Approved'
;


-- Task 3
-- (1 балл) Вывести все профессии у клиентов из сферы IT или Financial Services, которые начинаются с фразы 'Senior'.
SELECT DISTINCT c.job_title
FROM customer c
INNER JOIN transaction t ON c.customer_id = t.customer_id
WHERE c.job_industry_category IN ('IT', 'Financial Services')
AND c.job_title LIKE 'Senior%';



-- Task 4
-- (1 балл) Вывести все бренды, которые закупают клиенты, работающие в сфере Financial Services
SELECT DISTINCT t.brand
FROM transaction t
INNER JOIN customer c ON t.customer_id = c.customer_id
WHERE c.job_industry_category = 'Financial Services';


-- Task 5
-- (1 балл) Вывести 10 клиентов, которые оформили онлайн-заказ продукции из брендов 'Giant Bicycles', 'Norco Bicycles', 'Trek Bicycles'.
SELECT DISTINCT c.customer_id, c.first_name, c.last_name
FROM transaction t
INNER JOIN customer c ON t.customer_id = c.customer_id
WHERE t.online_order = 'TRUE'
    AND t.brand IN ('Giant Bicycles', 'Norco Bicycles', 'Trek Bicycles')
LIMIT 10;



-- Task 6
-- (1 балл) Вывести всех клиентов, у которых нет транзакций.
SELECT c.customer_id, c.first_name, c.last_name
FROM customer c
LEFT JOIN transaction t ON c.customer_id = t.customer_id
WHERE t.transaction_id IS NULL;


-- Task 7
-- (2 балла) Вывести всех клиентов из IT, у которых транзакции с максимальной стандартной стоимостью.
SELECT c.customer_id, c.first_name, c.last_name, t.standard_cost
FROM customer c
INNER JOIN transaction t ON c.customer_id = t.customer_id
WHERE c.job_industry_category = 'IT'
    AND t.standard_cost = (
        SELECT max(standard_cost)
        FROM transaction
    );


-- Task 8
-- (2 балла) Вывести всех клиентов из сферы IT и Health, у которых есть подтвержденные транзакции за период '2017-07-07' по '2017-07-17'.
SELECT DISTINCT c.customer_id, c.first_name, c.last_name, c.job_industry_category
FROM customer c
INNER JOIN transaction t ON c.customer_id = t.customer_id
WHERE c.job_industry_category in ('IT', 'Health')
    AND t.transaction_date BETWEEN '2017-07-07' AND '2017-07-17'
    AND t.order_status = 'Approved';
