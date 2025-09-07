import re #lib regex 



if __name__ == '__main__':
    N = int(input().strip())
    names = []

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        firstName = first_multiple_input[0]
        emailID = first_multiple_input[1]
        
        if re.match(r".+@gmail\.com$", emailID):
            names.append(firstName)
            
names.sort()
for name in names:
    print(name)
            
"""
Sample Input:
6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com

Sample Output:
julia
julia
riya
samantha
tanya
"""          
