def is_prime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    else:
        return True


def primepartition(num):
    if num > 0:
        for i in range(2, int(num / 2) + 1):
            if is_prime(i):
                if is_prime(num - i):
                    return True
    return False


def nestingdepth(string):
    num_of_nest = 0
    num_of_brackets_opened = 0

    for c in string:
        if c == '(':
            if num_of_brackets_opened == num_of_nest:
                num_of_nest += 1
            num_of_brackets_opened += 1
        if c == ')':
            if num_of_brackets_opened <1:
                return -1
            num_of_brackets_opened -= 1
    if num_of_brackets_opened == 0:
        return num_of_nest
    else:
        return -1


def rotatelist(l, k):
    k = k % len(l)
    return l[k:] + l[:k]
