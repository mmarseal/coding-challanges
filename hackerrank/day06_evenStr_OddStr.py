T = int(input())
for _ in range(T):
    S = input().strip()
    even = ""
    odd = ""

    for i in range(len(S)):
        if i % 2 == 0:
            even += S[i]
        else:
            odd += S[i]

    print(f"{even} {odd}")

"""
Sample Input:
2 
Hacker
Rank
"""