# Each statement ends with a semicolon (;)

# CREATE is primarily used in the creation of objects (e.g., tables) within a database.
# CREATE syntax:
    # CREATE TABLE TableName(
        # Fieldname1 datatype properties,
        # Fieldname2 datatype properties,
        # Fieldname3 datatype properties,
        # Fieldname4 datatype properties);   
# for primary keys:
    # Fieldname INT IDENTITY (1,1) #auto numbering property, created automatically

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SELECT statement
# The SELECT statement is used to select data from a database.
# A SELECT statement can be used to return information that does not include a table. 
# For example, you can have SELECT calculate a value and return the value SELECT 27 * 18 from dual. 
# The DUAL table is a generic table and is optional. The same SELECT statement can be written as SELECT 27*18, and the same value, 486, will be returned.
# SELECT statements can also include subqueries and UNION statements. 
# SELECT statements can also be used to populate a table by using a SELECT INTO statement. 
# The data that are returned will be inserted into a specific table.
# The data returned is stored in a result table, called the result-set.
# Example:
    # SELECT expressions
    # FROM tables
    # [WHERE conditions]
    # [ORDER BY expression [ ASC | DESC ]];

# Simpler:
    # SELECT * from tables;

#Another example:
# Table 1:
# customer_id	last_name	first_name	favorite_website
# 4000	        Jackson	    Joe	        techonthenet.com
# 5000	        Smith	    Jane	    digminecraft.com
# 6000	        Ferguson	Samantha	bigactivities.com
# 7000	        Reynolds	Allen	    checkyourmath.com
# 8000	        Anderson	Paige	    NULL
# 9000	        Johnson	    Derek	    techonthenet.com

#Table 2:
# order_id	customer_id	order_date
# 1	        7000	    2016/04/18
# 2	        5000	    2016/04/18
# 3	        8000	    2016/04/19
# 4	        4000	    2016/04/20
# 5	        NULL	    2016/05/01

    # SELECT orders.order_id, customers.last_name
    # FROM orders
    # INNER JOIN customers
    # ON orders.customer_id = customers.customer_id
    # WHERE orders.order_id <> 1
    # ORDER BY orders.order_id;

# Result:
# order_id	last_name
# 2	Smith
# 3	Anderson
# 4	Jackson

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# WHERE statement
# The WHERE clause has the ability to select rows based on a Boolean expression. 
# The rows in which the expression is true are returned in the result. 
# If it is a DELETE statement, then it is deleted. In an UPDATE statement, it is updated.
# The WHERE clause has the ability to join or filter predicates. 
# This can be accomplished as a way to limit the data that are returned by table expressions.
# Examples:
    # Where Clause Type                     Example
    # Simple                                col1 = 3
    # Text compare                          col1 = 'Car'
    # Not equal                             col1<> 'Car'
    # Compare date                          col1 = '2009-11-07'
    # Multiple values                       col1 in ('Car1','Car2','Car3')
    # Starts with                           col1 like 'Car%'
    # Contains                              col1 like '%Car%'
    # Between two values                    col1 between 0 and 200
    # Text between                          col1 between 'MARY' and 'SMITH'
    # Value is present in another table     col1 in (select col2 from another table)
    # Value is not present in another table col1 not in (select col2 from another table)
    # Value is null                         col1 is null
    # Value is not null                     col1 is not null

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# An INSERT statement is used to add data into a table within a relational database.
# You do not have to include all of the columns in an INSERT statement—only those where a value should be entered.
# You also need to ensure that you are including the PRIMARY KEY and that each primary key value is unique. 
# A PRIMARY KEY can be set to auto-increment when it is a numeric value. In these cases, the PRIMARY KEY does not have to be included in the INSERT statement.
# Information can be added one row at a time using the following syntax:
    # INSERT [LOW_PRIORITY | DELAYED | HIGH_PRIORITY] [IGNORE]
    #     [INTO] tbl_name
    #     [PARTITION (partition_name,...)]
    #     [(col_name,...)]
    #     {VALUES | VALUE} ({expr | DEFAULT},...),(...),...
    #     [ ON DUPLICATE KEY UPDATE
    #        col_name=expr
    #        [, col_name=expr] ... ]

# Or simpler:
    # INSERT INTO tablename (COL1, COL2, …. ,COLn ) VALUES (value1, value2, …, valueN)

