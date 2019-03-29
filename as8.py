def check_if_plaindrome(string):
    if list(string.casefold()) == list(reversed(string)):
        return True
    else:
        return False

def get_largest_palindrome(size, string):
    for i in range(size):
        for j in range(i+1):
            if check_if_plaindrome(string[j:size-i+j]):
                print(str(size-i))
                print(string[j:size-i+j])
                return

def main():
    size = input()
    string = input()
    get_largest_palindrome(int(size), string)


if __name__ == '__main__':
    main()
