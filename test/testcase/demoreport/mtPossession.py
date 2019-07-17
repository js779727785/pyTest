from lib.log import logger
import unittest
from lib.mysql.possession import queryMtPossession
from lib.mysql.userQuery import queryuser

headers = {"Content-type": "application/json"}
class mtPossession(unittest.TestCase):
    def setUp(self) -> None:
        logger.info("*"*20+"start")
    def test_queryMtPossession(self):
        userid=queryuser('16803581610')
        if userid is None:
            logger.info("userid is None")
            return None
        #先用一个queryuser查到的结果是json，提取之后传参
        re = queryMtPossession(userid['id'])
        print(re)
        #从多个loan_id中提取第一个loan_id
        print(re[0]['loan_id'])
        self.assertIsNotNone(re[0]['loan_id'],msg="re为空")

    def tearDown(self) -> None:
        logger.info("end")
