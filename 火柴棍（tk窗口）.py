import sys
import tkinter
from tkinter import ttk
from tkinter import *
from tkinter.ttk import *

def check():
    global num,ws
    num = numt.get('1.0','end').strip()
    ws = wst.get('1.0','end').strip()
    result.config(state=NORMAL)
    result.delete('1.0','end')
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
root.title("火柴棍（作业本 P59 T9") 
root.geometry('600x400+100+100')
ttk.Style().configure("TButton", padding=6, relief="flat",font=('微软雅黑', 15),
   background="#ccc")

frm = ttk.Frame(root, padding=10)
frm.grid()
label = ttk.Label(frm, text="火柴棍",font=("微软雅黑",20))
label.grid(column=0, row=0,sticky=NW)
numt = Text(frm,width=10, height=1,font=("微软雅黑",20))
numt.grid(column=0, row=1,sticky=W)
numt.insert('1.0', "火柴棍数量")
numt.bind('<FocusIn>', lambda event: numt.delete('1.0', 'end'))
wst = Text(frm,width=10, height=1,font=("微软雅黑",20))
wst.grid(column=1, row=1,sticky=W)
wst.insert('1.0', "输入位数")
wst.bind('<FocusIn>', lambda event: wst.delete('1.0', 'end'))
result = Text(frm,width=60, height=10,font=("微软雅黑",10),state=DISABLED)
result.grid(column=0, row=2,columnspan=3,pady=5)
btn = ttk.Button(frm, text="确定",command=check)
btn.grid(column=0, row=4,sticky=W)
quit = ttk.Button(frm, text="退出", command=root.destroy)
quit.grid(column=1, row=4,rowspan=2,sticky=W)
root.mainloop()