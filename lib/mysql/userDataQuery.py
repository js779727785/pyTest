#coding=utf-8
from lib.MySQLHelper import MySQLHelper
from lib.log import logger

# 根据telNum查询用户user表信息
def getUserInfo(telNum):
    sql = "select * from user where tel_num=%s and logical_del=0"
    params = (telNum)
    result = MySQLHelper("qydproduction").get_one(sql, params)
    if result is None:
        return None
    return result['id']

# 根据telNum查询用户关注公众号信息
def wechatAttentionInfo(telNum):
    sql = "SELECT * FROM wechat_attention_info WHERE ssoid = ( SELECT sso_id FROM user_profile WHERE id = ( SELECT id FROM user WHERE tel_num = %s ))"
    params = (telNum)
    result = MySQLHelper("qydproduction").get_one(sql, params)
    if result is None:
        return None
    return result['id']

# 根据ssoid查询用户基础信息
def getUserBaseInfo(ssoId):
    sql = "select * from user where logical_del=0 and id=(select id from user_profile where logical_del=0 and sso_id=%s)"
    params = (ssoId)
    result = MySQLHelper("qydproduction").get_one(sql, params)
    logger.info("the result is:")
    logger.info(result)
    return result

# 用户存管账户状态查询-判断用户身份
def getSsoIdByCheckUserRole(logical_del, user_role, status):
    sql = "select u.sso_id as ssoId,count(*) from xw_user_role xw INNER JOIN  user_profile u on xw.user_id=u.id where xw.logical_del=%s " \
          "and u.logical_del=0 and xw.user_role=%s and xw.`status`=%s  and u.sso_id is not NULL GROUP BY xw.user_id HAVING count(*)=1 " \
          "order by xw.create_time desc limit 1"
    params = (logical_del, user_role, status)
    result = MySQLHelper("qydproduction").get_one(sql, params)
    logger.info("the result is:")
    logger.info(result)
    return result

# 查询未开通存管角色的用户-判断用户身份
def getSsoIdByCheckUserRoleNotInXW(user_role):
    sql = "select sso_id as ssoId from user_profile where logical_del=0 and sso_id is not NULL and id not in (select user_id from " \
          "xw_user_role where user_role=%s) ORDER BY createtime desc limit 1"
    params = (user_role)
    result = MySQLHelper("qydproduction").get_one(sql, params)
    logger.info("the result is:")
    logger.info(result)
    return result

# 查询担保人是否在黑名单-判断用户身份
def getSsoIdByBestsignBlack(logical_del):
    sql = "select up.sso_id as ssoId from user_profile up INNER JOIN qydnewproduction.mt_bestsign_black mbb on up.sso_id = mbb.sso_id " \
          "where up.logical_del=0 and mbb.logical_del=%s ORDER BY up.createtime desc limit 1"
    params = (logical_del)
    result = MySQLHelper("qydproduction").get_one(sql, params)
    logger.info("the result is:")
    logger.info(result)
    return result

def getSsoIdByBestsignBlackNotIn():
    sql = "select sso_id as ssoId from user_profile where logical_del=0 and sso_id is not NULL and sso_id not in (select sso_id from " \
          "qydnewproduction.mt_bestsign_black ) ORDER BY createtime desc limit 1"
    result = MySQLHelper("qydproduction").get_one(sql, None)
    logger.info("the result is:")
    logger.info(result)
    return result