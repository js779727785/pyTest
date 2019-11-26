# coding = UTF-8

import datetime
# Author: bai
# Time : 2018/11/8 10:11
import os
import time

parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
import sys

sys.path.append(parent_dir)
from lib.MySQLHelper import MySQLHelper
import matplotlib.pyplot as plt

from matplotlib.font_manager import FontProperties

from lib import send_email

font_set = FontProperties(fname=r"../lib/fonts/simsun.ttc", size=12)

daily_report_path = "../report/casebugs/"

# plt.rcParams['figure.dpi'] = 120
# 设置图片分辨率
plt.rcParams['savefig.dpi'] = 120


def get_yestday_bugs():
    """获取昨天的bug数量，保存柱状图，并返回总数量"""
    # sql = "select count(openedBy) as count,openedBy,openedDate from zt_bug where deleted='0' and DATE_FORMAT(openedDate,'%Y-%m-%d') =DATE_FORMAT((SELECT date_sub(curdate(),interval 1 day)),'%Y-%m-%d') group by openedBy order by count desc;"
    sql = "select count(1) as count,ztu.realname as reporter,ztb.openedDate from zt_bug ztb, zt_user ztu where ztb.openedBy = ztu.account and ztb.deleted='0' and DATE_FORMAT(ztb.openedDate,'%Y-%m-%d') =DATE_FORMAT((SELECT date_sub(curdate(),interval 1 day)),'%Y-%m-%d') group by reporter order by count desc;"
    bugs = MySQLHelper("zentao").selectsql(sql)
    name_list = []
    num_list = []
    for bug in bugs:
        name_list.append(bug["reporter"])
        num_list.append(bug["count"])
    plt.bar(range(len(num_list)), num_list, width=0.3, color='rgb', tick_label=name_list)
    xlist = list(range(len(num_list)))
    for xx, yy in zip(xlist, num_list):
        plt.text(xx, yy + 0.1, str(yy), ha='center')

    plt.ylabel("Bug数量", fontproperties=font_set)
    plt.title("测试团队Bug数量日统计 单位（个）", fontproperties=font_set)

    # 设置横轴label样式
    ax = plt.gca()
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(-35)
        label.set_ha("left")
        label.set_fontproperties(font_set)
    plt.tight_layout()

    image_path = os.path.abspath(
        daily_report_path + "bug" + time.strftime("%Y-%m-%d", time.localtime()) + ".png")
    plt.savefig(image_path)
    plt.close()
    return sum(num_list)


def get_yestday_cases():
    """获取昨天的用例数量，保存柱状图，并返回总数量"""
    # sql = "select count(openedBy) as count,openedBy,openedDate from zt_case where deleted='0' and DATE_FORMAT(openedDate,'%Y-%m-%d') =DATE_FORMAT((SELECT date_sub(curdate(),interval 1 day)),'%Y-%m-%d') group by openedBy order by count desc;"
    sql = "select count(1) as count,ztu.realname as reporter,ztc.openedDate from zt_case ztc, zt_user ztu where ztc.openedBy = ztu.account and ztc.deleted='0' and DATE_FORMAT(ztc.openedDate,'%Y-%m-%d') =DATE_FORMAT((SELECT date_sub(curdate(),interval 1 day)),'%Y-%m-%d') group by reporter order by count desc;"
    cases = MySQLHelper("zentao").selectsql(sql)
    name_list = []
    num_list = []
    for case in cases:
        name_list.append(case["reporter"])
        num_list.append(case["count"])
    plt.bar(range(len(num_list)), num_list, width=0.3, color='rgb', tick_label=name_list)
    xlist = list(range(len(num_list)))
    for xx, yy in zip(xlist, num_list):
        plt.text(xx, yy + 0.1, str(yy), ha='center')

    plt.ylabel("用例数量", fontproperties=font_set)
    plt.title("测试团队用例数量日统计 单位（个）", fontproperties=font_set)

    # 设置横轴label样式
    # 设置横轴label样式
    ax = plt.gca()
    for label in ax.xaxis.get_ticklabels():
        label.set_rotation(-35)
        label.set_ha("left")
        label.set_fontproperties(font_set)
    plt.tight_layout()

    image_path = os.path.abspath(
        daily_report_path + "case" + time.strftime("%Y-%m-%d", time.localtime()) + ".png")
    plt.savefig(image_path)
    plt.close()
    return sum(num_list)


if __name__ == "__main__":
    total_bugs = get_yestday_bugs()
    total_cases = get_yestday_cases()
    yestday = datetime.datetime.now() + datetime.timedelta(days=-1)
    content = "Hi All:<br><br> <h2>以下为测试组Bug和用例统计情况:</h2><h3 style=\"color:red \">Bug总数: " + str(
        total_bugs) + "</h3><h3 style=\"color:green \">用例总数: " + str(total_cases) + "</h3><br><hr>"
    title = "测试组工作产出日报 " + yestday.strftime("%Y-%m-%d")
    # send_email_mixed(content, title, os.path.abspath(daily_report_path))

