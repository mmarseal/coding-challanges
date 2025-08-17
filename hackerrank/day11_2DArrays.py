if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    max_sum = -63
    
    for i in range(4):
        for j in range(4):
            top = arr[i][j] + arr[i][j+1] + arr[i][j+2]
            mid = arr[i+1][j+1]
            bot = arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            hourglass_sum = top + mid + bot
            
            if hourglass_sum > max_sum:
                max_sum = hourglass_sum
                
    print(max_sum)


"""
Sample Input

1 1 1 0 0 0
0 1 0 0 0 0
1 1 1 0 0 0
0 0 2 4 4 0
0 0 0 2 0 0
0 0 1 2 4 0

Sample Output

19
"""