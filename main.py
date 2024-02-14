n = int(input('Enter a number: '))
max_sum_num = 0
max_sum = 0
while not (n==0):
    cur_sum = sum([int(d) for d in str(n)])
    if (cur_sum > max_sum):
        max_sum_num = n
        max_sum = cur_sum
    n = int(input('Enter a number: '))

print(f'The number {max_sum_num} has the largest sum of digits.\nThe sum of its digits is {max_sum}. ')
