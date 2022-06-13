import xlsxwriter


def export_check(text):
    name = text[0]
    price = [float(i) for i in text[1]]
    count_name = [int(i) for i in text[2]]
    workbook = xlsxwriter.Workbook('res.xlsx')
    worksheet = workbook.add_worksheet()
    for row in range(len(name)):
        worksheet.write(name[row], price[row], count_name[row])

    workbook.close()


export_check([['pr1', 'pr2'], [200, 150], [3, 5]])