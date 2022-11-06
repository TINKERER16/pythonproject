ip = str(input("Enter valid ip address"))
#program by Pranav Deshpande

def validate(ipaddress):
    if ipaddress.count(".") != 3:
        print("not valid ip")
        return 1
    else:
        ipad = list(ipaddress.split("."))
        a = True
        for i in ipad:
            if int(i) > 255 or int(i) < 0 or int(i[0]) == 0:
                a = False
        if a:
            print("Valid ip")
            return ipad
        else:
            print("invalid ip")
            return 1


test1 = validate(ip)
if test1 != 1:
    first = int(test1[0])
    if first <= 127:
        print("The ip is from class A")

       # print(f"The net id is {test1[0]}")
       # print(f"The host id is {test1[1]+'.'+test1[2]+'.'+test1[3]}")
        print("The subnet mask is 255.0.0.0")
    elif first > 127 and first <= 191:
        print("The ip is from class B")

       # print(f"The net id is {test1[0]+'.'+test1[1]}")
        #print(f"The host id is {test1[2] + '.' + test1[3]}")
        print("The subnet mask is 255.255.0.0")

    elif first > 191 and first <= 223:
        print("The ip is from class C")

       # print(f"The net id is {test1[0] + '.' + test1[1]+'.'+test1[2]}")
       # print(f"The host id is {test1[2] + '.'+test1[3]}")
        print("The subnet mask is 255.255.255.0")
    elif first > 223 and first <= 239:
        print("The ip is from class D")

       # print(f"The net id is {test1[0] + '.' + test1[1] + '.' + test1[2]+'.'+test1[3]}")
    else:
        print("The ip is from class E")

        #print(f"The net id is {test1[0] + '.' + test1[1] + '.' + test1[2] + '.' + test1[3]}")
    # netid = ""
    # for i in range(a):
    #     netid += test1[i]
    #     if a - i != 1:
    #         netid += '.'
    # b = 4 - a
    # if b != 0:
    #
    #     hostid = ""
    #     while a < 4:
    #         hostid += test1[a]
    #         a += 1
    #         if a != 4:
    #             hostid += '.'
    #
    # print(f"The net id is{netid}")
    # print(f"The host id is{hostid}")