# Rows can also be added in bulk using a SELECT statement. The syntax would look like the following (MySQL, n.d.b):
    # INSERT [LOW_PRIORITY | HIGH_PRIORITY] [IGNORE]
    #     [INTO] tbl_name
    #     [PARTITION (partition_name,...)]
    #     [(col_name,...)]
    #     SELECT ...
    #     [ ON DUPLICATE KEY UPDATE
    #        col_name=expr
    #        [, col_name=expr] ... ]

# Or simpler:
    # INSERT INTO tablename (COL1, COL2, …, COLn) SELECT COLb1, COLb2, …., COLbn FROM tablename2 WHERE …
# Example: 
    # INSERT INTO TBL_Names SELECT UID, First_Name, Last_Name from tbl_OldNames where first_name = ‘Phillip';

# Example of INSERT method to 'tbl_Member2' table:
    # INSERT INTO `mydb`.`tbl_Member2` 
    # (`Member_ID`, `Last_Name`, `First_Name`, `EMail`, `Address_Line_1`, `Address_Line_2`, `City`, `State`, `Zip`, `Phone`) 
    # VALUES 
    # (12, 'Membertwo', 'Sarah', 'membertwo@email.com', '222SilverAve', '', 'Denver', '', '', '720-345-2222');

# 'mydb' is a database where table 'tbl_Member2' is located
# 'tbl_Member2' column datatypes:
# (`Member_ID`, `Last_Name`, `First_Name`, `EMail`, `Address_Line_1`, `Address_Line_2`, `City`, `State`, `Zip`, `Phone`)
# INT, VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45), VARCHAR(45) 

#The following example shows how to do a multitable insert through an INSERT ALL statement, which is not supported by all databases but is supported by ORACLE 9i databases and higher (Gennick, 2005):
    #  INSERT ALL
    #        INTO table1 (column1, column2, …, columnN) VALUES (value1, value2, …., valueN)
    #        INTO table2 (column1, column2, …, columnN) VALUES (value1, value2, …., valueN)
    #        ….
    #        INTO tableN(column1, column2, …, columnN) VALUES (value1, value2, …., valueN)
    #  SELECT * from dual;
# The SELECT * from dual part of the statement allows you to enter your own values. 
# If you wanted to use a SELECT statement, the value1 to valueN for each area would be the column names from the SELECT statement at the bottom of the INSERT ALL statement. 
# Because a SELECT statement can come from one or more tables, the columns can use any of the specified columns' names across each table that is specified in the SELECT statement.

# An INSERT ALL can also be performed conditionally. 
# The example above is an unconditional INSERT ALL wherein all of the INSERT statements are performed without any conditions.
#  For a conditional INSERT ALL, the syntax would look mostly the same; however, it would contain a WHEN statement. The syntax would be as follows:
    # INSERT ALL|FIRST
    #      [WHEN condition THEN] INTO target [VALUES]
    #      [WHEN condition THEN] INTO target [VALUES]
    #      ...
    #      [ELSE] INTO target [VALUES]
    # SELECT ...
    # FROM source_query;
# Using the FIRST statement will allow the row to fall into the FIRST condition that was met vice all of the conditions that might be met with the row value being tested.

# Copy data from one table to another:
    # INSERT INTO table2
    # SELECT * FROM table1;
# or specific columns:
    # INSERT INTO table2
    # (column_name(s))
    # SELECT column_name(s)
    # FROM table1;
# or create new table with columns:
    # SELECT * INTO SupplierUSA
    # FROM Supplier
    # WHERE Country = 'USA'
# This will create a SupplierUSA table that has the same columns as the Supplier table.

# If the database that you are using does not support INSERT ALL, the recommended way to add rows to multiple tables is to use transactions. 
# A transaction will ensure that all of the statements included within will be completed or ignored together. Consider the following example:
    # START TRANSACTION
    #      [transaction_characteristic [, transaction_characteristic] ...]
    # transaction_characteristic:
    #      WITH CONSISTENT SNAPSHOT
    #      | READ WRITE
    #      | READ ONLY
# Once a transaction is started, it must be ended with either a COMMIT or a ROLLBACK. 
# A COMMIT processes the statements within the transaction to make the changes permanent. 
# A ROLLBACK cancels all of the changes made within the transaction.
# The following is a quick example:
    # START TRANSACTION;
    # SELECT @A:=SUM(salary) FROM table1 WHERE type=1;
    # UPDATE table2 SET summary=@A WHERE type=1;
    # COMMIT;
