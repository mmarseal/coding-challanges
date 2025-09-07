d1, m1, y1 = map(int, input().split()) #return date

d2, m2, y2 = map(int, input().split()) #expected return date

fine = 0 #default

if y1 > y2:
    fine = 10000
elif y1 == y2:
    if m1 > m2:
        fine = 500 * (m1 - m2)
    elif d1 > d2:
        fine = 15 * (d1 - d2)
        
print(fine)

"""
Sample Input:
STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)

Sample Output:
45
"""