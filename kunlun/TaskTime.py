import requests,json


def get_taskdata(work_id):
    url = f'https://api-pre.skyreels.ai/agent_api/story/getTaskLog?uuid={work_id}'
    # url = f'http://47.237.102.241:8080/agent_api/story/getTaskLog?uuid={work_id}'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        data_list = data['data']['list']
        return  data_list
    else:
        print(f"Error: {response.status_code}")
        return []

def TaskTime(work_id):
    act_to_data = {}
    for item in get_taskdata(work_id):
        act = item["act"]
        if act not in act_to_data:
            act_to_data[act] = []
        act_to_data[act].append(item)

    for act, items in act_to_data.items():
        print(f"Act: {act}")
        total = len(items)

        for index, item in enumerate(items):
            task_id = item.get("task_id")
            if index > 0:
                prev_created = items[index - 1]["created"]
                time_diff = item["created"] - prev_created
                print(f"Task ID: {task_id}, Time Difference (in seconds): {time_diff}")
            else:
                print(f"Task ID: {task_id}, Time Difference (in seconds): N/A")
        print(f"Total for this act: {total}\n")
work_id = '1847126670456569856'
# TaskTime(work_id)


import datetime

timestamp = 1729502659
date_time = datetime.datetime.fromtimestamp(timestamp)
print(date_time)

import time
from datetime import datetime

# 假设给定的时间为 2024-12-17 20:00:00
date_time_str = "2024-10-21 13:50:00"
date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d %H:%M:%S')

# 将 datetime 对象转换为时间戳
timestamp = time.mktime(date_time_obj.timetuple())
# print(timestamp)