import requests

url = "http://zucheucordertest.zuche.com/wapi/order/applet/list"

payload="{\"pageNo\":1,\"pageSize\":10,\"orderNo\":\"\",\"orderStatus\":\"\",\"orderType\":\"\",\"signStatus\":\"\",\"checkType\":\"\",\"payStatus\":\"\",\"source\":\"6\",\"customMobile\":\"\",\"customName\":\"\",\"customType\":\"\",\"createEmpName\":\"\",\"startCreateTime\":\"\",\"endCreateTime\":\"\",\"vehicleVin\":\"\",\"orderStatusList\":[],\"earnestSettleStatus\":\"\",\"vehicleSettleStatus\":\"\",\"canBeDelivered\":\"\",\"licensePlateNumber\":\"\",\"ifBigCustomer\":\"\",\"pickCityId\":\"\",\"pickInfoPickCityId\":\"\",\"hasContract\":\"\"}"
headers = {
  'Accept': 'application/json, text/plain, */*',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
  'Content-Type': 'application/json;charset=UTF-8',
  'Cookie': 'intranet-test-sessionid=33693AC8487364190F724B09045B2D2C; intranet-test-sessionid=6FB01C8AF8503542FE98D60D695A683E'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)