def position_loc(array):
    a = 0
    position = []
    while pow(2, a) - 1 <= len(array):
        position.append(pow(2, a) - 1)
        a += 1
    a -= 1
    return position

def counter_one(i,data_sent):
    counter = i + 1

    c = i
    inc = counter
    count_one = 0
    while c < len(data_sent):
        while counter != 0 and c < len(data_sent):
            if int(data_sent[c]) == 1:
                count_one += 1
            c += 1
            counter -= 1
        counter = inc
        c += inc
    return count_one

def sender():
    send = input("Enter the sending data in binary")

    position=position_loc(send)
    data_sent=[]
    for i in send:
        while len(data_sent) in position:
            data_sent.append(-1)
        data_sent.append(int(i))

    for i in position:
        count_one=counter_one(i,data_sent)
        if count_one%2 == 0:
            data_sent[i] = 0
        else:
            data_sent[i] = 1

    print(f"The encrypted data sent is {data_sent}")




def receiver():
    encoded_data=input("Enter the received data")
    position=position_loc(encoded_data)

    error = []
    for i in position:

        count_one=counter_one(i,encoded_data)
        if count_one%2==0:
            error.append(False)
        else:
            error.append(True)
    if True not  in error:
        print("no error found in the code")




a = int(input("Enter sender or receiver mode input0,1:"))
if a==0:
    sender()
if a==1:
    receiver()