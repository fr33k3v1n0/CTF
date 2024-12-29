# chall Name: love game

we are given this python script
 i think a made some modification, to simplify  the script 
```python
flag = 'REDACTED'

n = 22024?? ##complete the two last n value by yourself

output = []

s = 36


while (s>0):
    for j in range(0,35):
        for i in flag:
            output.append(hex(ord(chr((ord(i)^n + j - s)%256))))
            print(j)
        break
    break
    s-=1
print(output)

"""output = ['0x46', '0x65', '0x7c', '0x6f', '0x49', '0x5e', '0x4c',
	     '0x71', '0x73', '0x3a', '0x5f', '0x55', '0x66', '0x63',
	     '0x61', '0x6f', '0x55', '0x7e', '0x62', '0x3b', '0x79',
	     '0x55', '0x6d', '0x3e', '0x67', '0x6f', '0x55', '0x78',
	     '0x3b', '0x6d', '0x62', '0x7e', '0x35', '0x35', '0x77']"""


```
i write this autoSolve to get the flag

```python
flag = "LoveCTF{"
output = ['0x46', '0x65', '0x7c', '0x6f', '0x49', '0x5e', '0x4c', '0x71']
from string import printable

# brute force the two last digit
p = '22024'
fund = False
for i in range(10):
    for j in range(10):
        n = int(p + str(i) + str(j))
        result = []
        for l in flag:
            result.append(hex(ord(chr((ord(l)^n + 0 - 36)%256))))
        if result == output:
            fund = True
            break
    if fund:
        break



# get the flag now
print(f"n= {n}")
output = ['0x46', '0x65', '0x7c', '0x6f', '0x49', '0x5e', '0x4c',
             '0x71', '0x73', '0x3a', '0x5f', '0x55', '0x66', '0x63',
             '0x61', '0x6f', '0x55', '0x7e', '0x62', '0x3b', '0x79',
             '0x55', '0x6d', '0x3e', '0x67', '0x6f', '0x55', '0x78',
             '0x3b', '0x6d', '0x62', '0x7e', '0x35', '0x35', '0x77']


for t in output:
    for l in printable:
        if hex(ord(chr((ord(l)^n  - 36)%256))) == t:
            print(l, end='')


```

```bash
┌──(top0n3㉿top0n3)-[/media/…/ctf/loveCTf/reverse/theloveSCript]
└─$ python3 autsolve.py
n= 2202414
LoveCTF{y0U_like_th1s_g4me_r1ght??}
```

So we get the flag (very easy)
