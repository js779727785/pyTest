
# def project_to_testcase(project_list):
#     """
#         根据projectID查关联的testid
#         :param id_list:
#         :return:
#         """
#     case_id_list = []
#     id_list = []
#     if project_list and len(project_list) > 0:
#         for project_id in project_list:
#             re = Testcase.objects.filter(belong_project_id=project_id)
#             serializer = TestcaseSerializer(re, many=True)
#             case_list = serializer.data
#             if len(case_list) == 0:
#                 continue
#             for case in case_list:
#                 case_id_list.append(case['testcase_id'])
#         id_list = list(set(case_id_list))
#         return id_list


# def caselevel_to_testcase(oldcase_list, level_list):
#     """
#         根据传入的优先级level_list，过滤case
#         :param id_list:
#         :return:
#         """
#     if oldcase_list and len(oldcase_list) > 0:
#         # 未传入优先级或传入全部时，不过滤直接返回
#         if not level_list or "3" in level_list:
#             return oldcase_list
#         newcase_list = []
#         for old_id in oldcase_list:
#             re = Testcase.objects.filter(testcase_id=old_id)
#             for case in re:
#                 case_level = str(case.level)
#                 # 传入优先级时，过滤case优先级
#                 if case_level in level_list:
#                     newcase_list.append(old_id)
#         id_list = list(set(newcase_list))
#         return id_list