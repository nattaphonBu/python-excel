import xlsxwriter

def main():
    file_name = 'python-excell.xlsx'
    workbook = xlsxwriter.Workbook(file_name)
    worksheet = workbook.add_worksheet()
    worksheet.merge_range('A1:D3', 'การทำ Python Excel')
    workbook.close()

if __name__ == "__main__":
    main()
