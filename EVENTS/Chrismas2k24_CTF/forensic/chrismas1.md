# chall name: Christmas Toys Heist #1 

# description: 
```
 Christmas Toys Heist #1
100

When did the attack start?

Flag format: CMCTF{day:month:year_hour:minute:second}

Flag example: CMCTF{07:Jan:2003_12:06:06}

Author: t4f3

```

on website log file we found this line:
``192.168.1.100 - - [20/Dec/2024:00:01:31 +0100] "POST /upload.php HTTP/1.1" 200 789``
that is the start of the attack
# flag : CMCTF{20:Dec:2024:00:01:31}

