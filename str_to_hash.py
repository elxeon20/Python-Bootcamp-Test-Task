
n = int(input())
list = []
for i in range(n):
    list = [[0 for x in range(2)] for y in range(n)]
for i in range(n):
    list[i] = input().split()
list2 = []
for i in range(int(input())):
    list2.append(input())
for i in list2:
    for d in range(n):
        if i in list[d]:
            print(list[d][0])

                   
            