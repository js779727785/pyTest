import  requests
from lib.common.DemoLogin import qydFrontLogin
from lib.common.subminToken import subminToken
from config.demoUrl import qyd_url
from lib.log import logger
from lib.MySQLHelper import MySQLHelper


"""手动撤回处理中的轻盈撤资"""
def QY_CancleAssign(phone,pwd,assignIds):
    urlInfo="/entrance/mt/cacleAssign/json"
    token = qydFrontLogin(phone, pwd)
    headers = {"Content-type": "application/json", "X-Auth-Token": token}
    "submintToken"
    submitToken = subminToken(phone,pwd)
    # demoParams="{"assignIds":"198a40bc-835f-4aaf-9d00-3b0d94a1c1e1","submitToken":"099c679e-9bd8-42e5-a747-ec54e91694cc"}"
    parm={"assignIds":assignIds,"submitToken":submitToken}
    response= requests.post(url=qyd_url+urlInfo,json=parm,headers=headers)
    print(response)
    re=response.json()
    logger.info("请求结果："+str(re))

def queryOpenQY(phone):
    """查询撤资中的QY数据，返回assignIds"""
    sql_info="select * from mt_assignment where user_id=(select id from user where tel_num=%s) and `status`='OPEN' and (amount-already_amount-match_amount)!=0 ORDER BY create_time desc;"
    query_info=MySQLHelper("qydproduction").get_many(sql_info,phone)
    # if resultInfo is not None or resultInfo.__len__()>0:
    #     for i in range(resultInfo.__len__()):
    #         self.assertEquals(resultInfo[i]["sqlStatus"], testdata[0]['exceptStatus'])
    logger.info("撤资数据:"+str(query_info))
    if query_info is not None and query_info.__len__()>0:
        assignIds = []
        for i in range(query_info.__len__()):
            query_res=query_info[i]
            assignId=query_res['id']
            amount=query_res['amount']
            already_amount=query_res['already_amount']
            match_amount=query_res['match_amount']
            cancleAmount=(amount-already_amount-match_amount)/10000
            logger.info("撤资中assignId："+str(assignId)+"  ，可驳回金额："+str(cancleAmount))
            assignIds.append(assignId)
        logger.info("assignIds:"+str(assignIds))
        return assignIds
    else:logger.info("无处理中的撤资数据！！！")




#手动撤回处理中的轻盈撤资
# queryOpenQY('16803581611')
# QY_CancleAssign('16803581611','js123456','e52a7ea5-5dd2-4f13-8716-0b517866bb35')

