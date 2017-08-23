# Example armstrong number: 1634
while True:
    number = input("Enter the number: ")
    sum = 0
    for i in number:
        sum += int(i) ** 4
    if sum == int(number):
        print("Armstrong number")
    else:
        print("Not armstrong number")
