n = input()
n = int(n)
count = 0
for i in range (0, n+1):
    for j in range (0, 60):
        for k in range (0, 60):
            if (str(i).find("3") == 1) or (str(j).find("3") == 1) or (str(k).find("3") == 1):
                count = count+1
print(count)