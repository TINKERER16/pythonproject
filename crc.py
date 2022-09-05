def xor(data, key):
    a = 0
    for i in key:
        if int(i) == data[a]:
            data[a] = 0
        else:
            data[a] = 1
        a += 1
    return data


def crc(data, key):
    temp3 = [data[i] for i in range(len(data))]

    while (True):
        a = 0
        temp2 = []
        while (data[a] == 0 and a < len(data)):
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
    a += 1
    while (a < len(data)):
        b.append(data[a])
        a += 1
    b = b[-(len(key) - 1):]
    c = len(temp3) - len(key) + 1
    for i in range(len(key) - 1):
        temp3[c] = b[i]
        c += 1
    print(temp3)


def sender():
    data = input("Enter the data to be sent in binary")
    key = input("Enter the  key ")
    for i in range(len(key) - 1):
        data = data + "0"
    print(f"before completging {data}")
    temp = [int(i) for i in data]
    crc(temp, key)


sender()