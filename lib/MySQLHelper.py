#coding=utf-8

import pymysql
from config import config
from lib.log import logger
class MySQLHelper(object):

    def __init__(self, dbName):
        if dbName == "paycenter":
            self.conn = config.qydNewpaycenter
        elif dbName == "qydproduction":
            self.conn = config.qyddb_QA
        elif dbName == "qydnewproduction":
            self.conn = config.qydnewproduction
        elif dbName == "dataGateway":
            self.conn = config.dataGateway
        elif dbName == "pushplatform":
            self.conn = config.pushplatform
        else:
            self.conn = config.qydnewproduction

    """查询返回只有一条结果"""
    def get_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        logger.info('the sql is : %s' % sql)
        logger.info('the params is : %s' % str(params))
        #cur = conn.cursor()
        cur.execute(sql, params)
        data = cur.fetchone()
        cur.close()
        conn.close()
        logger.info('the result data is :%s' % data)
        return data

    def get_many(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        logger.info('the sql is :%s' % sql)
        logger.info('the params is : %s' % str(params))
        cur.execute(sql, params)
        data = cur.fetchall()
        cur.close()
        conn.close()
        logger.info('the result data is :%s' % str(data))
        return data

    def insert_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor()
        logger.info('the sql is :%s' % sql)
        logger.info('the params is : %s' % str(params))
        cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'插入数据库成功'

    def insert_many(self, sql, params):
        conn = pymysql.connect(**self.conn)
        logger.info('the sql is :%s' % sql)
        logger.info('the params is : %s' % str(params))
        cur = conn.cursor()
        cur.executemany(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'批量插入数据库成功'

    def update_one(self,sql,params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        logger.info('the sql is :%s' % sql)
        logger.info('the params is : %s' % str(params))
        ret = cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'更新数据库成功'

    def update_oneLine (self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        logger.info('the sql is :%s' % sql)
        logger.info('the params is : %s' % str(params))
        ret = cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return ret

    def delete_one(self, sql, params):
        conn = pymysql.connect(**self.conn)
        cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
        logger.info('the sql is :%s' % sql)
        logger.info('the params is : %s' % str(params))
        ret = cur.execute(sql, params)
        conn.commit()
        cur.close()
        conn.close()
        return u'删除数据库成功'


    #add by tony
    def selectsql(self,sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        con.close()
        return data

    def updatesql(self,sql):
        con = pymysql.connect(**self.conn)
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            logger.info(sql)
            con.commit()
        except Exception as e:
            con.rollback()
            logger.error(e.message)

