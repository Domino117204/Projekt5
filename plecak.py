import itertools
import random

def generate_data(filename, n=10, max_capacity=50, max_value=100, max_weight=30):
    C = random.randint(max_capacity // 2, max_capacity)
    with open(filename, 'w') as f:
        f.write(f"{C}\n")
        f.write(f"{n}\n")
        for _ in range(n):
            value = random.randint(1, max_value)
            weight = random.randint(1, max_weight)
            f.write(f"{value} {weight}\n")
    print(f"Dane zapisane do pliku {filename}")

def read_data(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    C = int(lines[0].strip())
    n = int(lines[1].strip())
    items = [tuple(map(int, line.strip().split())) for line in lines[2:]]
    return C, n, items

def knapsack_dp(C, items):
    n = len(items)
    dp = [[0] * (C + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(C + 1):
            if weight > w:
                dp[i][w] = dp[i - 1][w]
            else:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)

    # Odtworzenie przedmiotów
    w = C
    taken = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            taken.append(items[i - 1])
            w -= items[i - 1][1]
    return dp[n][C], taken

def knapsack_brute_force(C, items):
    n = len(items)
    best_value = 0
    best_combination = []

    for r in range(1, n + 1):
        for combination in itertools.combinations(items, r):
            total_weight = sum(item[1] for item in combination)
            total_value = sum(item[0] for item in combination)
            if total_weight <= C and total_value > best_value:
                best_value = total_value
                best_combination = combination
    return best_value, best_combination

if __name__ == "__main__":
    filename = "dane.txt"
    generate_data(filename, n=10, max_capacity=50)

    C, n, items = read_data(filename)
    print(f"Pojemność plecaka: {C}, liczba przedmiotów: {n}")

    val_dp, items_dp = knapsack_dp(C, items)
    print("\n[Programowanie dynamiczne]")
    print(f"Maksymalna wartość: {val_dp}")
    print(f"Wybrane przedmioty (wartość, waga): {items_dp}")

    val_bf, items_bf = knapsack_brute_force(C, items)
    print("\n[Brute Force]")
    print(f"Maksymalna wartość: {val_bf}")
    print(f"Wybrane przedmioty (wartość, waga): {items_bf}")
