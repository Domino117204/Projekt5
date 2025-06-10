import time
import csv
from plecak import generate_data, read_data, knapsack_dp, knapsack_brute_force

def benchmark_time_vs_n(filename, max_n=18, step=2, constant_capacity=50):
    with open("benchmark_n_dp.csv", "w", newline="") as dp_file, \
         open("benchmark_n_bf.csv", "w", newline="") as bf_file:

        dp_writer = csv.writer(dp_file)
        bf_writer = csv.writer(bf_file)

        dp_writer.writerow(["n", "ms"])
        bf_writer.writerow(["n", "ms"])

        for n in range(2, max_n + 1, step):
            generate_data(filename, n=n, max_capacity=constant_capacity)
            C, _, items = read_data(filename)

            # Dynamic Programming
            start = time.time()
            knapsack_dp(C, items)
            dp_time_ms = (time.time() - start) * 1000

            # Brute Force
            start = time.time()
            knapsack_brute_force(C, items)
            bf_time_ms = (time.time() - start) * 1000

            dp_writer.writerow([n, round(dp_time_ms, 3)])
            bf_writer.writerow([n, round(bf_time_ms, 3)])

            print(f"n={n}: DP={dp_time_ms:.3f}ms, BF={bf_time_ms:.3f}ms")


def benchmark_time_vs_C(filename, max_C=100, step=10, constant_n=12):
    with open("benchmark_C_dp.csv", "w", newline="") as dp_file, \
         open("benchmark_C_bf.csv", "w", newline="") as bf_file:

        dp_writer = csv.writer(dp_file)
        bf_writer = csv.writer(bf_file)

        dp_writer.writerow(["C", "ms"])
        bf_writer.writerow(["C", "ms"])

        for C in range(10, max_C + 1, step):
            generate_data(filename, n=constant_n, max_capacity=C)
            _, _, items = read_data(filename)

            # Dynamic Programming
            start = time.time()
            knapsack_dp(C, items)
            dp_time_ms = (time.time() - start) * 1000

            # Brute Force
            start = time.time()
            knapsack_brute_force(C, items)
            bf_time_ms = (time.time() - start) * 1000

            dp_writer.writerow([C, round(dp_time_ms, 3)])
            bf_writer.writerow([C, round(bf_time_ms, 3)])

            print(f"C={C}: DP={dp_time_ms:.3f}ms, BF={bf_time_ms:.3f}ms")


if __name__ == "__main__":
    filename = "benchmark_dane.txt"

    print("=== Benchmark: czas (ms) vs liczba przedmiotów (n) ===")
    benchmark_time_vs_n(filename)

    print("\n=== Benchmark: czas (ms) vs pojemność plecaka (C) ===")
    benchmark_time_vs_C(filename)
