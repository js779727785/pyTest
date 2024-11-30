
import math
import time

def schedule_task_calculate_task_priority(user_to_task_data_map):
    total_task_num = sum(task_data["TaskNum"] for task_data in user_to_task_data_map.values())
    for userId, task_data in user_to_task_data_map.items():
        # 1.饥饿避免(任务等待时间权重)
        waiting_time_factor = get_waiting_time_factor(task_data["FirstTaskTime"])
        # 2.队列长度影响
        user_queue_length_factor = get_user_queue_length_factor(task_data["TaskNum"])
        # 3.用户任务数量占比
        user_task_ratio_factor = get_user_task_ratio_factor(task_data["TaskNum"], total_task_num)
        # 混合策略
        task_data["FinalScore"] = (waiting_time_factor * 0.20) + (user_queue_length_factor * 0.10) + (
                user_task_ratio_factor * 0.10)
        user_to_task_data_map[userId] = task_data
    return user_to_task_data_map

def get_waiting_time_factor(timestamp):
    wait_time = time.time() - timestamp
    return min(wait_time / 3600.0, 1.0)  # 最多等待1小时达到最大因子


def get_user_queue_length_factor(task_num):
    return min(task_num / 50.0, 1.0)  # 因子计算上限为50个任务


def get_user_task_ratio_factor(task_num, total_task_num):
    ratio = task_num / total_task_num
    return max(0.3, 1.0 - ratio)  # 用户任务占比越高，优先级因子越低，但不低于0.3


def test(time,data,queue=50.0,ratio=0.3):

    a_wait_time = time.get('a', 0) * 60
    b_wait_time = time.get('b', 0) * 60
    c_wait_time = time.get('c', 0) * 60
    a_time = min(a_wait_time / 3600.0, 1.0)
    b_time = min(b_wait_time / 3600.0, 1.0)
    c_time = min(c_wait_time / 3600.0, 1.0)


    total_task_num = data.get('a', 0) + data.get('b', 0) + data.get('c', 0)
    a_task_num = data.get('a', 0)
    b_task_num = data.get('b', 0)
    c_task_num = data.get('c', 0)

    a_queue=min(a_task_num / queue, 1.0)
    b_queue=min(b_task_num / queue, 1.0)
    c_queue=min(c_task_num / queue, 1.0)

    a_ratio = a_task_num / total_task_num
    b_ratio = b_task_num / total_task_num
    c_ratio = c_task_num / total_task_num

    a_task = max(ratio, 1.0 - a_ratio)
    b_task = max(ratio, 1.0 - b_ratio)
    c_task = max(ratio, 1.0 - c_ratio)

    a=a_time * 0.20 + a_queue * 0.10 + a_task * 0.10
    b=b_time * 0.20 + b_queue * 0.10 + b_task * 0.10
    c=c_time * 0.20 + c_queue * 0.10 + c_task * 0.10
    return {'a':a,'b':b,'c':c}

"""
模拟队列已打满，开始排队,abc分别有data个在排队，等待时间分别为time分钟
"""
if __name__ == '__main__':

    data={'a':5,'b':2,'c':1}
    time={'a':15,'b':3,'c':1}
    res=test(time,data)
    # 按值从大到小排序
    sorted_data = dict(sorted(res.items(), key=lambda item: item[1], reverse=True))

    print(sorted_data)

