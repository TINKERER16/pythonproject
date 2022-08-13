def sender():
    send = input("Enter the sending data in binary")
    length= len(send)
    a=0
    while pow(2,a)<=length:
       a+=1
    a-=1
    print(a)


def receiver():
    pass
a = int(input("Enter sender or receiver mode input0,1:"))
if a==0:
    sender()
if a==0:
    receiver()