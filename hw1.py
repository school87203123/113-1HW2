from typing import List, Tuple

def getResult(sentence: str) -> Tuple[List[List[chr]], List[List[chr]]]:
    # 宣告兩個二維陣列，分別為字母1和字母2
    alphabet: List[List[chr]] = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']
    ]
    alphabet2: List[List[chr]] = [
        ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')'],
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':'],
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?']
    ]
    return alphabet, alphabet2

def find_position(alphabet: List[List[chr]], alphabet2: List[List[chr]], char: str) -> Tuple[int, int]:
    # 先查找字元 S 在 alphabet 中的位置
    for i in range(len(alphabet)):
        for j in range(len(alphabet[i])):
            if alphabet[i][j] == char:
                return i, j
    # 如果字元 S 不在 alphabet 中，查找 alphabet2
    for i in range(len(alphabet2)):
        for j in range(len(alphabet2[i])):
            if alphabet2[i][j] == char:
                return i, j
    return -1, -1  # 如果找不到，返回 (-1, -1)

def process_tests(N: int, tests: List[Tuple[str, int]]) -> None:
    # 取得兩個二維陣列
    alphabet, alphabet2 = getResult("")
    
    # 定義二維陣列的大小
    rows = len(alphabet)      # 第幾個列表
    cols = len(alphabet[0])   # 第幾個元素

    # 依序處理每一筆測試資料
    for S, K in tests:
        # 找到字元 S 在 alphabet 或 alphabet2 中的位置
        row, col = find_position(alphabet, alphabet2, S)

        # 如果找不到字元 S，就打印 "Not Found"
        if row == -1 and col == -1:
            print("Not Found")
        else:
            # 根據 K 的值來決定輸出的方向
            if K == 1:  # 上
                new_row = (row - 1) % rows  # 向上移動
                print(alphabet[new_row][col])  # 在 alphabet 中輸出
            elif K == 2:  # 下
                new_row = (row + 1) % rows  # 向下移動
                print(alphabet[new_row][col])  # 在 alphabet 中輸出
            elif K == 3:  # 左
                new_col = (col - 1) % cols  # 向左移動
                print(alphabet[row][new_col])  # 在 alphabet 中輸出
            elif K == 4:  # 右
                new_col = (col + 1) % cols  # 向右移動
                print(alphabet[row][new_col])  # 在 alphabet 中輸出
        # 每筆資料換行
        print()

# 主程式，用於測試
N = int(input("請輸入測試資料的筆數: "))
tests = []

# 讀取每筆測試資料
for _ in range(N):
    S = input("請輸入要檢測的字元: ")
    K = int(input("請輸入方向 K (1: 上, 2: 下, 3: 左, 4: 右): "))
    tests.append((S, K))

# 呼叫函式處理輸入的測試資料
process_tests(N, tests)
