stack = []

k = int (input())

for _ in range (k):
    input1 = int(input())
    if input1 == 0 :
        stack.pop()
    else :
        stack.append(input1)
print(sum(stack))