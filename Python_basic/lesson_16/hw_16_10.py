nums = [1,2,3,4,3,2]
new_nums = []
answer = []

for i_nums in range(len(nums)):
    for j_elem in range(i_nums, len(nums)):
        new_nums.append(nums[j_elem])
    print(new_nums)
    if new_nums == new_nums[::-1]:
        for i_answer in range(i_nums):
            answer.append(nums[i_answer])
        answer.reverse()
        break
    new_nums = []

print('Исходный список:', nums)
print('Нужно чисел для палиндрома:', len(answer))
print('Список этих чисел:', answer )