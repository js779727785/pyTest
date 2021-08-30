def get_create_order_param(kid, uid):
    """
    获取创建订单入参
    :param kid:
    :param uid:
    :return:
    """
    # 菲教课
    if kid == 300865594013722:
        data_json_create_order = "{\"uid\":" + str(uid) + ",\"price\":998000,\"curriculums\":[{" \
                                                          "\"kid\":300865594013722,\"sectioncn\":200,\"spec\":0}]," \
                                                          "\"expiremins\":1440,\"scoredays\":720," \
                                                          "\"packageid\":303182049372170,\"manualgive\":null," \
                                                          "\"installment\":0,\"name\":\"【菲教预售】20单元特惠套餐\"," \
                                                          "\"bookprice\":0,\"makeid\":null,\"invitediscount\":0} "
    # 启蒙欧美课
    elif kid == 384878474279176:
        data_json_create_order = "{\"uid\":" + str(uid) + ",\"price\":288000,\"" \
                                                          "curriculums\":[{\"kid\":384878474279176,\"sectioncn\":24,\"spec\":0}]," \
                                                          "\"expiremins\":1440,\"scoredays\":0,\"packageid\":388315300729090," \
                                                          "\"manualgive\":null,\"installment\":0,\"name\":\"启蒙欧美永久\",\"bookprice\":0," \
                                                          "\"makeid\":null,\"invitediscount\":0}"
    # 启蒙菲教课
    elif kid == 387362146756864:
        data_json_create_order = "{\"uid\":" + str(uid) + ",\"price\":168000,\"curriculums\"" \
                                                          ":[{\"kid\":387362146756864,\"sectioncn\":24,\"spec\":0}]," \
                                                          "\"expiremins\":120,\"scoredays\":0,\"packageid\":387588387936516," \
                                                          "\"manualgive\":null,\"installment\":0,\"name\":\"启蒙菲教\",\"bookprice\":0," \
                                                          "\"makeid\":null,\"invitediscount\":0}"
    else:
        data_json_create_order = "{\"uid\":" + str(
            uid) + ",\"price\":1538000,\"curriculums\":[{\"kid\":173108934578178," \
                   "\"sectioncn\":150,\"spec\":0},{\"kid\":173108934578178," \
                   "\"sectioncn\":5,\"spec\":1}],\"expiremins\":1440," \
                   "\"scoredays\":540,\"packageid\":301285305896970," \
                   "\"manualgive\":null,\"installment\":0," \
                   "\"name\":\"【含教材】15单元特惠套餐（150+5节）\",\"bookprice\":30000," \
                   "\"makeid\":null,\"invitediscount\":0} "
    return data_json_create_order
