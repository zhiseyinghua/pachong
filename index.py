from pasevices.chineseafs import Chineseafs
from services.mysql import MysqlOperation
from urllib import parse

if __name__ == '__main__':
    print("123")
    obj = MysqlOperation()  # 对象
    sql = """
        create table student(
        id int not null,
        name char(10),
        age int,
        address char(20),
        )
    """
    obj.__enter__()
    obj.execute(sql)
    obj.__exit__()