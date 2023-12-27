def levenshtein_distance(str1, str2):
    len1, len2 = len(str1), len(str2)
    dp = [[0] * (len2 + 1) for _ in range(len1 + 1)]

    for i in range(len1 + 1):
        dp[i][0] = i
    for j in range(len2 + 1):
        dp[0][j] = j

    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 1

            dp[i][j] = min(
                dp[i - 1][j] + 1,  # Удаление
                dp[i][j - 1] + 1,  # Вставка
                dp[i - 1][j - 1] + cost,  # Замена
            )

    return dp[len1][len2]


def main():
    print("Введите первую строку: ", end='')
    a = input()
    print("Введите вторую строку: ", end='')
    b = input()

    print("Расстояние Левенштейна: {}".format(levenshtein_distance(a, b)))


if __name__ == "__main__":
    main()
