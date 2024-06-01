def min_edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    if m == 0:
        return n
    if n == 0:
        return m
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]

def get_user_input():
    string1 = input("Введите первую строку ")
    string2 = input("Введите вторую строку ")
    return string1, string2

if __name__ == "__main__":
    string1, string2 = get_user_input()
    result = min_edit_distance(string1, string2)
    print(f"Минимальное количество операций для конвертации '{string1}' в '{string2}' является: {result}")
