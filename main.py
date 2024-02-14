n = int(input('Enter a number: '))
max_sum_nums = [0]
max_sum = 0
while not (n==0):
    cur_sum = sum([int(d) for d in str(n).replace('-', '')])
    if (cur_sum > max_sum):
        max_sum_nums = [n]
        max_sum = cur_sum
    elif (cur_sum == max_sum):
        max_sum_nums.append(n)
    n = int(input('Enter a number: '))

print(f'The max sum digits among input numbers is {max_sum}.')
print('The following numbers have this sum of digits:')
for num in max_sum_nums:
    print(f'{num}', end=' ')
print()
