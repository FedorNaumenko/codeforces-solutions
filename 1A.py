def main():
    n, m, a = map(int, input().split())

    tiles_n = (n+a-1) // a
    tiles_m = (m+a-1) // a

    print(tiles_n*tiles_m)

if __name__ == "__main__":
    main()