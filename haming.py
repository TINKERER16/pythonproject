def sender():
    send = input("Enter the sending data in binary")
    length= len(send)
    a=0
    position=[]
    while pow(2,a)<=length:

        position.append(pow(2,a)-1)
        a+=1
    a-=1
    data_sent=[]
    for i in send:
        while len(data_sent) in position:
            data_sent.append(-1)
        data_sent.append(int(i))
    print(data_sent)
    # for i in position:
    #     i += 1
    #     temp = []
    #     c=i
    #     while c<=len():




def receiver():
    pass
a = int(input("Enter sender or receiver mode input0,1:"))
if a==0:
    sender()
if a==0:
    receiver()