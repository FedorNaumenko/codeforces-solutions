import sys

def count_occurrences(n, a):
    m = len(a)

    resets = []
    for i in range(1, m):
        if a[i] == 1:
            resets.append(i)
        elif a[i] != a[i-1] + 1:
            return 0

    if not resets:
        need = a[0] + m - 1
        return max(0, n - (need - 1))  # = max(0, n - a1 - m + 2)

    # there is at least one reset
    end0 = a[resets[0] - 1]
    K0 = end0

    for j, idx in enumerate(resets):
        if a[idx - 1] != K0 + j:
            return 0

    K_last = K0 + len(resets)
    for i in range(resets[-1], m):
        if a[i] > K_last:
            return 0

    return 1 if K_last <= n else 0

def main():
    num_of_tests = int(input().strip())
    for _ in range(num_of_tests):
        # read n, m (skip blank lines if any)
        line = input().strip()
        while not line:
            line = input().strip()
        n, m = map(int, line.split())

        # read m integers possibly across multiple lines
        array_to_check = []
        while len(array_to_check) < m:
            parts = input().split()
            if parts:
                array_to_check.extend(map(int, parts))
        array_to_check = array_to_check[:m]

        print(count_occurrences(n, array_to_check))

if __name__ == "__main__":
    main()

