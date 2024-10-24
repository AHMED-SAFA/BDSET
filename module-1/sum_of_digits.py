# sum of digit

num = input()
str_num = str(num)
sum = 0

for i in str_num:
    int_index = int(i)
    sum += int_index

print(sum)
