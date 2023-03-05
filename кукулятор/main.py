import sys

from PyQt6.QtWidgets import QApplication

from func import MainWindow
from PyQt6.QtGui import QFont, QFontDatabase

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet("""
        QLabel {
            background-color: #A3AAAA;
            font-size: 60px;
            font-weight: bold;
        }
        QLabel::hover {
            background-color: rgba(1, 1, 1, 6);
        }
           
        QMainWindow {
            background-color: #A3C1DA;
            font-size: 45px;
            font-weight: bold;
            border-radius: 5%;
            border-style: solid;
            border-width: 2px;
            border-color: #FFFFF;
            color: purple;
        }
        QPushButton::hover {
            background-color: rgba(1, 1, 1, 6);
        }
        QPushButton {
            background-color: #A5CDRF;
            Width: 270px;
            min-height: 100px;
            max-height: 150px;
            font-size: 75px;
            font-weight: bold;
            border-color: #FFFFF;
            color: purple
            
            
        }
       
                            
                               
    """)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()