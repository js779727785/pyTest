import requests,time

"""增加积分"""
# token="568805c070673676b076c9828b59c6db8be10aa3bf4183e6e668bbd9b252e9af"
# # url = "http://47.237.102.241:8080/wallet-api/points/add"
# url="https://api-pre.skyreels.ai/wallet-api/points/add"
# current_time = time.time()
# one_year_in_seconds = 365 * 24 * 60 * 60
# expire = int(current_time + one_year_in_seconds)
# print(expire)
# re=requests.post(url, headers={"Login-Token": token, "Content-Type": "application/json"}, json={
#     "points": 100,
#     "expire": expire,
#     "type": 0,
#     "comment": "注册赠送"
# })
# print(re.text)



"""
分镜视频结果失败统计fetch_and_count_failures
"""
import requests,json

def count_failures(data_list):
    failed_count = 0
    results = []
    for item in data_list:
        if item['status'] == 'failed':
            failed_count += 1
            taskid = item['taskid']
            algorithm_taskid = item['algorithm_taskid']
            response_dict = json.loads(item['response'])
            code = response_dict.get('code')
            msg = response_dict.get('msg')
            parts = msg.split("task_status_msg': '")
            if len(parts) > 1:
                task_status_msg = parts[1].split("',")[0]
            else:
                task_status_msg = None
            results.append((taskid, algorithm_taskid, code,task_status_msg))
    return failed_count, results

def fetch_and_count_failures(uuid):
    # url = f'https://api-pre.skyreels.ai/agent_api/story/getTaskLog?uuid={uuid}'
    url = f'http://47.237.102.241:8080/agent_api/story/getTaskLog?uuid={uuid}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data_list = data['data']['list']
        return count_failures(data_list)
    else:
        return 0, []

def main(uuid):
    failed_count, details = fetch_and_count_failures(uuid)
    print(f"Failed total count: {failed_count}")
    print("Details:")
    for taskid, algorithm_taskid, code, task_status_msg in details:
        print(f"TaskID: {taskid}, AlgorithmTaskID: {algorithm_taskid}, Response code: {code}, Task_status_msg: {task_status_msg}")

# uuid = '1845403224914059264'
uuid = '1860997306632630272'
main(uuid)