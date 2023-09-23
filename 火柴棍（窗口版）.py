import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class win(QMainWindow):
    def __init__(self):
        super(win, self).__init__()
        self.init_ui()
        
    def init_ui(self):
        font = QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        fonte = QFont()
        fonte.setFamily("微软雅黑")
        fonte.setPointSize(16)
        fontres = QFont()
        fontres.setFamily("微软雅黑")
        fontres.setPointSize(11)
        fontbtn = QFont()
        fontbtn.setFamily("微软雅黑")
        fontbtn.setPointSize(12)

        self.setGeometry(100, 100, 700, 500)
        self.setWindowTitle('火柴棍')
        title = QtWidgets.QLabel(self)
        title.setText("火柴棍（作业本P59 T9(3)） by STR")
        title.setFont(font)
        title.adjustSize()
        title.move(20, 20)
        self.num = QtWidgets.QTextEdit(self)
        self.num.setFixedWidth(250)
        self.num.setFixedHeight(50)
        self.num.setFont(fonte)
        self.num.setPlaceholderText("请输入所需火柴棍")
        self.num.move(20, 80)
        self.ws = QtWidgets.QTextEdit(self)
        self.ws.setFont(fonte)
        self.ws.setFixedWidth(220)
        self.ws.setFixedHeight(50)
        self.ws.setPlaceholderText("请输入位数")
        self.ws.move(300, 80)
        self.result = QtWidgets.QTextEdit(self)
        self.result.setFont(fontres)
        self.result.setFixedWidth(500)
        self.result.setFixedHeight(230)
        self.result.setReadOnly(True)
        self.result.setPlaceholderText("结果")
        self.result.move(20, 150)
        self.btn = QtWidgets.QPushButton('确定',self)
        self.btn.setFont(fontbtn)
        self.btn.setFixedWidth(180)
        self.btn.setFixedHeight(50)
        self.btn.resize(self.btn.sizeHint())
        self.btn.clicked.connect(self.check)
        self.btn.move(20, 400)
        self.show()

    def check(self):
        num = self.num.toPlainText().strip()
        ws = self.ws.toPlainText().strip()
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
                self.result.setPlainText(str(count))
            elif count == []:
                self.result.setPlainText("未找到符合要求的组合")
            print("生成结果：",count)
        else:
            self.result.setPlainText("请输入数字！")
            print("请输入数字！")
        count = []

if __name__ == '__main__':
    app = QApplication(sys.argv)
    hcg = win()
    sys.exit(app.exec_())
