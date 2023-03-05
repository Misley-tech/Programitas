from pypdf import PdfMerger
from pypdf import PdfReader
class PdfEditor:
    def __init__(self,pdfs):
        self.pdfs = pdfs

    def Merge(self,pdfs):
        merger = PdfMerger()

        for pdf in pdfs:
            merger.append(pdf)

        merger.write("result.pdf")
        merger.close()

if __name__ == "__main__":

    pdfs = [
        'Documento1.pdf',
        'Documento2.pdf',
        'Documento3.pdf'
    ]
    pdfeditor = PdfEditor(pdfs)
    pdfeditor.Merge(pdfs)