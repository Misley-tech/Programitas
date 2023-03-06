import sys
from pypdf import PdfMerger

from PyQt6.QtWidgets import(
    QApplication,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton
)

class Window(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.title = 'PDF Reader'
        self.left = 10
        self.top = 10
        self.width = 320
        self.height = 200
        self.initUI()

    def initUI(self):
        dialogLayout = QVBoxLayout()
        formLayout = QFormLayout()

        pdf1LineEdit = QLineEdit()
        formLayout.addRow("PDF 1:", pdf1LineEdit)

        pdf2LineEdit = QLineEdit()
        formLayout.addRow("PDF 2:", pdf2LineEdit)                

        pdf3LineEdit = QLineEdit()
        formLayout.addRow("PDF 3:", pdf3LineEdit)            

        pdf4LineEdit = QLineEdit()        
        formLayout.addRow("PDF 4:", pdf4LineEdit)        

        pdf5LineEdit = QLineEdit()       
        formLayout.addRow("PDF 5:", pdf5LineEdit)

        dialogLayout.addLayout(formLayout)
        self.setLayout(dialogLayout)

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        button = QPushButton('Merge', self)
        button.setToolTip('Merge')
        button.move(100,160)
        button.clicked.connect(self.on_click)

    def on_click(self,pdf1LineEdit):
        pdf1_text = pdf1LineEdit.text()
        print(f'esto son las {pdf1_text}')

        # merger = PdfMerger()

        # for pdf in range(pdfs):
        #     merger.append(pdf)

        # merger.write("result.pdf")
        # merger.close()

if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())