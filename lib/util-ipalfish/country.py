class Country(object):
    country_abb = {"CN": "中国,China", "US": "美国,USA", "GB": "英国,England", "CA": "加拿大,Canada", "PH": "菲律宾,Philippines",
                   "AU": "澳大利亚,Australia", "NZ": "新西兰,New Zealand", "RU": "俄罗斯,Russia", "CM": "喀麦隆,Cameroon",
                   "AO": "安哥拉,Angola", "AF": "阿富汗,Afghanistan", "AL": "阿尔巴尼亚,Albania", "DZ": "阿尔及利亚,Algeria",
                   "AD": "安道尔共和国,Andorra", "AI": "安圭拉岛,Anguilla", "AG": "安提瓜和巴布达,Antigua and Barbuda",
                   "AR": "阿根廷,Argentina", "AM": "亚美尼亚,Armenia", "AT": "奥地利,Austria", "AZ": "阿塞拜疆,Azerbaijan",
                   "BS": "巴哈马,Bahamas", "BH": "巴林,Bahrain", "BD": "孟加拉国,Bangladesh", "BB": "巴巴多斯,Barbados",
                   "BY": "白俄罗斯,Belarus", "BE": "比利时,Belgium", "BZ": "伯利兹,Belize", "BJ": "贝宁,Benin",
                   "BM": "百慕大群岛,Bermuda Is.", "BO": "玻利维亚,Bolivia", "BA": "波斯尼亚和黑塞哥维那,Bosnia And Herzegovina",
                   "BW": "博茨瓦纳,Botswana", "BR": "巴西,Brazil", "BN": "文莱,Brunei", "BG": "保加利亚,Bulgaria",
                   "BF": "布基纳法索,Burkina-faso", "MM": "缅甸,Burma", "BI": "布隆迪,Burundi",
                   "CF": "中非共和国,Central African Republic", "TD": "乍得,Chad", "CL": "智利,Chile", "CO": "哥伦比亚,Colombia",
                   "CG": "刚果,Congo", "CK": "库克群岛,Cook Is.", "CR": "哥斯达黎加,Costa Rica",
                   "HR": "克罗地亚,Croatia", "CU": "古巴,Cuba", "CY": "塞浦路斯,Cyprus", "CZ": "捷克,Czech Republic",
                   "DK": "丹麦,Denmark",
                   "DJ": "吉布提,Djibouti", "DO": "多米尼加共和国,Dominica Rep.", "EC": "厄瓜多尔,Ecuador", "EG": "埃及,Egypt",
                   "SV": "萨尔瓦多,EI Salvador", "EE": "爱沙尼亚,Estonia", "ET": "埃塞俄比亚,Ethiopia", "FJ": "斐济,Fiji",
                   "FI": "芬兰,Finland", "FR": "法国,France", "GF": "法属圭亚那,French Guiana", "GA": "加蓬,Gabon",
                   "GM": "冈比亚,Gambia", "GE": "格鲁吉亚,Georgia", "DE": "德国,Germany", "GH": "加纳,Ghana",
                   "GI": "直布罗陀,Gibraltar", "GR": "希腊,Greece", "GD": "格林纳达,Grenada", "GU": "关岛,Guam",
                   "GT": "危地马拉,Guatemala", "GN": "几内亚,Guinea", "GY": "圭亚那,Guyana", "HT": "海地,Haiti",
                   "HN": "洪都拉斯,Honduras", "HK": "香港,Hongkong", "HU": "匈牙利,Hungary", "IS": "冰岛,Iceland",
                   "IN": "印度,India", "ID": "印度尼西亚,Indonesia", "IR": "伊朗,Iran", "IQ": "伊拉克,Iraq", "IE": "爱尔兰,Ireland",
                   "IL": "以色列,Israel", "IT": "意大利,Italy", "JM": "牙买加,Jamaica", "JP": "日本,Japan", "JO": "约旦,Jordan",
                   "KH": "柬埔寨,Kampuchea (Cambodia)", "KZ": "哈萨克斯坦,Kazakstan", "KE": "肯尼亚,Kenya", "KR": "韩国,Korea",
                   "KW": "科威特,Kuwait", "KG": "吉尔吉斯坦,Kyrgyzstan", "LA": "老挝,Laos", "LV": "拉脱维亚,Latvia",
                   "LB": "黎巴嫩,Lebanon", "LS": "莱索托,Lesotho", "LR": "利比里亚,Liberia", "LY": "利比亚,Libya",
                   "LI": "列支敦士登,Liechtenstein", "LT": "立陶宛,Lithuania", "LU": "卢森堡,Luxembourg", "MO": "澳门,Macao",
                   "MG": "马达加斯加,Madagascar", "MW": "马拉维,Malawi", "MY": "马来西亚,Malaysia", "MV": "马尔代夫,Maldives",
                   "ML": "马里,Mali", "MT": "马耳他,Malta", "MU": "毛里求斯,Mauritius", "MX": "墨西哥,Mexico",
                   "MD": "摩尔多瓦,Moldova Republic of", "MC": "摩纳哥,Monaco", "MN": "蒙古,Mongolia",
                   "MS": "蒙特塞拉特岛,Montserrat Is", "MA": "摩洛哥,Morocco", "MZ": "莫桑比克,Mozambique", "NA": "纳米比亚,Namibia",
                   "NR": "瑙鲁,Nauru", "NP": "尼泊尔,Nepal", "NL": "荷兰,Netherlands", "NI": "尼加拉瓜,Nicaragua",
                   "NE": "尼日尔,Niger", "NG": "尼日利亚,Nigeria", "KP": "朝鲜,North Korea", "NO": "挪威,Norway", "OM": "阿曼,Oman",
                   "PK": "巴基斯坦,Pakistan", "PA": "巴拿马,Panama", "PG": "巴布亚新几内亚,Papua New Cuinea", "PY": "巴拉圭,Paraguay",
                   "PE": "秘鲁,Peru", "PL": "波兰,Poland", "PF": "法属玻利尼西亚,French Polynesia", "PT": "葡萄牙,Portugal",
                   "PR": "波多黎各,Puerto Rico", "QA": "卡塔尔,Qatar", "RO": "罗马尼亚,Romania", "RW": "卢旺达,Rwanda",
                   "LC": "圣卢西亚,Saint Lueia", "VC": "圣文森特,Saint Vincent", "SM": "圣马力诺,San Marino",
                   "ST": "圣多美和普林西比,Sao Tome and Principe", "SA": "沙特阿拉伯,Saudi Arabia", "RS": "塞尔维亚,Serbia",
                   "SN": "塞内加尔,Senegal", "SC": "塞舌尔,Seychelles", "SL": "塞拉利昂,Sierra Leone",
                   "SG": "新加坡,Singapore", "SK": "斯洛伐克,Slovakia", "SI": "斯洛文尼亚,Slovenia", "SB": "所罗门群岛,Solomon Is",
                   "SO": '索马里,Somali', "ZA": "南非,South Africa",
                   "ES": "西班牙,Spain", "LK": "斯里兰卡,Sri Lanka", "SD": "苏丹,Sudan", "SR": "苏里南,Suriname",
                   "SZ": "斯威士兰,Swaziland",
                   "SE": "瑞典,Sweden", "CH": "瑞士,Switzerland", "SY": "叙利亚,Syria", "TW": "台湾省,Taiwan",
                   "TJ": "塔吉克斯坦,Tajikstan",
                   "TZ": "坦桑尼亚,Tanzania", "TH": "泰国,Thailand", "TG": "多哥,Togo", "TO": "汤加,Tonga",
                   "TT": "特立尼达和多巴哥,Trinidad and Tobago", "TN": "突尼斯,Tunisia", "TR": "土耳其,Turkey",
                   "TM": "土库曼斯坦,Turkmenistan",
                   "UG": "乌干达,Uganda", "UA": "乌克兰,Ukraine", "AE": "阿拉伯联合酋长国,United Arab Emirates", "UY": "乌拉圭,Uruguay",
                   "UZ": "乌兹别克斯坦,Uzbekistan", "VE": "委内瑞拉,Venezuela", "VN": "越南,Vietnam", "YE": "也门,Yemen",
                   "YU": "南斯拉夫,Yugoslavia",
                   "ZW": "津巴布韦, Zimbabwe", "ZR": "扎伊尔, Zaire", "ZM": "赞比亚, Zambia"
                   }
    country_dict = {"中国": 86, "韩国": 82, "日本": 81, "美国": 1, "加拿大": 10001, "英国": 44,
                    "新加坡": 65, "马来西亚": 60,
                    "泰国": 66, "越南": 84, "菲律宾": 63, "印度尼西亚": 62, "意大利": 39, "俄罗斯": 7, "新西兰": 64, "荷兰": 31, "瑞典": 46,
                    "澳大利亚": 61, "乌克兰": 380,
                    "法国": 33, "德国": 49, "阿富汗": 93, "阿尔巴尼亚": 355, "阿尔及利亚": 213, "东萨摩亚(美)": 1684, "安道尔": 376,
                    "安哥拉": 244,
                    "安圭拉岛(英)": 1264,
                    "安提瓜和巴布达": 1268, "阿根廷": 54, "亚美尼亚": 374, "阿鲁巴岛": 297, "奥地利": 43, "阿塞拜疆": 994, "巴林": 973,
                    "孟加拉国": 880, "巴巴多斯": 1246,
                    "白俄罗斯": 375, "比利时": 32, "伯利兹": 501, "贝宁": 229, "百慕大群岛(英)": 1441, "不丹": 975, "玻利维亚": 591,
                    "波斯尼亚和黑塞哥维那": 387,
                    "博茨瓦纳": 267, "巴西": 55, "保加利亚": 359, "布基纳法索": 226, "布隆迪": 257, "喀麦隆": 237, "佛得角": 238,
                    "开曼群岛(英)": 1345, "中非": 236,
                    "乍得": 235, "智利": 56, "圣诞岛": 100061, "科科斯岛": 200061, "哥伦比亚": 57, "科摩罗": 269, "刚果": 242,
                    "科克群岛(新)": 682,
                    "哥斯达黎加": 506,
                    "克罗地亚": 385, "古巴": 53, "塞浦路斯": 357, "捷克": 420, "丹麦": 45, "吉布提": 253, "多米尼克国": 1767,
                    "多米尼加共和国": 1809,
                    "厄瓜多尔": 593,
                    "埃及": 20, "萨尔瓦多": 503, "赤道几内亚": 240, "厄立特里亚": 291, "爱沙尼亚": 372, "埃塞俄比亚": 251, "福克兰群岛": 500,
                    "法罗群岛(丹)": 298, "斐济": 679,
                    "芬兰": 358, "法属波里尼西亚": 689, "加蓬": 241, "冈比亚": 220, "格鲁吉亚": 995, "加纳": 233, "直布罗陀(英)": 350,
                    "希腊": 30,
                    "格陵兰岛": 299,
                    "格林纳达": 1473, "瓜德罗普岛(法)": 590, "关岛(美)": 1671, "危地马拉": 502, "几内亚": 224, "几内亚比绍": 245, "圭亚那": 592,
                    "海地": 509,
                    "洪都拉斯": 504, "匈牙利": 36, "冰岛": 354, "印度": 91, "伊郎": 98, "伊拉克": 964, "爱尔兰": 353, "以色列": 972,
                    "科特迪瓦": 225, "牙买加": 1876,
                    "约旦": 962, "柬埔塞": 855, "哈萨克斯坦": 10007, "肯尼亚": 254, "基里巴斯": 686, "科威特": 965, "吉尔吉斯斯坦": 996,
                    "老挝": 856,
                    "拉脱维亚": 371,
                    "黎巴嫩": 961, "莱索托": 266, "利比里亚": 231, "利比亚": 218, "列支敦士登": 423, "立陶宛": 370, "卢森堡": 352,
                    "马其顿": 389,
                    "马达加斯加": 261,
                    "马拉维": 265, "马尔代夫": 960, "马里": 223, "马耳他": 356, "马绍尔群岛": 692, "马提尼克(法)": 596, "毛里塔尼亚": 222,
                    "毛里求斯": 230, "马约特岛": 1000262,
                    "墨西哥": 52, "密克罗尼西亚(美)": 691, "摩纳哥": 377, "蒙古": 976, "蒙特塞拉特岛(英)": 1664, "摩洛哥": 212, "莫桑比克": 258,
                    "缅甸": 95, "纳米比亚": 264,
                    "瑙鲁": 674, "尼泊尔": 977, "荷属安的列斯群岛": 599, "新喀里多尼亚群岛(法)": 687, "尼加拉瓜": 505, "尼日尔": 227,
                    "尼日利亚": 234,
                    "纽埃岛(新)": 683,
                    "诺福克岛(澳)": 672, "朝鲜": 850, "马里亚纳群岛": 1670, "挪威": 47, "阿曼": 968, "巴基斯坦": 92, "帕劳(美)": 680,
                    "巴拿马": 507, "巴布亚新几内亚": 675,
                    "巴拉圭": 595, "秘鲁": 51, "波兰": 48, "葡萄牙": 351, "卡塔尔": 974, "摩尔多瓦": 373, "留尼汪岛": 262,
                    "罗马尼亚": 40, "卢旺达": 250,
                    "阿森松(英)": 247, "圣赫勒拿": 290, "圣克里斯托弗和尼维斯": 1869, "圣卢西亚": 1758, "圣皮埃尔岛及密克隆岛": 508,
                    "圣文森特岛(英)": 1784,
                    "西萨摩亚": 685,
                    "圣马力诺": 378, "圣多美和普林西比": 239, "沙特阿拉伯": 966, "塞内加尔": 221, "塞舌尔": 248, "塞拉利昂": 232, "斯洛伐克": 421,
                    "斯洛文尼亚": 386,
                    "所罗门群岛": 677, "索马里": 252, "南非": 27, "西班牙": 34, "斯里兰卡": 94, "苏丹": 249, "苏里南": 597, "斯威士兰": 268,
                    "瑞士": 41, "叙利亚": 963,
                    "塔吉克斯坦": 992, "巴哈马国": 1242, "梵蒂冈": 14397, "多哥": 228, "汤加": 676, "特立尼达和多巴哥": 1868, "突尼斯": 216,
                    "土耳其": 90, "土库曼斯坦": 993,
                    "特克斯和凯科斯群岛(英)": 1649, "图瓦卢": 688, "乌干达": 256, "英国": 44, "坦桑尼亚": 255, "乌拉圭": 598, "乌兹别克斯坦": 998,
                    "瓦努阿图": 678,
                    "委内瑞拉": 58, "维尔京群岛(英)": 1340, "也门": 967, "南斯拉夫": 381, "赞比亚": 260, "桑给巴尔": 259, "津巴布韦": 263}

    def get_country_name(self, enum):
        """
        获取国家名称
        :param enum:
        :return:
        """
        country_name = self.country_abb.get(enum)
        if country_name == '' or country_name == None:
            return '老师国籍不存在 ' + str(enum)
        return country_name

    def get_name_list(self):
        """
        获取国家名称列表
        :return:
        """
        name_list = self.country_dict.keys()
        return list(name_list)

    def get_country_code(self, name):
        """
        获取国家区号
        :return:
        """
        code = self.country_dict.get(name)
        if code:
            return code
        else:
            raise Exception('国家不存在')

    def get_abb_by_code(self, code):
        """
        根据国家区号获取国家简称
        :return:
        """

        for k, v in self.country_dict.items():
            if int(code) == v:
                for abb_k, abb_v in self.country_abb.items():
                    if abb_v.find(k) > -1:
                        return abb_k
                else:
                    return ''


if __name__ == '__main__':
    k = Country().get_abb_by_code(44)
    print(k)
