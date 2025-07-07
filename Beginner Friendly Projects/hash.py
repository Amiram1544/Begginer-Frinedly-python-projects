import hashlib

#ramz==5656

target = "f0dd4a99fba6075a9494772b58f95280"


for i in range(10000):
    
    password = (f"{i:04d}")
            



    hashobj = hashlib.md5(password.encode())

    hashgen = hashobj.hexdigest()


    if hashgen == target:
        print(f"Correct, your password is {password}")
        break

else :
    print ("password peyda nashod")
    
        