if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif 2 <= n <= 5:
        print("Not Weird")
    elif 6<=n<=20:
        print("Weird")
    else:
        print("Not Weird")
        

"""
Output Format :
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0 : 
3

Sample Output 0: 
Weird

Sample Input 1: 
24

Sample Output 1: 
Not Weird
"""