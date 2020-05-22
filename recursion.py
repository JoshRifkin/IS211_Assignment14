# Week 13, Assignment 14
# By Josh Rifkin


def fibonacci(n):
    if n <= 0:
        return "Please enter a number greater than or equal to 1"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b > a:
        return gcd(b, a)
    elif a % b == 0:
        return b
    return gcd(b, a % b)


def compareTo(s1, s2):
    s1, s2 = str(s1), str(s2)
    ls1, ls2 = len(s1), len(s2)
    if ls1 < ls2:
        return -1
    elif ls1 > ls2:
        return 1
    else:
        if ls1 == 0:
            return 0
        elif s1[0] == s2[0]:
            return compareTo(s1[1:], s2[1:])
        else:
            return ord(max(s1, s2))


def main():
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(5))
    print(fibonacci(20))
    print(gcd(30, 35))
    print(gcd(40, 80))
    print(gcd(23523, 3456))
    print(compareTo("apple", "appple"))
    print(compareTo("apple", "apple"))
    print(compareTo("appple", "apple"))
    print(compareTo("snickerdoodle", "apple"))
    print(compareTo("apple", "snickerdoodle"))


if __name__ == "__main__":
    main()
