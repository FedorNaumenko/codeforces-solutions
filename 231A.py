# team

def main():
    num_of_tests = int(input().strip())
    implement_counter = 0
    for _ in range(num_of_tests):
        votes = list(map(int, input().strip().split()))
        if sum(votes) >= 2:
            implement_counter += 1
    print(implement_counter)

if __name__ == "__main__":
    main()