# Transactions can be short, such as the example above, or long, with the transaction containing multiple statements. 
# It is important to be aware that not all statements can be rolled back. 
# The statements that are done within a transaction that impact the database structure, such as a CREATE table, an ALTER table, or a DROP table, cannot be rolled back.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Several common conversions might be converting a TYPE1 value to a TYPE2 or the other way around.
# Often, a CAST function will work to accomplish this goal, as shown in the following:
    # CAST(datetime_col AS DATE)    (This will take a DATETIME value and convert it to a DATE value.)

# CONVERT is also another function:
    # CONVERT(expr USING transcoding_name)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# DELETE statement
# It is important to remember that DELETE only works on data and not on any type of database component, 
# such as a field, table, index, or view. 
# In these cases, a DROP or ALTER command would be used. DELETE is solely used on data, specifically entire rows of data, stored within the database.
#Again, if you just want to delete the value for a specific field of data, an UPDATE command would be used to set the value to null, zero, or empty. 
# DELETE is used only for the removal of an entire row or rows of data at one time.

# Single Table
    # DELETE [LOW_PRIORITY] [QUICK] [IGNORE] FROM tbl_name
    #  [PARTITION (partition_name,...)]
    #  [WHERE where_condition]
    #  [ORDER BY ...]
    #  [LIMIT row_count]                         

# Multiple Tables
    # DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    #  tbl_name[.*] [, tbl_name[.*]] ...
    #  FROM table_references
    #  [WHERE where_condition]                       

# Or
    # DELETE [LOW_PRIORITY] [QUICK] [IGNORE]
    #  FROM tbl_name[.*] [, tbl_name[.*]] ...
    #  USING table_references
    #  [WHERE where_condition]

# Simpler
    # DELETE FROM tbl_Player WHERE UID = 10;

# Delete all data from table (if you need to delete table, use DROP):
    # DELETE from table

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# TRUNCATE statement.
# TRUNCATE is another statement which is used to delete ALL data from a table, but not the table itself.
# The DELETE statement removes rows one at a time and records an entry in the transaction log for each deleted row. 
# TRUNCATE TABLE removes the data by deallocating the data pages used to store the table data and records only the page deallocations in the transaction log. 
# DELETE command is slower than TRUNCATE command.
# Example of TRUNCATE:
    # TRUNCATE TABLE TableName; 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# UPDATE statement.
# When using UPDATE to a single row, the WHERE clause becomes very important to single out the row that you want to update.
# Example:
    # UPDATE tbl_Player set Team_ID = 1 where Lastname like ‘J*’
    # UPDATE tbl_Player set TeamID = 3 where ISNULL(TeamID)     (ISNULL function tests to see whether the value specified in the column is set to NULL.
    #                                                            If expr is NULL, ISNULL() returns 1, otherwise it returns 0.)

# The following is a single-table syntax update:
    # UPDATE [LOW_PRIORITY] [IGNORE] table_reference
    #     SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    #     [WHERE where_condition]
    #     [ORDER BY ...]
    #     [LIMIT row_count]

# The following is a multiple-table syntax update:
    # UPDATE [LOW_PRIORITY] [IGNORE] table_references
    #     SET col_name1={expr1|DEFAULT} [, col_name2={expr2|DEFAULT}] ...
    #     [WHERE where_condition]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Locking tables helps keep other sessions from interfering with the data within the specified tables. See the following example:
    # LOCK TABLES
    #      tbl_name [[AS] alias] lock_type
    #      [, tbl_name [[AS] alias] lock_type] ...
    # lock_type:
    #      READ [LOCAL]
    #      | [LOW_PRIORITY] WRITE
    # UNLOCK TABLES
# Using locks on tables can also contribute to sessions working together. The interaction or non-interaction between sessions depends on how the tables are locked.
# The following sections describe the different types of locks.
# The READ [LOCAL] lock has the following characteristics (MySQL, n.d.f):
    # The session that holds the lock can read from a table but cannot write to it.
    # Multiple sessions can acquire a READ lock for a table at the same time.
    # Other sessions can read a table without explicitly acquiring a READ lock.
    # The LOCAL modifier allows nonconflicting INSERT statements (concurrent inserts) by other sessions to execute while the lock is held. 
        # However, READ LOCAL cannot be used if you are going to manipulate a database using processes that are external to the server while you hold the lock.
