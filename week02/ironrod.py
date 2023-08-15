
stack = []
cnt = 0
lst = input()
rod = 0
for i in range(len(lst)):
    if lst[i]=='(':
        stack.append(lst[i])

    elif lst[i]==')' and lst[i-1]=='(':
        stack.pop()
        rod+=len(stack)
    elif lst[i]==')':
        stack.pop()
        rod+=1
print(rod)