
import pymysql


class MysqlOperation():

    def __init__(self, host='localhost', user='root', pwd='533162903', port=3306, db='compangy_data'):
        self.host = host
        self.user = user
        self.password = pwd
        self.port = port
        self.dbname = db
        self.conn = None  # 连接
        self.cur = None  # 游标

    def open(self):
        # 创建连接
        print('创建连接',self.host,self.user)
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, port=self.port,
                                    db=self.dbname, charset='utf8')  # 创建连接
        self.cur = self.conn.cursor()  # 创建游标
        print("连接成功")

    def select(self, table_name, id):
        '''查询数据'''

        sql = "select pwd from %s where user_id = %s" % (table_name, id)
        self.cur.execute(sql)  # 查询数据
        return self.cur.fetchall()  # 获取结果

    def insert(self, sql, val):
        # 首先，查询该id是否已经存在了
        # id存在， 注册失败
        # id不存在， 将一条记录插入user表中，注册成功
        # result = self.select(table_name, id)
        # if result != ():
        #     return -1
        print( sql, val)
        self.cur.execute(sql,val)
        # else:
        #     sql = "insert into %s(user_id, pwd) values(%s,%s)" % (
        #         table_name, id, pwd)
        #     self.execute(sql)
        #     return 1
        # self.execute(sql)

    def delete(self, table_name, id):
        result = self.select(table_name, id)
        if result == ():
            print("该账号不存在")
        else:
            sql = "delete from %s where user_id = %s" % (table_name, id)
            self.execute(sql)
            print("删除成功")  # 也弹出一个对话框

    def update(self, table_name, id, pwd):
        result = self.select(table_name, id)
        if result == ():
            print("该账号不存在")
        elif pwd == result[0][0]:
            print("新密码与原密码一致")  # 该账号存在，但是密码并未改变
        else:
            sql = "update %s set pwd = %s where user_id = %s" % (
                table_name, pwd, id)
            self.execute(sql)
            print("密码更新成功")  # 也弹出一个对话框

    def execute(self, sql):
        '''执行sql'''
        try:
            self.cur.execute(sql)
            # 提交事务到数据库执行
            self.conn.commit()  # 事务是访问和更新数据库的一个程序执行单元

        except BaseException as f:
            print("执行sql语句错误")
            self.conn.rollback()

        # 返回受影响行数
        return self.cur.rowcount

    def executemany(self, sql, params):
        '''
        批量插入数据
        :param sql:    插入数据模版, 需要指定列和可替换字符串个数
        :param params:  插入所需数据，列表嵌套元组[(1, '张三', '男'),(2, '李四', '女'),]
        :return:    影响行数
        '''
        try:
            # sql = "INSERT INTO USER VALUES (%s,%s,%s,%s)"  # insert 模版
            # params = [(2, 'fighter01', 'admin', 'sanpang'),
            #           (3, 'fighter02', 'admin', 'sanpang')]  # insert数据，
            self.cur.executemany(sql, params)

        except BaseException as f:
            self.conn.rollback()

        return self.cur.rowcount

    def __enter__(self):
        print("MysqlOperation __enter__")
        self.open()
        return self

    def __exit__(self):
        print("退出时关闭游标关闭连接")
        '''退出时关闭游标关闭连接'''
        self.cur.close()
        self.conn.close()
