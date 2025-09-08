def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

if __name__ == '__main__':
    n = int(input("input number: ").strip())
    result = factorial(n)
    print(result)


"""
Sample Input: 3

Sample Output: 6
"""
