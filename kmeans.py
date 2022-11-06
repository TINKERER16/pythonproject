import random

def select_centriod(no_of_clusters):
    global centriod1
    a = -1
    while no_of_clusters != 0:

        while a in centriod1 or a == -1:
            a = random .choice(datasets)
        centriod1.append(a)
        no_of_clusters -= 1

def cluster(centriod1):
    global  datasets,means
    minimum = -1
    clusters=[]
    for i in centriod1:
        temp = [i]
        clusters.append(temp)
    for i in datasets:
        if i not in centriod1:
            for j in clusters:
                dif = abs(j[0] - i)
                if dif < minimum or minimum == -1:
                    minimum = dif
                    pos = clusters.index(j)
                    a = clusters[pos]
            a.append(i)
            minimum=-1
    for element in clusters:
        means.append(element[0])
        if element[0] not in datasets:
            element.remove(element[0])
    return clusters


no_of_elements = int(input("Enter the no of elements in datasets"))
datasets = []
for i in range(no_of_elements):
    datasets.append(int(input(f"Enter the {i+1} element")))
no_of_clusters = int(input("Enter the no of clusters"))
centriod1 = []
means=[]
select_centriod(no_of_clusters)
centriod2=[]

while True:
    clusters1 = cluster(centriod1)
    for i in range(no_of_clusters):
        centriod2.append(round(sum(clusters1[i])/len(clusters1[i]),2))
    clusters2=cluster(centriod2)
    if clusters1!=clusters2:
        clusters1=clusters2
        centriod1=[]
        for i in range(no_of_clusters):
            centriod1.append(round(sum(clusters1[i]) / len(clusters1[i]),2))
        clusters2=[]
        centriod2=[]
    else:
        break
print(f"The final clusters are{clusters2}")
print(f"Final centriod are{centriod2}")