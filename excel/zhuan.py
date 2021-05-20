
import xlrd
import sys
from mysql import MysqlOperation

# 传入的数据


# tpye 表示插入的表，hang表示插入的主键


def _ref(_type, data):
    _type =  str(_type)
    print(_type, data)
    obj = MysqlOperation()  # 对象
    insertsql = 'INSERT ignore INTO excel(content,_image,_image1,_image2,content_time,ratesku,ratesku2,user,id)VALUES("' +data[0] + '","' +data[1] + '","' +data[2] +'","' +data[3] +'","' +data[4] +'","' +data[5] +'","' +data[6] +'","' +data[7]+'","'+_type+'")'
    print(insertsql)

    sql = """
            create table if not exists excel(
                content varchar(30) not null, 
                _image  varchar(30) not null,
                _image1 varchar(30) not null,
                _image2 varchar(30) not null,
                content_time    varchar(30) not null,
                ratesku  varchar(30) not null,
                ratesku2  varchar(30) not null,
                user  varchar(30) not null,
                id  varchar(30) not null,
                primary key ( `id` )
        )"""
    print("sql", _type, sql)
    obj.__enter__()
    obj.execute(sql)
    obj.execute(insertsql)  
    obj.__exit__()


def read_excel():
    book = xlrd.open_workbook('pike.xlsx')
    sheet1 = book.sheets()[0]
    nrows = sheet1.nrows
    # print('表格总行数', nrows)
    ncols = sheet1.ncols
    # print('表格总列数', ncols)
    _list = []
    for lie in range(nrows):
        # print(sheet1.cell(0, 2).value)
        for hang in range(ncols):

            print(lie, hang)
            #
            try:
                data = sheet1.cell(lie, hang).value
                if type(data) != "str":
                    data = str(data)
                else:
                    print()
                print("type", type(data))

                if (data == "" or data == None):
                    # print("数据为空", data)
                    _list.append("")
                else:
                    # _ref(lie, sheet1.cell(hang, lie).value, hang)
                    # print("dd")
                    _list.append(data)
            except:
                print("error")
                pass
                continue

            # print(/n)
        print("换行")
        # print("list", _list)
        _ref(lie, _list)
        _list.clear()


    # print('第3行第3列的单元格的值：', cell_3_3)
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
    # sys.exit()
