a, b = list(map(int, input().split()))
odd_num_sum = sum(num for num in range(a, b+1) if num % 2 != 0)
print(odd_num_sum)