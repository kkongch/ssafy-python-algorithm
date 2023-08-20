tc = int(input())
for test_case in range(1,tc+1):
    lst = list(input().split())
    stack = []

    for i in range(len(lst)):
        if lst[i]=='.':
            if len(stack)>1:
                print(f'#{test_case} error')
                break
            else:
                print(f'#{test_case} {stack[0]}')
                break
        elif lst[i].isdigit():
            stack.append(int(lst[i]))
        elif lst[i] in '+-*/':
            if len(stack) < 2:
                print(f'#{test_case} error')
                break
            x2 = stack.pop()
            x1 = stack.pop()
            if lst[i] == '+':
                result = x1 + x2
            elif lst[i] == '-':
                result = x1 - x2
            elif lst[i] == '*':
                result = x1 * x2
            elif lst[i] == '/':
                if x2 == 0:
                    print(f'#{test_case} error')
                    break
                result = x1 // x2
            stack.append(result)


