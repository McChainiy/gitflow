translater = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

arab_nums = []

for i in list(input()):
    arab_nums.append(translater[i])

print(arab_nums)
total_sum = 0
to_be_continued = False
for count, num in enumerate(arab_nums):
    if to_be_continued:
        to_be_continued = False
        continue
    if count == len(arab_nums) - 1:
        total_sum += num
        continue
    if count == 0 or arab_nums[count + 1] <= num:
        total_sum += num

    elif num < arab_nums[count + 1]:
        to_be_continued = True
        total_sum += arab_nums[count + 1] - num

    print(total_sum)


print(total_sum)
    #total_sum
