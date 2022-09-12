import json
def position_loc(array,b=0):
    a = 0
    position = []
    if b==0:
        while pow(2, a) - 1 <= len(array)+len(position):
            position.append(pow(2, a) - 1)
            a += 1
    else:
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
def error_checking(error,data_sent):
    temp=[]
    for j in error:
        i=pow(2,j)-1
        counter = i + 1
        c = i
        inc = counter
        temp1=[]
        while c < len(data_sent):
            while counter != 0 and c < len(data_sent):
                temp1.append(c)
                c += 1
                counter -= 1
            counter = inc
            c += inc
        temp.append(temp1)
    for i in temp[0]:
        if i in temp[1]:
            return i

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
    d=""
    for i in data_sent:
        d = d + str(i)

    with open("data.txt", "w") as t:
        t.write(json.dumps({"data": d}))

    print(f"The encrypted data sent is {d}")




def receiver():
    with open("data.txt") as t:
        t = t.read()
        dict = json.loads(t)
        encoded_data = dict["data"]
    position=position_loc(encoded_data,1)
    final_ans=[int(i) for i in encoded_data]
    error = []
    pos_error=[]
    for i in position:

        count_one=counter_one(i,encoded_data)
        if count_one%2==0:
            error.append(False)
        else:
            pos_error.append(len(error))
            error.append(True)
    if True not  in error:
        print("no error found in the code")
    else:

        print("error in the code")
        p=error_checking(pos_error,encoded_data)
        print(f"The error was at {p+1} position")
        if final_ans[p] == 0:
            final_ans[p]='1'
        else:
            final_ans[p]='0'

        print(f"The corrected data is{final_ans}")



while(True):
    a = int(input("Enter which mode 0.Sender 1.Reciver 2.Exit"))
    if a==0:
        sender()
    if a==1:
        receiver()
    if a==2:
        break