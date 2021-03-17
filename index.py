from pasevices.chineseafs import Chineseafs
from services.mysql import MysqlOperation
from urllib import parse

if __name__ == '__main__':
    print("123")
    obj = MysqlOperation()  # 对象
    sql = """
        CREATE TABLE IF NOT EXISTS `company_phone`(
            `runoob_key`  VARCHAR(11) NOT NULL,
            `runoob_locla` VARCHAR(100) NOT NULL,
            `runoob_phone` VARCHAR(40) NOT NULL,
            `runoob_phone` VARCHAR(11) NOT NULL,
            `submission_date` DATE,
            PRIMARY KEY ( `runoob_key` )
        )ENGINE=compangy_data DEFAULT CHARSET=utf8;
    """
    obj.__enter__()
    obj.__exit__()
