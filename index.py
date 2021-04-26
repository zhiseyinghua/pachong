from pasevices.chineseafs import Chineseafs
# from pasevices.financialData import FinancialData
from services.mysql import MysqlOperation
from urllib import parse
import asyncio


if __name__ == '__main__':
    chi = Chineseafs()  # 对象
    chi.getManyChineseafst(amount=387)
    # fin = FinancialData()  # 对象
    # fin.getManyChineseafst()


