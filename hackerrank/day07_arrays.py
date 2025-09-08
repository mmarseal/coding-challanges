if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    reversed_arr = arr[::-1]
    print(" ".join(map(str, reversed_arr)))


"""
Sample Input:
4
1 4 3 2

Sample Output:
2 3 4 1
"""