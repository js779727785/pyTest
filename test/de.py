# 读取日志文件中 排名前3的api
# [2024-1-2 12:34:43] xxxfile /api/create/order POST
# [2024-1-2 12:34:43] xxxfile /api/create/user POST
# [2024-1-2 12:34:43] xxxfile /inner/select/order POST
# .....
#
# app.log


# def get_top_three_apis(log_file_path):
#     api_counts = {}
#     with open(log_file_path, 'r') as file:
#         for line in file.readlines():
#             parts = line.split()
#             if len(parts) > 2:
#                 api = parts[2]
#                 if api in api_counts:
#                     api_counts[api] += 1
#                 else:
#                     api_counts[api] = 1
#     sorted_apis = sorted(api_counts.items(), key=lambda x: x[1], reverse=True)
#     return [api for api, _ in sorted_apis[:3]]
#
# log_file_path = "app.log"  # 请替换为实际的日志文件路径
# print(get_top_three_apis(log_file_path))

# lis=[3,2,5,1,4,6,7,8,9]
