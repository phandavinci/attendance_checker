from collections import Counter
#time table
prds = ['secure system', 'social', 'big data', 'project', 'image', 'robotics', 'supply chain']
# 0 - secure system
# 1 - social
# 2 - big data
# 3 - project
# 4 - image
# 5 - robotics
# 6 - supply chain
days = [{2:1, 3:4, 4:1, 6:1},
        {2:2, 1:1, 5:1, 4:1, 0:1},
        {5:3, 6:2, 4:1, 0:1},
        {2:2, 3:1, 0:1, 5:1, 1:1},
        {3:7}]


#attended
attended = [26, 19, 39, 115, 26, 31, 28]
total = [35, 24, 54, 130, 35, 36, 39]

#input
start = int(input("Enter the starting day:"))
n = int(input("Enter the number of days:"))
clgleave = {i:0 for i in range(5)}
off = {i:0 for i in range(5)}
for day in input("Enter the days when the clg is holiday:").split():
    clgleave[int(day)]+=1
for day in input("Enter the days you want to get off:").split():
    off[int(day)]+=1


#processing
for i in range(n):
    index = start%5
    curr = days[index]
    for prd in curr:
        if clgleave[index]>0:
            clgleave[index]-=1
        elif off[index]>0:
            total[prd] += curr[prd]
            attended[prd] -= curr[prd]
            off[index]-=1
        else:
            total[prd] += curr[prd]
            attended[prd] += curr[prd]

#printing
print("\n\n")
for i in range(7):
    currat = attended[i]
    currto = total[i]
    print(str(prds[i])+':\n'+"Percentage: "+str((currat/currto)*100)+"\n"+"Attended: "+str(currat)+"\n"+"Total:"+str(currto)+"\n")


