def is_valid_input(n):
    return 3 <= n <= 20


def get_non_trivial_divisors(n):
    divisors = []
    for i in range(3, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors


def generate_pairs(simple_list, n):
    finale_str = ''
    x = 1
    for i in range(n // 2):
        for num in simple_list:
            y = num - x
            if y > 1 and y != x:
                finale_str += str(x) + str(y)
        x += 1
    return finale_str


def main():
    n = int(input("Enter a number between 3 and 20: "))

    if is_valid_input(n):
        simple_list = get_non_trivial_divisors(n)
        finale_str = generate_pairs(simple_list, n)
        print(finale_str)
    else:
        print('wrong')


print(main())