-- 175. Combine Two Tables
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person p
LEFT JOIN Address a ON p.personId = a.personId


-- 176. Second Highest Salary
SELECT MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT max(salary) FROM Employee);


-- 177. Nth Highest Salary
CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
  RETURN QUERY
  WITH rnkd AS (
    SELECT Employee.salary as salary,
           DENSE_RANK() OVER (ORDER BY Employee.salary DESC) AS rnk
    FROM Employee
  )
  SELECT MAX(rnkd.salary)
  FROM rnkd
  WHERE rnkd.rnk = N;
END;
$$ LANGUAGE plpgsql;


-- 178. Rank Scores
SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores;


-- 180. Consecutive Numbers
SELECT DISTINCT(num) AS ConsecutiveNums
FROM (
    SELECT
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev1,
        LAG(num, 2) OVER (ORDER BY id) AS prev2
    FROM Logs
)
WHERE num = prev1 and num = prev2


-- 181. Employees Earning More Than Their Managers
SELECT e1.name as Employee
FROM Employee e1
INNER JOIN Employee e2 ON e1.managerId = e2.id
WHERE e1.salary > e2.salary


-- 182. Duplicate Emails
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;


-- 183. Customers Who Never Order
SELECT c.name as Customers
FROM Customers c
LEFT JOIN Orders o
    ON c.id = o.customerId
GROUP BY c.id
HAVING COUNT(o.id) < 1


-- 184. Department Highest Salary
SELECT 
    Department,
    Employee,
    Salary
FROM (
    SELECT 
        e.name AS Employee, 
        e.salary AS Salary, 
        d.name AS Department,
        RANK() OVER(PARTITION BY d.name ORDER BY salary DESC) AS salaryRank
    FROM Employee e
    LEFT JOIN Department d
        ON e.departmentId = d.id
) t
WHERE salaryRank = 1


-- 185. Department Top Three Salaries
SELECT 
    Department,
    Employee,
    Salary
FROM (
    SELECT 
        e.name AS Employee, 
        e.salary AS Salary, 
        d.name AS Department,
        DENSE_RANK() OVER(PARTITION BY d.name ORDER BY salary DESC) AS salaryRank
    FROM Employee e
    LEFT JOIN Department d
        ON e.departmentId = d.id
) t
WHERE salaryRank = 1 OR salaryRank = 2 OR salaryRank = 3

-- 196. Delete Duplicate Emails
DELETE FROM Person
WHERE id NOT IN (
    SELECT * 
    FROM (
        SELECT MIN(id)
        FROM Person
        GROUP BY email
    ) AS temp
)


-- 197. Rising Temperature
SELECT w1.id as id
FROM Weather w1
JOIN Weather w2
    ON w1.recordDate = DATE_ADD(w2.recordDate, INTERVAL 1 DAY)
WHERE w1.temperature > w2.temperature


-- 262. Trips and Users
WITH filtered AS (
    SELECT
        t.client_id,
        t.driver_id,
        t.status,
        t.request_at AS Day
    FROM Trips t
    JOIN Users c
        ON c.users_id = t.client_id AND c.banned = 'No'
    JOIN Users d
        ON d.users_id = t.driver_id AND d.banned = 'No'
    WHERE t.request_at BETWEEN '2013-10-01' AND '2013-10-03'
)

SELECT
    Day,
    ROUND(
        SUM(CASE WHEN status LIKE 'cancelled%' THEN 1 ELSE 0 END) * 1.0 
        / 
        COUNT(*)
    , 2) AS "Cancellation Rate"
FROM filtered
GROUP BY Day


-- 511. Game Play Analysis I
SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id


-- 570. Managers with at Least 5 Direct Reports
SELECT e.name
FROM Employee e
JOIN Employee m
    ON e.id = m.managerId
GROUP BY e.id, e.name
HAVING COUNT(m.id) >= 5


-- 577. Employee Bonus
SELECT
    e.name,
    b.bonus
FROM Employee e
LEFT JOIN Bonus b
    ON e.empId = b.empId
WHERE b.bonus < 1000  OR b.bonus IS NULL;


-- 584. Find Customer Referee
SELECT name
FROM Customer
WHERE referee_id <> 2 OR referee_id IS NULL


-- 585. Investments in 2016
SELECT ROUND(SUM(i.tiv_2016)::numeric, 2) AS tiv_2016
FROM Insurance i
WHERE i.tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) >= 2
)
AND (i.lat, i.lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)


-- 586. Customer Placing the Largest Number of Orders
SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;


-- 595. Big Countries
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000


-- 607. Sales Person
WITH SalesRed AS (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c
        ON o.com_id = c.com_id
    WHERE c.name = 'RED'
)

SELECT sp.name
FROM SalesPerson sp
WHERE sp.sales_id NOT IN (
    SELECT * FROM SalesRed
)


-- 608. Tree Node
SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM TREE) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree;


-- 610. Triangle Judgement
SELECT
    x, y, z,
    CASE
        WHEN x + y > z AND x + z > y AND z + y > x THEN 'Yes'
        ELSE 'No'
    END AS triangle
FROM Triangle


-- 619. Biggest Single Number
SELECT MAX(num)
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;


-- 620. Not Boring Movies
SELECT c.*
FROM Cinema c
WHERE c.description <> 'boring'
    AND c.id % 2 != 0
ORDER BY rating DESC


-- 619. Biggest Single Number
SELECT MAX(num)
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) t;


-- 626. Exchange Seats
SELECT
    CASE
        WHEN id % 2 = 0 THEN id - 1
        WHEN id % 2 <> 0 AND id != (SELECT MAX(id) FROM Seat) THEN id + 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id


-- 627. Swap Sex of Employees
UPDATE Salary
SET sex = CASE 
    WHEN sex = 'f' THEN 'm'
    ELSE 'f'
END;


-- 1045. Customers Who Bought All Products
SELECT c.customer_id
FROM Customer c
GROUP BY c.customer_id
HAVING COUNT(DISTINCT c.product_key) = (SELECT COUNT(*) FROM Product p)


-- 1050. Actors and Directors Who Cooperated At Least Three Times
SELECT actor_id, director_id
FROM (
    SELECT actor_id, director_id, COUNT(*) AS cnt
    FROM ActorDirector
    GROUP BY actor_id, director_id
) t
WHERE cnt >= 3


-- 1068. Product Sales Analysis
SELECT p.product_name, s.year, s.price
FROM Sales s
LEFT JOIN Product p ON s.product_id = p.product_id


-- 1075. Project Employees I
SELECT p.project_id, ROUND(AVG(e.experience_years)::numeric, 2) AS average_years
FROM Project p
JOIN Employee e
    ON p.employee_id = e.employee_id
GROUP BY p.project_id
ORDER BY p.project_id DESC
