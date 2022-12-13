r_n = {'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000 }

s = 'MCMXC'
num = 0
lent = len(s)
right = 1
left = 0
x = 0
y = 0


while right < lent:
    if r_n[s[right]] > r_n[s[left]] :
        x += 1
        num = num + (r_n[s[right]] - r_n[s[left]])
        right += 2
        left += 2
    else:
        y += 1
        num = num +  r_n[s[left]]
        right += 1
        left +=1
try:
    if r_n[s[right-1]] <= r_n[s[left-1]] :
        num = num + r_n[s[left]]
except:
    print("")
print(num)



    