# The WRITE lock has the following characteristics (MySQL, n.d.f):
    # The session that holds the lock can read from and write to a table.
    # Only the session that holds the lock can access a table. No other session can access the table until the lock is released.
    # Lock requests for a table from other sessions are blocked while the WRITE lock is held.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# WITH statement
# The SQL WITH clause allows you to give a sub-query block a name (a process also called sub-query refactoring), which can be referenced in several places within the main SQL query.
    # WITH temporaryTable (averageValue) as
        # (SELECT avg(Attr1)
        # FROM Table)
        # SELECT Attr1
        # FROM Table, temporaryTable
        # WHERE Table.Attr1 > temporaryTable.averageValue;
# In this query, WITH clause is used to define a temporary relation temporaryTable that has only 1 attribute averageValue. 
# averageValue holds the average value of column Attr1 described in relation Table. 
# The SELECT statement that follows the WITH clause will produce only those tuples 
# where the value of Attr1 in relation Table is greater than the average value obtained from the WITH clause statement. 

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# OVER (PARTITION BY)
# Use PARTITION BY to divide the result set into partitions and perform computation on each subset of partitioned data.
    # SELECT Customercity, 
    #        AVG(Orderamount) OVER(PARTITION BY Customercity) AS AvgOrderAmount, 
    #        MIN(OrderAmount) OVER(PARTITION BY Customercity) AS MinOrderAmount, 
    #        SUM(Orderamount) OVER(PARTITION BY Customercity) TotalOrderAmount
    # FROM [dbo].[Orders];
# Almost the same as:
    # SELECT Customercity, CustomerName ,OrderAmount,
    #        AVG(Orderamount) AS AvgOrderAmount, 
    #        MIN(OrderAmount) AS MinOrderAmount, 
    #        SUM(Orderamount) TotalOrderAmount
    # FROM [dbo].[Orders]
    # GROUP BY Customercity;
# but it returns all columns (doesn't group columns into 1, returns averages, but as many rows as there are same cities)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ORDER BY clause
# The ORDER BY clause provides a means for allowing the syntax to specify the order of the result set based on an expression in which rows appear in the results.
# In subqueries, the ORDER BY clause should be accompanied by one or both of the results, offset, and fetch first clauses or in conjunction with the ROW_NUMBER function.
    # SELECT expressions
    # FROM tables
    # [WHERE conditions]
    # ORDER BY expression [ ASC | DESC ];
# Here, ASC - ascending, DESC - descending

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# GROUP BY clause
# The Group By clause is used to group the result set based on a common value present in the results. 
# In conjunction with the Group By clause, the WHERE clause and HAVING clause can be used to limit or filter the grouped result.
# It follows the WHERE clause in a SELECT statement and precedes the ORDER BY clause.
    # SELECT column1, column2
    # FROM table_name
    # WHERE [ conditions ]
    # GROUP BY column1, column2
    # HAVING ...
    # ORDER BY column1, column2
# Example:
#   SELECT
#       ISNULL(ContryName, 'Total'), # ISNULL for GRAND TOTAL in GROUP BY
#       AVG(CONVERT(DECIMAL, FilmRunTimeMinutes)) AS [AverageRunTime],
#       SUM(FilmRunTimeMinutes) AS [TotalRunTime],
#       MAX(FilmRunTimeMinutes) AS [LongestRunTime],
#       MIN(FilmRunTimeMinutes) AS [ShortestRunTime]
#   FROM
#       tblFilm as f
#       INNER JOIN tblCountry AS c ON c.countryID = f.FilmCountryID
#   GROUP BY
#       CountryName WITH ROLLUP # WITH ROLLUP means to add GRAND TOTAL
#   ORDER BY
#       CountryName ASC
# Result:
#   ContryName      AverageRunTime      TotalRunTime        LongestRunTime      ShortestRunTime
#   Total           126                 32944               201                 84
#   China           110                 442                 120                 99
#   France          119                 358                 169                 78
#   Germany         136                 536                 234                 101

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# PIVOT statement
# Pivot allows users to rotate a table-valued expression by turning the unique values from one column into individual columns.
# Example:
# Table (not all data):
    # Date	        Temp (°F)
    # 07-22-2018	86
    # 07-23-2018	90
    # 07-24-2018	91
    # 07-25-2018	92
    # 07-26-2018	92
    # 07-27-2018	88
    # 07-28-2018	85
    # 07-29-2018	94
    # 07-30-2018	89
