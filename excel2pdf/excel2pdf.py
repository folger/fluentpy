import os
from win32com import client

def exceltopdf(doc):
    if not doc:
        return
    excel = client.DispatchEx("Excel.Application")
    excel.Visible = 0
    wb = excel.Workbooks.Open(doc)
    ws = wb.Worksheets[0]

    try:
        fname, _ = os.path.splitext(os.path.basename(doc))
        wb.SaveAs(fname, FileFormat=57)
    except Exception as e:
        print("Failed to convert")
        print(str(e))
    finally:
        wb.Close()
        excel.Quit()
        os.system('pause')

if __name__ == '__main__':
    exceltopdf(input('Excel文件：'))
