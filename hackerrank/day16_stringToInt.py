S = input().strip()

try:
    print(int(S))

except ValueError:
    print("Bad String")


"""
Sample Input 0:
3

Sample Output 0:
3

Sample Input 1:
za

Sample Output 1:
Bad String
"""