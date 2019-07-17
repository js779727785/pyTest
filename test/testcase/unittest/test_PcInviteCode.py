from config.demoUrl import base_url
import requests
from lib.log import logger
import unittest
from lib.mysql.userQuery import queryuser
class inviteCode(unittest.TestCase):

    def setUp(self) :
        logger.info("***开始测试***")

    def test_PcInviteCode(self):
        pho='19903581111'
        inviteCodeUrl="/nbigfront/entrance/yyapis/inviteCode/validate"
        url=base_url+inviteCodeUrl
        id=queryuser(pho)
        logger.info("id:"+str(id))
        if id is None:
            logger.info("phone不存在")
            return None
        data={"invitecodeid":pho,
            "_":1562035280723}
        r = requests.get(url=url,params=data)
        result=r.json()
        logger.info("result:"+str(result))
        self.assertEqual(result['code'],10000)




    def tearDown(self):
        logger.info("***tearDown***")


