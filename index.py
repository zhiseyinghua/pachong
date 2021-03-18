from pasevices.chineseafs import Chineseafs
from services.mysql import MysqlOperation
from urllib import parse
import asyncio


if __name__ == '__main__':
    chi = Chineseafs()  # 对象
    chi.getManyChineseafst(amount=3)

