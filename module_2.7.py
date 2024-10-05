n = int(input())
finale_str = ''
x = 1
simple_list = []


if 3 <= n <= 20:
    for i in range(n):
        if n % (i + 1) == 0 and i + 1 != 1 and i + 1 != 2:
            simple_list.append(i + 1)


    for i in range(n // 2):
        for num in simple_list:
            y = num - x
            if y > 1 and y != x:
                finale_str += str(x) + str(y)
        x += 1


    print(finale_str)


else:
    print('wrong')



