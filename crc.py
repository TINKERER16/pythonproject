def xor(data, key):
    a = 0
    for i in key:
        if int(i) == data[a]:
            data[a] = 0
        else:
            data[a] = 1
        a += 1
    return data


def crc(data, key,type):
    temp3 = [data[i] for i in range(len(data))]

    while (True):
        a = 0
        temp2 = []
        while (data[a] == 0 and a < len(data)-1):
            a += 1
        if (a + len(key) - 1 >= len(data)):
            break
        else:
            for i in range(len(key)):
                temp2.append(data[a])
                a += 1
            a -= len(key)
            b = xor(temp2, key)
            for i in range(len(key)):
                data[a] = b[i]
                a += 1
    if type==0:
        a += 1
        while (a < len(data)):
            b.append(data[a])
            a += 1
        b = b[-(len(key) - 1):]
        c = len(temp3) - len(key) + 1
        for i in range(len(key) - 1):
            temp3[c] = b[i]
            c += 1
        print(f"the checksum bit is {b}")
        print(f"The sending data is {temp3}")
    elif type==1:
        if 1 in data:
            print("There is error")
        else:
            print("This is proper data")


def sender():
    data = input("Enter the data to be sent in binary")
    key = input("Enter the  key ")
    for i in range(len(key) - 1):
        data = data + "0"
    print(f"before completging {data}")
    temp = [int(i) for i in data]
    crc(temp, key,0)
def reciver():
    data = input("Enter the data to be sent in binary")
    key = input("Enter the  key ")
    temp = [int(i) for i in data]
    crc(temp,key,1)

a=int(input("Enter which mode 0.Sender 1.Reciver"))
if a==0:
    sender()
elif a==1:
    reciver()