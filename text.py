s=int(input("Enter the no of subjects"))
marks=[]
for i in range(s):
    marks.append(float(input(f"Enter the marks in sub{i+1}")))
totalmarks=s*100
totalmm=0
for i in marks:
    totalmm=totalmm+i
percentage=(totalmm/totalmarks)*100
print(f"The marks in the subject are{marks}",end="\n")
print(f"The total percentage is{percentage}")