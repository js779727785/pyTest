import logging
from BusinessTools.models import *

logger = logging.getLogger('DataFactoryTools')


def add_stu_account(**kwargs):
    """
    添加学生账户
    :param kwargs:
    :return:
    """

    stu_opt = StudentAccount.objects
    try:
        stu_opt.insert_stu_account(**kwargs)
    except Exception as e:
        print(e)
        logging.error('学生账户添加失败：{kwargs}'.format(kwargs=kwargs))
    logger.info('学生账户添加成功：{kwargs}'.format(kwargs=kwargs))


def add_tea_account(**kwargs):
    """
    添加老师账户
    :param kwargs:
    :return:
    """

    tea_opt = TeacherAccount.objects
    try:
        tea_opt.insert_tea_account(**kwargs)
    except Exception as e:
        print(e)
        logging.error('老师账户添加失败：{kwargs}'.format(kwargs=kwargs))
    logger.info('老师账户添加成功：{kwargs}'.format(kwargs=kwargs))


def update_account(cate, uid):
    """
    更新学生或老师账户状态
    :return:
    """
    stu_opt = StudentAccount.objects
    tea_opt = TeacherAccount.objects
    try:
        if cate and cate == "学生":
            stu_opt.update_stu_account(uid)
        elif cate and cate == "老师":
            tea_opt.update_tea_account(uid)
        else:
            raise "注销账户失败，cate为空或不存在：{cate}".format(cate=cate)
    except Exception as e:
        return e
