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
    # print(data_sent)
    for i in position:
        counter=i+1
        temp = []
        c=i
        inc=counter
        count_one = 0
        while c < len(data_sent):
            while counter != 0 and c < len(data_sent):
                if data_sent[c] == 1:
                    count_one += 1
                c += 1
                counter -= 1
            counter = inc
            c += inc
        if count_one%2 == 0:
            data_sent[i] = 0
        else:
            data_sent[i] = 1

    print(f"The encrypted data sent is {data_sent}")




def receiver():
    pass
a = int(input("Enter sender or receiver mode input0,1:"))
if a==0:
    sender()
if a==0:
    receiver()