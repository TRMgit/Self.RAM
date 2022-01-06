num = 0
i = 0
byteamount=input("Amount of bytes?: ")
increasegrad=input("Gradually increase by: ")
x=input("Start? lag can occur. Program will run indefinitely. Use stop button to end process and to read output. y/n ")
while x== "y" or "1":
    print(memoryview(bytes(int((byteamount)))))
    num = num + 1
    byteamount = int(byteamount) + int(increasegrad)
    print(num ," successful scans")
    print(len(memoryview(bytes(int(byteamount)))), " bytes viewed.")
