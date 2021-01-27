import rsa
(public_key,private_key)=rsa.newkeys(512)
#Original file
f = open("original.txt", "rb")
crypto=rsa.encrypt(f.read(), public_key)
rsa.encrypt(f.read(),public_key)
f.close()
# #Encrypted File
f = open('encryptedData.txt','wb')
f.write(crypto)
f.close()
# #Decrypting and Save File
f = open('encryptedData.txt','rb')
tempFIle = f.read()
res = rsa.decrypt(tempFIle, private_key).decode()
f.close()
f = open('result.txt','w')
f.write(res)
