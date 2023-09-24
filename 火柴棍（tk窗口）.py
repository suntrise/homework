import sys
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

global num1,ws1,num2,ws2
match = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
def check1():
    num1 = num1t.get('1.0','end').strip()
    res1 = 0
    res1t.config(state=NORMAL)
    res1t.delete('1.0','end')
    for i in range(len(num1)):
        res1 += match[int(num1[i])]
    res1t.insert('1.0',res1)
    print(res1)
    i=0
    res1=0
    res1t.config(state=DISABLED)

def check2():
    num2 = numt.get('1.0','end').strip()
    ws2 = wst.get('1.0','end').strip()
    result.config(state=NORMAL)
    result.delete('1.0','end')
    match = {0:6,1:2,2:5,3:5,4:4,5:5,6:6,7:3,8:7,9:6}
    count = []
    s = 0
    j = 0
    if num2.isdigit() and ws2.isdigit():
        num2 = int(num2)
        ws2 = int(ws2)
        for i in range(10**(ws2-1),10**ws2):
            ii = str(i)
            while j<len(ii):
                s += match[int(ii[j])]
                j+=1
            if s==num2:
                count.append(i)
            s=0
            j=0
        if count !=[]:
            result.insert('1.0',str(count))
            print("生成结果：",count)
        elif count == []:
            result.insert('1.0',"未找到符合要求的组合")
            print("未找到符合要求的组合")
    else:
        result.insert('1.0',"请输入数字！")
        print("请输入数字！")
    count = []
    result.config(state=DISABLED)

root = tkinter.Tk()
root.title("火柴棍") 
root.geometry('500x500+100+100')
ttk.Style().configure("TButton", padding=6, relief="flat",font=('微软雅黑', 15),
   background="#ccc")
label = ttk.Label(root, text="火柴棍（作业本P59 T9）by STR",font=("微软雅黑",20))
label.grid(column=0, row=0,sticky=NW)
frm2 = ttk.Frame(root, padding=10)
frm2.grid()
n = ttk.Notebook(root)
frm2 = ttk.Frame(n, padding=10)   
frm1 = ttk.Frame(n)
n.add(frm1, text='T9(2)')   
n.add(frm2, text='T9(3)')
n.grid(column=0, row=1,sticky=W)

#frm1 内部
frml1 = ttk.Label(frm1, text="输入一个数，查看它所需的火柴棍数量",font=("微软雅黑",15))
frml1.grid(column=0, row=0,columnspan=2,sticky=W)
numl1 = ttk.Label(frm1, text="输入：",font=("微软雅黑",20))
numl1.grid(column=0, row=1,columnspan=2,sticky=W)
num1t = Text(frm1,width=15, height=1,font=("微软雅黑",20))
num1t.grid(column=1, row=1,sticky=W)
resl1 = ttk.Label(frm1, text="结果：",font=("微软雅黑",20))
resl1.grid(column=0, row=2,sticky=W)
res1t = Text(frm1,width=15, height=1,font=("微软雅黑",20),state=DISABLED)
res1t.grid(column=1, row=2,sticky=W)
btn = ttk.Button(frm1, text="确定",command=check1)
btn.grid(column=0, row=3,sticky=W,pady=5)
quit = ttk.Button(frm1, text="退出", command=root.destroy)
quit.grid(column=1, row=3,rowspan=2,sticky=W,pady=5)

#frm2 内部
numl2 = ttk.Label(frm2, text="输入火柴棍数量：",font=("微软雅黑",18))
numl2.grid(column=0, row=1,sticky=W)
numt = Text(frm2,width=10, height=1,font=("微软雅黑",18))
numt.grid(column=1, row=1,sticky=W)
wsl2 = ttk.Label(frm2, text="输入位数：",font=("微软雅黑",18))
wsl2.grid(column=0, row=2,sticky=W)
wst = Text(frm2,width=10, height=1,font=("微软雅黑",18))
wst.grid(column=1, row=2,sticky=W)
result = Text(frm2,width=60, height=10,font=("微软雅黑",10),state=DISABLED)
result.grid(column=0, row=3,columnspan=4,pady=5)
btn = ttk.Button(frm2, text="确定",command=check2)
btn.grid(column=0, row=4,sticky=W)
quit = ttk.Button(frm2, text="退出", command=root.destroy)
quit.grid(column=1, row=4,rowspan=2,sticky=W)
root.mainloop()
