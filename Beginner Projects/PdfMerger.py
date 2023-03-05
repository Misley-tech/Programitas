from pypdf import PdfMerger
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
        '(Corrección) Final IMA - Di Laudo, Misley, Rodriguez - 2022 2C.docx.pdf',
        'finales circuitos pt1.pdf',
        'Introduction_to_Convolutional_Neural_Networks_Wu.pdf'
    ]
    pdfeditor = PdfEditor(pdfs)
    pdfeditor.Merge(pdfs)
