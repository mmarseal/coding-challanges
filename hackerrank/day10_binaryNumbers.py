
def longest_ones_in_binary(n):
    binary_str = bin(n)[2:]
    
    current_count = 0
    max_count = 0
    
    for c in binary_str:
        if c == '1':
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0
    return max_count
            
            
if __name__ == '__main__':
    n = int(input().strip())
    result = longest_ones_in_binary(n)
    print(result)


"""
Sample Input 1: 
5

Sample Output 1: 
1

Sample Input 2:
13

Sample Output 2:
2
"""