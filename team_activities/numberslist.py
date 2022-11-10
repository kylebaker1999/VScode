import random

numbers = [16.2, 75.1, 52.3]

def append_random_numbers(numbers_list, quantity = 1):
    for i in range(quantity):
        num = round(random.uniform(0,100),2)
        numbers.append(num)

def main():
    print(numbers)
    append_random_numbers(numbers, quantity = 1)
    print(numbers)
    append_random_numbers(numbers, quantity = 3)
    print(numbers)

if __name__ == "__main__":
    main()


