import os,time
from util.common import md5_file,get_file_base_dir,json_response,deal_logic_dict,deal_model_id,dict_data
from BusinessTools.models import ReportFile
from BusinessTools import models
from django.http import FileResponse
# @method_decorator(login_check, name='dispatch')

class Uploads():
    """文件上传"""
    def add_file(self,request):
        report_address = request.POST.get('report_address','')
        username = request.COOKIES.get('username','')
        report_name = request.POST.get('report_name','')
        file_obj = request.FILES.get("file",'')
        result_count = ReportFile.objects.filter(report_name=report_name).count()
        dict_data = {}

        # 检查是否已有报告数据
        if result_count > 0:
            file_info = ReportFile.objects.get(report_name=report_name)
            report_name = file_info.report_name
            file_path = file_info.file_path
            if file_path != '':
                # 先原有删文件后更新数据
                os.remove(file_path)
            # 更新原有数据
            if file_obj =='':
                # 处理无文件上传场景
                dict_data.update(report_address=report_address, owner_name=username, file_name='',
                                 file_path='',
                                 md5='', report_name=report_name)
            else:
                #重新组装文件名
                ts = str(int(time.time()))
                file_name = ts + '_' + file_obj.name
                # 处理有文件更新场景
                # 更新原有数据
                storage = os.path.join(get_file_base_dir(), 'upload/')
                file_path = storage + file_name
                # 将上传文件写到存储路径下
                with open(file_path, "wb") as f:
                    for chunk in file_obj.chunks():
                        f.write(chunk)
                # 将文件内容进行md5，获取文件md5值
                md5 = md5_file(file_path)
                dict_data.update(report_address=report_address, owner_name=username,
                                 file_name=file_name,
                                 file_path=file_path,
                                 md5=md5, report_name=report_name)
            dict_data = deal_logic_dict(dict_data)
            try:
                models.ReportFile.objects.filter(report_name=report_name).update(**dict_data)
            except Exception as e:
                return json_response(report_name, 0, errmsg=e)
            return json_response(report_name, 0, "报告更新成功")
        else:
            #新增数据
            if file_obj == '':
                dict_data.update(report_address=report_address, owner_name=username, file_name='',
                                 file_path='',
                                 md5='', report_name=report_name)
            else:
            #新增文件报告
                ts = str(int(time.time()))
                file_name = ts + '_' + file_obj.name
                # 服务器文件存储路径
                # base_dir = "/Users/jingshuai/Desktop/"
                # file_path = base_dir + file_name
                # 本地测试文件存储路径
                storage = os.path.join(get_file_base_dir(), 'upload/')
                file_path = storage + file_name
                # 将上传文件写到存储路径下
                with open(file_path, "wb") as f:
                    for chunk in file_obj.chunks():
                        f.write(chunk)
                # 将文件内容进行md5，获取文件md5值
                md5 = md5_file(file_path)
                dict_data.update(report_address=report_address, owner_name=username, file_name=file_name,
                                 file_path=file_path,
                                 md5=md5, report_name=report_name)
            dict_data = deal_logic_dict(dict_data)
            # 在数据库创建一条记录
            dict_data = deal_model_id(dict_data, 'file_id')  # 获取文件id
            report_name = dict_data.get('report_name')
            try:
                models.ReportFile.objects.create(**dict_data)
            except Exception as e:
                return json_response(report_name, 0, errmsg=e)
            return json_response(report_name, 0, "报告上传成功")

    # 下载文件
    def download_file(self,request):
        report_name = request.get('report_name')
        try:
            file_info = ReportFile.objects.get(report_name=report_name)
            print('下载的文件名：' + file_info.file_name)
            file = open(file_info.file_path, 'rb')
            response = FileResponse(file)
            response['Content-Type'] = 'application/octet-stream'
            response['Content-Disposition'] = 'attachment;filename="%s"' % (file_info.file_name)
            return json_response(report_name, 0, "文件下载成功")
        except Exception as e:
            print(e)
            return json_response(report_name, 0, "该文件不存在，重新输入file_id")

    # 文件列表
    def list_file(self):
        file_infos = list(ReportFile.objects.all().values('report_name'))
        return dict_data(ret=1, data=file_infos, msg='查看文件成功')

    # 删除文件
    def delete_file(self, request):
        report_name = request.get('report_name')
        try:
            file_info = ReportFile.objects.get(report_name=report_name)
            file_path =file_info.file_path
            #先删文件后删库表数据
            os.remove(file_path)
            file_info.delete()
            return json_response(report_name, 0, "文件删除成功")
        except Exception as e:
            print(e)
            return json_response(report_name, 0, "该文件不存在，重新输入report_name")