import xlsxwriter

def main():
    file_name = 'python-excell.xlsx'
    workbook = xlsxwriter.Workbook(file_name)

    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "Hello")
    worksheet.write('A2', "Python")
    worksheet.write('A3', "Excel")
    workbook.close()

if __name__ == "__main__":
    main()
