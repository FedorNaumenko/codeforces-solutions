# Way Too Long Words

def main():
    num_of_tests = int(input().strip())
    for _ in range(num_of_tests):
        word = input().strip()
        len_word = len(word)
        if len_word > 10:
            print(f"{word[0]}{len_word - 2}{word[-1]}")
        else:
            print(word)

if __name__ == "__main__":
    main()