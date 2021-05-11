#!/user/bin/python
import hashlib

hashvalue = input("* Enter a string to hash: ")

hashobject1 = hashlib.md5()
hashobject1.update(hashvalue.encode())
print("MD5 Hash Value: " + hashobject1.hexdigest())

hashobject2 = hashlib.sha1()
hashobject2.update(hashvalue.encode())
print ("Sha1 Hash Value: " + hashobject2.hexdigest())

hashobject3 = hashlib.sha256()
hashobject3.update(hashvalue.encode())
print ("Sha256 Hash Value: "+ hashobject3.hexdigest())

