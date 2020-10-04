def nguyento(n):
    xam=0
    for i in range(1,n+1):
        if n%i==0:
            xam+=1
    if xam==2:
        return " LA SO NGUYEN TO"
    return "KHONG PHAI LA SO NGUYEN TO"
def TONG(n):
    sum=0
    for i in range(1,n+1):
        if nguyento(n):
            sum+=i
        print(sum)
n=int(input("Nhap So: "))
print(nguyento(n))
print(TONG(n))