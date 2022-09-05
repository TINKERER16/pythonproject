def sender():
    data=input("Enter the data to be sent in binary")
    key=input("Enter the  key ")
    for i in range(len(key)-1):
        data=data+"0"
    print(data)
    temp=[int(i) for i in data]
    print(temp)
sender()
# def crc(data,key):
#     a=0
#     while(a+len(key)<len(data)):
