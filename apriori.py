def iunique(dataset):  # for single dataset#
    global count, elementsdone
    unique = []
    for i in dataset:
        for j in i:
            if j in elementsdone:
                pass
            else:
                unique.append([j])
                elementsdone.append(j)
    print(unique)
    counter(dataset, unique)


def counter(dataset, items):
    global min_count
    isavail = []
    for i in items:
        count = 0
        for j in dataset:
            if (set(i).issubset(set(j))):
                count += 1
        if count >= min_count:
            isavail.append(i)
    print(isavail)


transactions=int(input("Enter the no of transactions"))
dataset = []
count = []
elementsdone = []
for i in range(transactions):
    temp=[]
    no_tran=int(input(f"Enter the no of items in{i+1} transaction"))
    for j in range(no_tran):
        temp.append(input("Enter item name"))
    dataset.append(temp)
min_support=int(input("Enter minimum min_support in percentage 0-100"))
min_count = int(input("Enter the minimum count"))
iunique(dataset)