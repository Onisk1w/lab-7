def count_routes(n, m):
    routes = [[0] * m for _ in range(n)]
    routes[0][0] = 1

    for i in range(n):
        for j in range(m):
            if i > 0:
                routes[i][j] += routes[i - 1][j]
            if j > 0:
                routes[i][j] += routes[i][j - 1]

    return routes[n - 1][m - 1]

def get_user_input():
    n = int(input("Количество строк "))
    m = int(input("Число столбцов  "))
    return n, m

def main():
    n, m = get_user_input()
    print(f"Количество маршрутов от А до B: {count_routes(n, m)}")

if __name__ == "__main__":
    main()
