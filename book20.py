n = int(input("Nhập n:"))
def tinhtong():
    x = 0
    for i in range(1, n):
        i+=1
        x += pow(i,3)
    print(x)
tinhtong()