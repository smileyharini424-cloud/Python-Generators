def generate_numbers(limit):
    number = 1

    while number <= limit:
        yield number
        number += 1


limit = int(input("Enter the limit: "))

print("Generated Numbers:")

for number in generate_numbers(limit):
    print(number)
