import sys
sys.path.append("")
from PyQt5.QtCore import Qt, QRect, QPoint
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QPainter, QBitmap, QPen, QBrush
from macro.config import config
from macro.config import config



'''
# setMask()的作用是为调用它的控件增加一个遮罩，遮住所选区域以外的部分，使之看起来是透明的。
# 它的参数可以为QBitmap或QRegion对象，此处调用QPixmap的mask（）函数获得图片自身的遮罩，是一个QBitmap对象，
# 在示例中使用的是Png格式，它的透明部分实际上就是一个遮罩
'''



@config.Singleton
class countWindow(QWidget):  # 不规则窗体
    """
    证明蒙版的作用，白色显示当前蒙版遮住的界面（不是gui界面，gui界面就是一个蒙版，可以看到蒙版的颜色是黑色，但可以通过设置界面透明度使黑色变成灰色），黑色遮蔽，mask之外的地方透明
    """
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setStyleSheet('''background-color:black; ''')

        self.pix = QBitmap(config.TMP_DIR + "/macro/modules/UI/icon/black.png")  # 蒙版
        self.resize(200, 200)  # 设置当前GUI主界面和蒙版图片一致

        desktop = QApplication.desktop()
        self.move((desktop.width() - 200) / 2, 300)
        
        self.cishu = 0
        self.image = config.TMP_DIR + "/macro/modules/UI/icon/number%d.png" % (3 - self.cishu)

    def initAndShow(self):
        self.cishu = 0
        self.image = config.TMP_DIR + "/macro/modules/UI/icon/number%d.png" % (3 - self.cishu)

    def Click(self):
        self.cishu = (self.cishu + 1) % 3
        if(self.cishu != 0):
            self.change_image()
        else:
            self.close()
            pass
  
    def paintEvent(self, event):  # 绘制窗口
        pp = QPainter(self.pix)  # 可以想象为给蒙版 pix 添加画手
        pen = QPen(Qt.red, 4)  # 钢笔
        # pen.setStyle(Qt.NoPen)  # 钢笔无颜色
        pp.setPen(pen)  # 可以想象为给画手钢笔
        brush = QBrush(Qt.white)   # 画刷，填充钢笔画的区域，填充白色是因为白色可以使蒙版透明
        pp.setBrush(brush)
        # 画一个矩形，【rectangle矩形】
        self.startPoint = QPoint(-2 , -2)
        self.endPoint = QPoint(405,305)
        pp.drawRect(QRect(self.startPoint, self.endPoint))  # 在蒙版mask上画矩形，
        pp.drawPixmap(0, 0, self.width(), self.height(), QPixmap(self.image))
        # 在蒙版mask上画矩形，使矩形以内蒙版是白色（可以说是在蒙版之外，使得gui界面透明了），以外蒙版是黑色
        
        self.setMask(self.pix)  # 把当前整个GUI界面设置为蒙版

    def change_image(self):    
        self.image = config.TMP_DIR + "/macro/modules/UI/icon/number%d.png" % (3 - self.cishu)
        self.paintEvent(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = countWindow()
    win.show()
    sys.exit(app.exec_())
