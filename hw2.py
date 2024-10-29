def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# 讓使用者輸入數字並轉換為整數列表
user_input = input("請輸入一組數字，數字之間用空格分隔: ")
nums = list(map(int, user_input.split()))

missing_number = find_missing_number(nums)
print("缺少的數字是:", missing_number)
