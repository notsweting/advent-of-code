ints = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six' : 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    '1': 1,
    '2': 2,
    '3': 3,
    '4' : 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8' : 8,
    '9': 9
}
nums = ['1','2','3','4','5','6','7','8','9', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
flag = True
ans = 0
while(flag):
    k = input()
    if k == 'end': break
    pos1 = 1e9
    num1 = -1
    pos2 = -1
    num2 = -1
    for i in nums:
        l = k.find(i)
        if(l != -1):
            if(l < pos1):
                pos1 = l
                num1 = ints[i]
        
        l = k.rfind(i)
        if(l != -1):
            if(l > pos2):
                pos2 = l
                num2 = ints[i]
    ans += num1*10 + num2

print(ans)
    


