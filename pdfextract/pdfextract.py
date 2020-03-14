import os
# from tkinter import Tk, filedialog as fd
from PyPDF2 import PdfFileReader, PdfFileWriter

# root = Tk()
# root.iconify()
# filename = fd.askopenfilename(initialdir = "C:/",
                                        # title = "选择PDF文件",
                                        # filetypes = (("PDF Files", "*.PDF"), ("All files", "*.*")))
# root.withdraw()
filename = input('PDF文件：')
if filename:
    s = input('提取页码：')
    pages = []
    for p in s.split(','):
        rr = p.strip().split('-')
        if len(rr) > 1:
            pages += list(range(int(rr[0]), int(rr[1])+1))
        else:
            pages.append(int(p))
    pdf = PdfFileReader(filename)
    pdf_writer = PdfFileWriter()
    for page in pages:
        pdf_writer.addPage(pdf.getPage(page - 1))
    path, name = os.path.split(filename)
    fname, _ = os.path.splitext(name)
    with open(os.path.join(path, f'{fname}_extracted.pdf'), 'wb') as out:
        pdf_writer.write(out)
    os.system('pause')
