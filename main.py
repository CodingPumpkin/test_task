import re

expected_number_pattern = re.compile("^-?[0-9]+$")
    
def read_input():
    valid_input = False
    while not valid_input:
        s = input('Enter an integer: ' )
        if (re.match(expected_number_pattern, s)):
            n = int(s)
            valid_input = True
        else:
            print('Invalid input!')
    return n

max_sum_nums = [0]
max_sum = 0
n = read_input()
while not (n==0):
    cur_sum = sum([int(d) for d in str(n).replace('-', '')])
    if (cur_sum > max_sum):
        max_sum_nums = [n]
        max_sum = cur_sum
    elif (cur_sum == max_sum):
        max_sum_nums.append(n)
    n = read_input()

print(f'The max sum digits among input numbers is {max_sum}.')
print('The following numbers have this sum of digits:')
for num in max_sum_nums:
    print(f'{num}', end=' ')
print()
