
import xlrd

print("a")


def read_excel():

    book = xlrd.open_workbook('pike.xlsx')
    sheet1 = book.sheets()[0]
    nrows = sheet1.nrows
    print('表格总行数', nrows)
    ncols = sheet1.ncols
    print('表格总列数', ncols)
    for item in [0, nrows]:
        # print(sheet1.cell(0, 2).value)
        for item in [0, ncols]:
            print(sheet1.cell(2, 2).value)
    # row3_values = sheet1.row_values(2)
    # print('第3行值', row3_values)
    # col3_values = sheet1.col_values(2)
    # print('第3列值', col3_values)
    cell_3_3 = sheet1.cell(2, 2).value

    print('第3行第3列的单元格的值：', cell_3_3)


# for item in range:
# 		print("a")
    # book = xlrd.open_workbook('pike.xlsx')
    # sheet1 = book.sheets()[0]
    # nrows = sheet1.nrows
    # print('表格总行数',nrows)
    # ncols = sheet1.ncols
    # print('表格总列数',ncols)
    # row3_values = sheet1.row_values(2)
    # print('第3行值',row3_values)
    # col3_values = sheet1.col_values(2)
    # print('第3列值',col3_values)
    # cell_3_3 = sheet1.cell(2,2).value
    # print('第3行第3列的单元格的值：',cell_3_3)
if __name__ == '__main__':
    read_excel()