# Code:
    # SELECT * FROM (
    #   SELECT year(date) year, month(date) month, temp
    #   FROM high_temps
    #   WHERE date BETWEEN DATE '2015-01-01' AND DATE '2018-08-31'
    # )
    # PIVOT (
    #   CAST(avg(temp) AS DECIMAL(4, 1))
    #   FOR month in (
    #     1 JAN, 2 FEB, 3 MAR, 4 APR, 5 MAY, 6 JUN,
    #     7 JUL, 8 AUG, 9 SEP, 10 OCT, 11 NOV, 12 DEC
    #   )
    # )
    # ORDER BY year DESC
# Result:
    # YEAR	JAN	    FEB	    MAR	    APR	    MAY	    JUNE	JULY	AUG	    SEPT	OCT	    NOV	    DEC
    # 2018	49.7	45.8	54.0	58.6	70.8	71.9	82.8	79.1	NULL	NULL	NULL	NULL
    # 2017	43.7	46.6	51.6	57.3	67.0	72.1	78.3	81.5	73.8	61.1	51.3	45.6
    # 2016	49.1	53.6	56.4	65.9	68.8	73.1	76.0	79.5	69.6	60.6	56.0	41.9
    # 2015	50.3	54.5	57.9	59.9	68.0	78.9	82.6	79.0	68.5	63.6	49.4	47.1

# Let’s take a closer look at this query to understand how it works. 
# First, we need to specify the FROM clause, which is the input of the pivot, in other words, the table or subquery based on which the pivoting will be performed. 
# In our case, we are concerned about the years, the months, and the high temperatures, so those are the fields that appear in the sub-query.
# Second, let’s consider another important part of the query, the PIVOT clause. 
# The first argument of the PIVOT clause is an aggregate function and the column to be aggregated. 
# We then specify the pivot column in the FOR sub-clause as the second argument, followed by the IN operator containing the pivot column values as the last argument.
# The pivot column is the point around which the table will be rotated, and the pivot column values will be transposed into columns in the output table. 
# The IN clause also allows you to specify an alias for each pivot value, making it easy to generate more meaningful column names.
# An important idea about pivot is that it performs a grouped aggregation based on a list of implicit group-by columns together with the pivot column. 
# The implicit group-by columns are columns from the FROM clause that do not appear in any aggregate function or as the pivot column.
# In the above query, with the pivot column being the column month and the implicit group-by column being the column year, 
# the expression avg(temp) will be aggregated on each distinct value pair of (year, month), where month equals to one of the specified pivot column values. 
# As a result, each of these aggregated values will be mapped into its corresponding cell of row year and column month.
# It is worth noting that because of this implicit group-by, 
# we need to make sure that any column that we do not wish to be part of the pivot output should be left out from the FROM clause, 
# otherwise the query would produce undesired results.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# CASE statement
# The CASE statement goes through conditions and returns a value when the first condition is met (like an if-then-else statement). 
# So, once a condition is true, it will stop reading and return the result. If no conditions are true, it returns the value in the ELSE clause.
# If there is no ELSE part and no conditions are true, it returns NULL.
    # CASE
    #     WHEN condition1 THEN result1
    #     WHEN condition2 THEN result2
    #     WHEN conditionN THEN resultN
    #     ELSE result
    # END;

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Subqueries
# Subqueries refine how data are evaluated for inclusion in a main query.
# Generally, for each row in a main query, a subquery is a predicate statement that evaluates to true or false. 
# If the statement is true for the row, it is included in the result set; otherwise, it is not.
# Basic evaluations are specified using an equal sign, an IN key word, or an EXISTS key word. 
# When an equal sign is used, the subquery must return a single row with a single column. 
# It operates exactly like a value argument in a standard query.
# Subqueries can also provide valid column information by providing a value from a specific field in another related table or 
# by providing different information from different tables depending on a specific value.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Conditional Queries
# Conditional queries are a form of a subquery, 
# but they are used in a different manner. 
# Conditional queries are used either in the WHERE clause or within the actual SELECT clause, 
# providing different information depending on the value of a column.

