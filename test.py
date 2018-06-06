import base64
from ceshi import *

Des_Key = "12345678"
data = '12351234'
Encryptdata = ''


def DesEncrypt(str):
    k = des(Des_Key, padmode=PAD_PKCS5)
    EncryptStr = k.encrypt(str)
    return base64.b64encode(EncryptStr)  # 转base64编码返回


a = data.encode('utf-8')
print(a)
Encryptdata = DesEncrypt(a).decode('utf-8')

print(Encryptdata)
def DesDecrypt(str):
    k = des(Des_Key, padmode=PAD_PKCS5)
    decrypt_str = k.decrypt(str)
    return base64.b64encode(decrypt_str)


b = Encryptdata.encode('utf-8')
print(b)
Decryptdata = DesDecrypt(b).decode('utf-8')
print(Decryptdata)