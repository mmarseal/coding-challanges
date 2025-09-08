if __name__ == '__main__':
    n = int(input())
    phonebook = {}
    
    for _ in range(n):
        name, phone = input().split()
        phonebook[name] = phone
        
    while True:
        try:
            query = input()
            if query in phonebook:
                print(f"{query}={phonebook[query]}")
            else:
                print("Not found")
        except EOFError:
            break

"""
Sample Input: 3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample Output:
sam=99912222
Not found
harry=12299933
"""