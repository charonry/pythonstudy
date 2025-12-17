import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
from Crypto.Util.Padding import pad

origin_url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 "
                  "Safari/537.36",
    'Connection': 'close'
}

origin_data = {
    "rid": "R_SO_4_3324801830",
    "threadId": "R_SO_4_3324801830",
    "pageNo": "1",
    "pageSize": "20",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "csrf_token": ""
}
e = "010001"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a" \
    "5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c368" \
    "5b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7 "
g = "0CoJUm6Qyw8W8jud"
i = "7wt4ZMA8AAM2badn"


def getEncSecKey():
    return "cf8df4588ae9b9f1b3bddc169ec006dfb13320de78d798b0aca7d8ce47ccf7c3e9d7c3" \
           "3c139211c001e995bab4b6a1388d103019d1ff8b2b127db7f511fb86539f6b14086e54bd022031" \
           "8bd183791a88b2ef970dc76cd891c1d349e667b5cbb2e83e410413d9c7570f76bca6ce217b27dd" \
           "39fa12fdb8a075f977fef8184c30d0"


def getEncSecText(dataParam):
    first = enc_params(dataParam, g)
    second = enc_params(first, i)
    return second


def enc_params(value, key):
    iv = "0102030405060708"
    aes = AES.new(key=key.encode("utf-8"), IV=iv.encode("utf-8"), mode=AES.MODE_CBC)
    padded_value = pad(value.encode("utf-8"), AES.block_size, style='pkcs7')
    bs = aes.encrypt(padded_value)
    return str(b64encode(bs), "utf-8")


url_data = {
    "params": getEncSecText(json.dumps(origin_data)),
    "encSecKey": getEncSecKey()

}

resp = requests.post(origin_url, headers=headers, data=url_data)
hotComments = resp.json()["data"]["hotComments"]
content_list = []
for item in hotComments:
    content = item.get("content")
    content_list.append(content)
print(content_list)

""" 加密规则
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
var bVC6w = window.asrsea(JSON.stringify(i2x), bss7l(["流泪", "强"]), 
bss7l(Af7Y.md), bss7l(["爱心", "女孩", "惊恐", "大笑"]));
d + g =》第一次结果 + i =》第二次结果
"""
