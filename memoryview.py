num = 0
i = 0
byteammount=input("Ammount of bytes?: ")
increasegrad=input("Gradually increase by: ")
x=input("Start? lag can occur. Program WILL crash after memory scanthrough is complete. y/n ")
while x== "y" or "1":
    print(memoryview(bytes(int((byteammount)))))
    num = num + 1
    byteammount = byteammount + increasegrad
    print(num ," successful scans")
    print(len(memoryview(bytes(int(byteammount)))), " bytes viewed.")
   