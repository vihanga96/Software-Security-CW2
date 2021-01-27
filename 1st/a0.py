import a1
a1.generate_key()
key = a1.load_key()

# encrypt file
f = open("Video.mp4", "rb")
a1.encrypt_message(f.read())
# print(f.read())
f.close()

#decrypt File
f = open('encoded.file','rb')
a1.decrypt_message(f.read())
f.close()
