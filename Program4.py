input_string = input("Enter numbers separated by commas: ")
numbers = list(map(int, input_string.split(',')))

counts = {}

for i in range(1, 10):
    count = 0
    for num in numbers:
        if num % i == 0:
            count += 1
    counts[i] = count

print("Output:")
print(counts)