# When used in a WHERE clause, the IN key word is used to relate a main query to a subquery, and the subquery generates rows that contain a single column of data. The main query specifies the column in conjunction with the IN key word. For each row in the main query, the value of that column is evaluated against the list of values generated by the subquery. If the value is contained in the subquery results, the main query row is included in the result set. The following example shows how the IN key word is used with a subquery:
    # SELECT
    #   FIRST_NAME, LAST_NAME, EMAIL
    # FROM
    #   tbl_member2
    # WHERE
    #   MEMBER_ID IN (
    #       SELECT
    #           tbl_Member_Member_ID
    #       FROM
    #           tbl_reservation)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# A conditional query can also be used within the SELECT column area and returns a value depending on the value of another column. 
# An example is to use a CASE statement to evaluate the column value and then run a SELECT statement on another table to return a result, as follows:

    # SELECT
    #   FIRST_NAME,
    #   Last_Name,
    #   EMAIL,
    #   CASE
    #       WHEN 
    #           IFNULL(Actual_Return_Date, CURDATE())
    #       THEN
    #           (SELECT
    #               Title
    #           FROM
    #               tbl_title
    #           WHERE
    #               TBL_CHECKOUT.tbl_Title_Copy_tbl_Title_Title_ID = tbl_title.Title_ID)
    #       ELSE (SELECT '')
    #  END AS TITLE_OVERDUE
    # FROM
    #   TBL_MEMBER2 LEFT join
    #       TBL_CHECKOUT ON TBL_MEMBER2.MEMBER_ID = TBL_CHECKOUT.TBL_MEMBER2_MEMBER_ID

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Joins
# -----
# CROSS JOIN
# The CROSS JOIN is used to generate a paired combination of each row of the first table with each row of the second table. 
# This join type is also known as cartesian join.
# # The Cartesian Product is a multiplication operation in the set theory that generates all ordered pairs of the given sets. 
# Suppose that, A is a set and elements are {a,b} and B is a set and elements are {1,2,3}. 
# The Cartesian Product of these two A and B is denoted AxB and the result will be like the following.
# # AxB ={(a,1), (a,2), (a,3), (b,1), (b,2), (b,3)}
    # SELECT ColumnName_1, 
    #        ColumnName_2, 
    #        ColumnName_N
    # FROM [Table_1]
    #      CROSS JOIN [Table_2]
# OR
    # SELECT ColumnName_1, 
    #        ColumnName_2, 
    #        ColumnName_N
    # FROM [Table_1],[Table_2]

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# INNER JOIN
# The INNER JOIN keyword selects records that have matching values in both tables.
# # Same as intersection of two sets
    # SELECT column_name(s)
    # FROM table1
    # INNER JOIN table2
    #   ON table1.column_name = table2.column_name;

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# FULL OUTER JOIN
# The FULL OUTER JOIN keyword returns all records when there is a match in left (table1) or right (table2) table records.
# # FULL OUTER JOIN and FULL JOIN are the same.
# # Same as union of two sets
    # SELECT column_name(s)
    # FROM table1
    # FULL OUTER JOIN table2
    #   ON table1.column_name = table2.column_name
    # WHERE condition;

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Aggregate functions
# -------------------
# COUNT function
# COUNT is the simplest function and is useful in counting the number of records that is expected to be returned by a SELECT statement.
    # SELECT COUNT(*)
    # FROM table
    # # returns num of rows
# or with the condition
    # SELECT COUNT(*)
    # FROM table
    # where salary > 50000
    # # return num of rows where salary more than 50000
# another useful example:
    # SELECT COUNT(DISTINCT job)
    # FROM table
    # return num of distinct jobs in table

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# AVG function
# The AVG() function returns the average value of an expression.
# # NULL values are ignored.
    # SELECT * FROM Products
    # WHERE Price > (SELECT AVG(Price) FROM Products);

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# SUM function
# The SUM() function returns the total sum of a numeric column. 
    # SELECT SUM(column_name)
    # FROM table_name
    # WHERE condition;
# or
    # SELECT name, SUM(daily_pages) AS total_pages
    # FROM writers
    # GROUP BY name
# which returns
    # name  total_pages
    # Jack  270 
    # Jill  220
    # John  250
# you can use SUM with IF clause
    # SELECT
    #     SUM(IF(status = 'Shipped', 1, 0)) AS Shipped,
    #     SUM(IF(status = 'Cancelled', 1, 0)) AS Cancelled
    # FROM orders

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MIN function
# The MIN() function returns the smallest value of the selected column.
    # SELECT MIN(column_name)
    # FROM table_name
    # WHERE condition;

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# MAX function
# The MAX() function returns the largest value of the selected column.
    # SELECT MAX(column_name)
    # FROM table_name
    # WHERE condition;

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

