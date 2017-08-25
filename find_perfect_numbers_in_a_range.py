def is_perfect_number(number):
    divisors = []

    for i in range(1, number):
        if number % i == 0:
            divisors.append(i)

    sum_of_divisors = sum(divisors)
    return sum_of_divisors

# You can change the range. Default is 1000
max = 1000
for j in range(1, max+1):
    # print("{} {}".format(j, is_perfect_number(j)))
    if is_perfect_number(j) == j:
        print(j)
