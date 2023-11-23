user_input = input()
user_input = user_input.lower()
total_sum = 0
for char in user_input:
    if char in 'aeiou':
        if char == 'a':
            total_sum += 1
        elif char == 'e':
            total_sum += 2
        elif char == 'i':
            total_sum += 4
        elif char == 'o':
            total_sum += 4
        elif char == 'u':
            total_sum += 5
print(total_sum)
