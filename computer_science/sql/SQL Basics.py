# Structured Query Language(SQL) as we all know is the database language by
#   the use of which we can perform certain operations on the existing database 
#   and also we can use this language to create a database. SQL uses certain commands 
#   like Create, Drop, Insert, etc. to carry out the required tasks. 

# Entity - table
# Attribute - column
# Record - row
# Relationship - association between entities
# Primary key:
#   unique identifier for a table
#   cannot be NULL
#   a table can have only one primary key
#   all columns in table are functionally dependent on A
# Foreign key:
#   primary key in another table
# Bridge / Linking table:
#   table that connects other tables
#   used to create one-many relationships instead of many-to-many
# one-to-many relationship:
#   one 'student' is related to many 'classes'
#   implement by having a common column in two or more tables
#   e.x.: 'STUDENT_ID' is a column in 'CLASSES' table and 'STUDENT_DATA' table

# Operators
# A traditional set of operators exists for the SQL, as follows:
#   != (not equal to)
#   = (equal to)
#   < (less than)
#   > (greater than)
#   <= (less than or equal to)
#   >= (greater than or equal to)

# Operators can work on both text and numerical data. 
# Similarly, a standard set of mathematical functions exist for the SQL, 
# but the following functions only work against numerical data elements:
#   + (add)
#   – (subtract)
#   / (divide)
#   * (multiply)

# Logical Comparison Operators
# A traditional set of logical comparison operators exists for the SQL, as follows:
#   AND
#   OR
#   NOT

# These SQL commands are mainly categorized into four (five) categories as: 
#   DDL – Data Definition Language
#   DQl – Data Query Language
#   DML – Data Manipulation Language
#   DCL – Data Control Language
#   *TCL - Transaction Control Language

# 1. DDL(Data Definition Language) : DDL or Data Definition Language actually consists 
#   of the SQL commands that can be used to define the database schema. It simply 
#   deals with descriptions of the database schema and is used to create and modify 
#   the structure of database objects in the database.

# Examples of DDL commands: 
#   CREATE – is used to create the database or its objects (like table, index, function, views, store procedure and triggers).
#   DROP – is used to delete objects from the database.
#   ALTER-is used to alter the structure of the database.
#   TRUNCATE–is used to remove all records from a table, including all spaces allocated for the records are removed.
#   COMMENT –is used to add comments to the data dictionary.
#   RENAME –is used to rename an object existing in the database.

# 2. DQL (Data Query Language) :

# DQL statements are used for performing queries on the data within schema objects. 
# The purpose of the DQL Command is to get some schema relation based on the query passed to it. 

# Example of DQL: 
#   SELECT – is used to retrieve data from the database.
#   INSERT
#   UPDATE
#   DELETE

# 3. DML(Data Manipulation Language): The SQL commands that deals with the manipulation 
# of data present in the database belong to DML or Data Manipulation Language and this 
# includes most of the SQL statements. 

# Examples of DML: 
#   INSERT – is used to insert data into a table.
#    UPDATE – is used to update existing data within a table.
#    DELETE – is used to delete records from a database table.

# 4. DCL(Data Control Language): DCL includes commands such as GRANT and REVOKE 
# which mainly deal with the rights, permissions and other controls of the database system. 

# Examples of DCL commands: 
#   GRANT-gives users access privileges to the database.
#   REVOKE-withdraw user’s access privileges given by using the GRANT command.

# 5. TCL(transaction Control Language): TCL commands deal with the transaction within the database. 

# Examples of TCL commands: 
#   COMMIT– commits a Transaction.
#   ROLLBACK– rollbacks a transaction in case of any error occurs.
#   SAVEPOINT–sets a savepoint within a transaction.
#   SET TRANSACTION–specify characteristics for the transaction.

# NORMALIZATION
# Normal forms are further described as follows:
#   1NF: This basically states that you must eliminate any duplicate columns within the same table. 
#       Another aspect of this standard is that separate tables should be created for each group of related data, 
#       and each record should have a unique column for the primary key.
#   2NF: This must meet the requirements of 1NF. In this process, you must also develop relationships between 
#       the tables normalized in 1NF and implement the use of foreign keys.
#   3NF: This must meet the requirements of 2NF. The new addition in this standard is to eliminate columns 
#       that are not dependent on the table’s primary key.
#   4NF: This must meet the requirements of 3NF. The only update to this standard that is different from 
#       the first three standards is that the table cannot contain more than one multivalued dependency.
#   5NF: This must meet the requirements of 4NF. It deals with a theory called join dependency.

# Conditional Queries
# Conditional queries are a form of a subquery, 
# but they are used in a different manner. 
# Conditional queries are used either in the WHERE clause or within the actual SELECT clause, 
# providing different information depending on the value of a column.

# Correlated Subquery
# If a subquery contains a reference to a table (or tables) named in the main query, 
# it is called a correlated subquery. 
# Correlated subqueries are used to evaluate columns in a main query directly against those in a subquery. 
# Correlation may be used in most subqueries and is necessary when evaluating columns in a main query against those in an EXISTS subquery, 
# although it is not a requirement in general.

# Single-row Subqueries
# Subqueries that return only one or zero row to the outer statement are called one-row or single-row subqueries. Single-row subqueries are used with a comparison operator in a WHERE or HAVING clause.
# Multiple-row Subqueries
# Subqueries that return more than one row (but only one column) to the outer statement are called multiple-row subqueries. Multiple-row subqueries are used with an IN, ANY, SOME, or ALL clause.


# JOINS
# Inner join: Only records in the left table and the right table with matching keys
# Left outer join: All records of the left table, with info from the right table only for those with matching keys
# Right outer join: All records of the right table, with info from the left table only for those with matching keys
# Full outer join: All records of both tables, with info from both tables only for those with matching keys; unmatched keys are added from each but with null for merged fields
# Self join: Join between two fields of the same table and records with no matching keys for outer joins receive null values for the merged fields. Outer joins differ from the inner joins only when the minimum cardinality of a relation is zero.
# Cross join: used to generate a paired combination of each row of the first table with each row of the second table. This join type is also known as cartesian join.

# Aggregate functions
# An aggregate function performs a calculation on a set of values, 
# and returns a single value. Except for COUNT(*), aggregate functions 
# ignore null values. Aggregate functions are often used with the GROUP BY 
# clause of the SELECT statement.
# All aggregate functions are deterministic. In other words, aggregate functions 
# return the same value each time that they are called, 
# when called with a specific set of input values.
# Use aggregate functions as expressions only in the following situations:
    # The select list of a SELECT statement (either a subquery or an outer query).
    # A HAVING clause.