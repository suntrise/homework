print("火柴棍（作业本P59 T9(3)） by STR")
num = ''
ws = ''
def check():
    global num,ws
    num = input("请输入所需火柴棍：")
    ws = input("请输入位数：")
    match = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    count = []
    s = 0
    j = 0
    if num.isdigit() and ws.isdigit():
        num = int(num)
        ws = int(ws)
        for i in range(10**(ws-1),10**ws):
            ii = str(i)
            while j<len(ii):
                s += match[int(ii[j])]
                j+=1
            if s==num:
                count.append(i)
            s=0
            j=0
        if count !=[]:
            print("生成结果：",count)
        elif count == []:
            print("未找到符合要求的组合")
    else:
        print("请输入数字！")
    count = []

while num != 'q':
    check()
