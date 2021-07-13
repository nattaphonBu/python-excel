import xlsxwriter

def main():
    file_name = 'python-excell.xlsx'
    workbook = xlsxwriter.Workbook(file_name)
    excel_format = workbook.add_format(
        {
            'bold': 1,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'fg_color': '#b3d9ff,
        }
    )
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', "Hello", excel_format)
    worksheet.write('A2', "Python", excel_format)
    worksheet.write('A3', "Excel", excel_format)
    workbook.close()

if __name__ == "__main__":
    main()
