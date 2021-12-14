n = input()
n = int(n)
count = 0

for i in range (n+1):
    for j in range (60):
        for k in range (60):
            #if (str(i).find("3") == 1 ) or (str(j).find("3") == 1) or (str(k).find("3") == 1):
            # 틀린 조건
            if '3' in (str(i)+str(j)+str(k)):
                count = count+1
print(count)



