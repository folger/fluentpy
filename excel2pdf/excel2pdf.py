from win32com import client

def exceltopdf(doc):
    excel = client.DispatchEx("Excel.Application")
    excel.Visible = 0

    wb = excel.Workbooks.Open(doc)
    ws = wb.Worksheets[0]

    try:
        wb.SaveAs('D:\\result.pdf', FileFormat=57)
    except Exception as e:
        print("Failed to convert")
        print(str(e))
    finally:
        wb.Close()
        excel.Quit()

if __name__ == '__main__':
    exceltopdf('')
