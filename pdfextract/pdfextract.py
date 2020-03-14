import os
from tkinter import Tk, filedialog as fd
from PyPDF2 import PdfFileReader, PdfFileWriter

root = Tk()
root.iconify()
filename = fd.askopenfilename(initialdir = "C:/",
                                        title = "选择PDF文件",
                                        filetypes = (("PDF Files", "*.PDF"), ("All files", "*.*")))
root.withdraw()
if filename:
    s = input('提取页码：')
    pages = []
    for p in s.split(','):
        rr = p.strip().split('-')
        if len(rr) > 1:
            pages += list(range(int(rr[0]), int(rr[1])+1))
        else:
            pages.append(int(p))
    fname, _ = os.path.splitext(os.path.basename(filename))
    pdf = PdfFileReader(filename)
    pdf_writer = PdfFileWriter()
    for page in pages:
        pdf_writer.addPage(pdf.getPage(page - 1))
    output_filename = f'{fname}_extracted.pdf'
    with open(output_filename, 'wb') as out:
        pdf_writer.write(out)
