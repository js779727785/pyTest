# -*- coding: utf-8 -*-
import pymysql.cursors
import pymysql
import importlib, sys

from config import config
from lib.log import logger

importlib.reload(sys)


class mysqldb(object):
    def __init__(self, dbName):
        if dbName == "front":
            self.conn = config.front
        elif dbName == "account":
            self.conn = config.account
        elif dbName == "ucenter":
            self.conn = config.ucenter
        elif dbName == "qyddb":
            self.conn = config.qyddb
        elif dbName == "qydpaycenter":
            self.conn = config.qydpaycenter
        elif dbName == "qydaccount":
            self.conn = config.qydaccount
        elif dbName == "qydNewpaycenter":
            self.conn = config.qydNewpaycenter
        elif dbName == "qydNewpaycenter_QA":
            self.conn = config.qydNewpaycenter_QA
        elif dbName == "qyddb_QA":
            self.conn = config.qydproduction
        elif dbName == "che001":
            self.conn = config.che001_wl
        elif dbName == "qydnewproduction":
            self.conn = config.qydnewproduction
        elif dbName == "qydNmt":
            self.conn = config.qydNmt
        elif dbName == "qydloan":
            self.conn = config.qydloan
        elif dbName == "qydrepayment":
            self.conn = config.qydrepayment
        elif dbName == "qydaccount":
            self.conn = config.qydaccount
        elif dbName == "paycenter":
            self.conn = config.paycenter
        else:
            pass

    def selectsql(self, sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

    def updatesql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        try:
            cursor.execute(sql)
            # logger.info(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.error(e.message)

    def insertsql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()


if __name__ == '__main__':


    # sql_1 = "select user_id from loan_user_credit_line where sso_id= %s limit 1"
    # params_1 = "1115747561558587297"
    # sqlresult_1 = mysqldb("qydnewproduction").selectsql(sql_1 % params_1)
    params_2 = "30e66a5a-e53c-416b-bcf5-3446dded05f3"
    sql_2 = 'select repay_date FROM loan_loan WHERE borrower_id="' + str(params_2) + '" ORDER BY repay_date ASC'

    # print("查询1结果：" + str(sqlresult_1) + "取参结果：" + params_2)
    # print("bb659559")
    sqlresult_2 = mysqldb("qydnewproduction").selectsql(sql_2)
    firsttime = sqlresult_2[0]['repay_date']
    print("第二个查询结果："+str(firsttime))
    abc = (1,2,3)
    if type(abc) == tuple:
        print("hhahhah")
    print(type(abc))
"""以上三种方法足以进行mysql的查询和更新操作---最新框架"""





