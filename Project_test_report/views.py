#!/user/bin/env python3
# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from framework.logger import Logger
from config.config import *
from framework.API import API
from framework.Fanchart import *
from framework.Add_call import Add_call
import time
from django.shortcuts import HttpResponse, render, redirect
logger = Logger(logger="views").getlog()
import configparser,os

proDir = os.getcwd()
configPath = os.path.join(proDir, "config\config.ini")
cf = configparser.ConfigParser()
cf.read(configPath,encoding="utf-8-sig")

head_host=head_server()['host']
head_port=head_server()['port']
head_addr='http://%s:%s/'%(head_host,head_port)
def index(request):#request是必须带的实例。类似class下方法必须带self一样

    # now = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    # random_str = Add_call().random_str(30)
    #"htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),


    data = API().APIall('get_All_projects', {})
    projects_list=data["Repair_rate_sorted"]
    projects_list.reverse()#列表反向输出

    logger.info(data)
    ########################################生成扇形统计图
    dic_All_product={
            "key":data['product_name'],
              "values":data['product_sum'],
                'titlename':"项目BUG数占比",
            "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(dic_All_product)

    #########################################生成扇形统计图
    ##############################################生成条形 修复率统计图
    dic_All_product_vertical={
            "key":data['Repair_rate_dic_sorted']['product_name_r'],
              "values":data['Repair_rate_dic_sorted']['Repair_rate_r'],
                'titlename':"BUG修复率",
                'legend': '',  # 图例名d
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Bar_chart_vertical(dic_All_product_vertical) # 条形图竖
    ############################################## 修复率统计图


    entry_name_lies=zentao_list()['pro_list']
    return render(request, "index.html", {
                                        "projects_list": projects_list,
                                          "head": '',
                                          'entry_name_lies':entry_name_lies,
                                          "path_url": 'product',
                                            'All_product_Fanchart':dic_All_product['htmlname'],
                                        'All_product_vertical':dic_All_product_vertical['htmlname']
                                          }
                  )


def project_summary(request):#
    product = request.GET.get('product')
    name = request.GET.get('name')
    path_url="module"
    dic = {
        'product': product,
        'module':''
    }

    data_product_sum=API().APIall('get_product_sum', dic)
    name = data_product_sum['data']['name']

    logger.info('入参：%s,%s'%(product,name))
    data = API().APIall('module_info', dic)

    module_bug_list=data['Repair_datalists_sorted']
    module_bug_list.reverse()#列表倒序输出



    entry_name_lies = zentao_list()['module_list']


    ########################################################生成修复率条形图排行
    dic_All_product_vertical={
            "key":data['Repair_rate_dic_sorted']['product_name_r'],
              "values":data['Repair_rate_dic_sorted']['Repair_rate_r'],
                'titlename':"BUG修复率",
                'legend': '',  # 图例名
            "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Bar_chart_vertical(dic_All_product_vertical) # 条形图竖



    ########################################################生成修复率条形图排行

    ############################################################获取严重级别以上BUG列表


    def Impo_level(severity):
        module_lsit = API().APIall('get_module', dic)["data"]
        Importance_level_data_list = []
        if severity != '':
            for i in module_lsit["modulelist"]:
                dic_Importance_level = {
                    "product": product,
                    "module": i,
                    'severity': severity  # 'severity<=2',
                }
                Importance_level_data = API().APIall('Importance_level', dic_Importance_level)["data"]

                if len(Importance_level_data["data"]) != 0:
                    Importance_level_data_list.append(Importance_level_data)
            return Importance_level_data_list




    ###########################################################获取严重级别以上BUG列表

    ##############################################简介语

    data_product_module_sum = API().APIall('get_product_module_sum', dic)["data"]
    if data_product_module_sum['bug_total']!=0:
        if data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] > 0:
            synopsis = product_lusion(data_product_module_sum)['brief_4']
            severity = '<=2'
            Importance_level_data_list = Impo_level(severity)
            need_settle = product_Next_step(data_product_module_sum)['brief_4']
        elif data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] == 0 and \
                data_product_module_sum['severity_3'] > 0:
            synopsis = product_lusion(data_product_module_sum)['brief_3']
            severity = '=3'
            Importance_level_data_list = Impo_level(severity)
            need_settle = product_Next_step(data_product_module_sum)['brief_3']

        elif data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] == 0 and \
                data_product_module_sum[
                    'severity_3'] == 0 and data_product_module_sum['severity_4'] > 0:
            synopsis = product_lusion(data_product_module_sum)['brief_2']
            severity = '=4'
            need_settle = product_Next_step(data_product_module_sum)['brief_2']

            Importance_level_data_list = Impo_level(severity)
        elif data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] == 0 and \
                data_product_module_sum[
                    'severity_3'] == 0 and data_product_module_sum['severity_4'] == 0:
            synopsis = product_lusion(data_product_module_sum)['brief_1']
            severity = ''
            need_settle = product_Next_step(data_product_module_sum)['brief_1']


        else:
            need_settle = product_Next_step(data_product_module_sum)['brief_1']
    else:
        synopsis=product_lusion(data_product_module_sum)['brief_-1']
        Importance_level_data_list = []
        need_settle = product_Next_step(data_product_module_sum)['brief_-1']
    ##############################################简介语





    #######################################进度图
    dic_progress_chart={
        "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
        'titlename':'BUG修复率',
        'share':float(round(data_product_sum['data']['data']['closed']/data_product_sum['data']['sum_all']  if data_product_sum['data']['sum_all']!=0 else 0.0,4)),

    }

    progress_chart(dic_progress_chart)

    #######################################进度图


    ###############################生成BUG处理状态扇形图
    key_list=list(config_bug()['status'].values())
    value_list = list(data_product_sum['data']['data'].values())
    dic_sxt={
            "key":key_list,
              "values":value_list,
                'titlename':"BUG处理占比",
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(dic_sxt)
    ##################################生成BUG处理状态扇形图

    ###############################生成模块BUG数占比扇形图
    key_list=data['Modulename_list']
    value_list =data['msdule_num']
    modular_sxt={
            "key":key_list,
              "values":value_list,
                'titlename':"模块BUG数占比",
            "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(modular_sxt)
    ###################################生成模块BUG数占比扇形图
    ###############################################################生成BUG日增量条形图
    data_time = API().APIall('Check_new_BUG', dic)
    import datetime
    End_Time = str(data_time['End_Time'])
    dt = datetime.datetime.strptime(End_Time, "%Y-%m-%d")
    StartTime_7_day = (dt - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

    dic_txt_BUG_rz={
        "product": product,
        "module": "",
        "StartTime": StartTime_7_day,
        "End_Time": End_Time
    }
    txt_BUG_rz_data=API().APIall('grow_days', dic_txt_BUG_rz)
    dic_txt_BUG_rz_data={
            "key":txt_BUG_rz_data['days_list'],
            "values":txt_BUG_rz_data["number_zs_list"],
            'titlename':"最近七日增量（BUG数）",
            'legend':name,# 图例名
            "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),

    }

    Bar_chart(dic_txt_BUG_rz_data)

    ################################################################生成BUG日增量条形图

    ##################################################生成所有BUG周期的折线图

    # key = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期七', '星期日']
    # values = [100, 200, 300, 400, 100, 400, 300]
    # values2 = [200, 300, 200, 100, 200, 300, 400]
    dic_txt_BUG_all_time={
        "product": product,
        "module": "",
        "StartTime":  str(data_time["StartTime"]),
        "End_Time": End_Time
    }
    txt_BUG_rz_data_all = API().APIall('grow_days', dic_txt_BUG_all_time)
    dic_all_bug_data = {
        "key": txt_BUG_rz_data_all['days_list'],
        "values": txt_BUG_rz_data_all["number_zs_list"],
        'series_name': name,  # 图例名
        'titlename': "全周期BUG日增量",
         "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }

    Line_chart(dic_all_bug_data)
    ##################################################生成所有BUG周期的折线图

    #####################################################BUG严重程度扇形图

    severity_data_all = API().APIall('get_severity', {"product": product,"module": ""})['data']
    severity_all_dic={
            "key":severity_data_all['severity_all']['severity_name_all'],
              "values":severity_data_all['severity_all']['severity_sums_all'],
                'titlename':"所有BUG级别占比",
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(severity_all_dic)

    severity_NOclosed_dic={
            "key":severity_data_all['severity_NOclosed']['severity_name_NOclosed'],
              "values":severity_data_all['severity_NOclosed']['severity_sums_NOclosed'],
                'titlename':"未关闭BUG等级",
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(severity_NOclosed_dic)
    severity_NOclosed_1_2_sum=sum(severity_NOclosed_dic['values'][:2])#严重BUG数
    #####################################################严重程度扇形图




    return render(
        request, "project_summary.html",
                  {
                   'synopsis':synopsis,
                   'head_addr':head_addr,
                   "module_list": module_bug_list,
                   'data_product_sum':data_product_sum['data'],
                   "head": name,
                   'entry_name_lies': entry_name_lies,
                   "path_url": path_url,
                   'htmlname':dic_sxt['htmlname'],
                   'modular_sxt':modular_sxt['htmlname'],
                   'dic_txt_BUG_rz_data':dic_txt_BUG_rz_data['htmlname'],
                   'dic_all_bug_data':dic_all_bug_data['htmlname'],
                    "Importance_level_data_list":Importance_level_data_list,
                      'need_settle':need_settle,
                    'entry_name_lies_BUGlist':zentao_list()['bug_list'],
                      'zentao_zm': zentaos_zm()['zentao'],
                      'severity_NOclosed_html':severity_NOclosed_dic['htmlname'],
                      'severity_all_html': severity_all_dic['htmlname'],
                      'severity_NOclosed_1_2_sum':severity_NOclosed_1_2_sum,
                      'progress_chart_html':dic_progress_chart['htmlname'],
                      'All_product_vertical': dic_All_product_vertical['htmlname']

                  }
                  )
def module(request):
    module = request.GET.get('module')




    dic = {
        'module': module,

    }

    data = API().APIall('get_module_bug', dic)

    entry_name_lies = zentao_list()['bug_list']


    dic_module={
        'module':module,
        "product":''
    }
    module_sum = API().APIall('get_product_sum', dic_module)
    Modulename = module_sum['data']['name']




    ############################################################获取严重级别以上BUG列表


    def Impo_level(severity):
        dic_module.update({'severity': severity})
        Importance_level_data = API().APIall('Importance_level', dic_module)["data"]


        return Importance_level_data

    ###########################################################获取严重级别以上BUG列表

    ##############################################简介语

    data_product_module_sum = API().APIall('get_product_module_sum', dic)["data"]
    product=data_product_module_sum['product']
    if data_product_module_sum['bug_total']!=0:
        if data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] > 0:
            synopsis = module_lusion(data_product_module_sum)['brief_4']
            severity = '<=2'
            Importance_level_data_list = Impo_level(severity)
            need_settle = module_Next_step(data_product_module_sum)['brief_4']
        elif data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] == 0 and \
                data_product_module_sum['severity_3'] > 0:
            synopsis = module_lusion(data_product_module_sum)['brief_3']
            severity = '=3'
            Importance_level_data_list = Impo_level(severity)
            need_settle = module_Next_step(data_product_module_sum)['brief_3']
        elif data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] == 0 and \
                data_product_module_sum[
                    'severity_3'] == 0 and data_product_module_sum['severity_4'] > 0:
            synopsis = module_lusion(data_product_module_sum)['brief_2']
            severity = '=4'
            Importance_level_data_list = Impo_level(severity)
            need_settle = module_Next_step(data_product_module_sum)['brief_2']

        elif data_product_module_sum['severity_1'] + data_product_module_sum['severity_2'] == 0 and \
                data_product_module_sum[
                    'severity_3'] == 0 and data_product_module_sum['severity_4'] == 0:
            synopsis = module_lusion(data_product_module_sum)['brief_1']
            severity = ''
            need_settle = module_Next_step(data_product_module_sum)['brief_1']

        else:
            need_settle = module_Next_step(data_product_module_sum)['brief_1']
    else:
        synopsis=module_lusion(data_product_module_sum)['brief_-1']
        Importance_level_data_list = []
        need_settle = module_Next_step(data_product_module_sum)['brief_-1']

    ##############################################简介语

    #######################################进度图
    dic_progress_chart={
         "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
        'titlename':'BUG修复率',
        'share':float(round(module_sum['data']['data']['closed']/module_sum['data']['sum_all'],4))  if module_sum['data']['sum_all']!=0 else 0.0,

    }

    progress_chart(dic_progress_chart)

    #######################################进度图






    ###############################生成BUG处理状态扇形图
    key_list=list(config_bug()['status'].values())
    value_list = list(module_sum['data']['data'].values())
    dic_sxt={
            "key":key_list,
              "values":value_list,
                'titlename':"BUG处理占比",
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(dic_sxt)
    ##################################生成BUG处理状态扇形图

    #####################################################BUG严重程度扇形图

    severity_data_all = API().APIall('get_severity', dic_module)['data']
    severity_all_dic={
            "key":severity_data_all['severity_all']['severity_name_all'],
              "values":severity_data_all['severity_all']['severity_sums_all'],
                'titlename':"所有BUG级别占比",
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(severity_all_dic)

    severity_NOclosed_dic={
            "key":severity_data_all['severity_NOclosed']['severity_name_NOclosed'],
              "values":severity_data_all['severity_NOclosed']['severity_sums_NOclosed'],
                'titlename':"未关闭BUG级别占比",
             "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }
    Fanchart(severity_NOclosed_dic)
    severity_NOclosed_1_2_sum=sum(severity_NOclosed_dic['values'][:2])#严重BUG数
    #####################################################严重程度扇形图

    ###############################################################生成BUG日增量条形图
    data_time = API().APIall('Check_new_BUG', dic_module)
    import datetime
    End_Time = str(data_time['End_Time'])
    dt = datetime.datetime.strptime(End_Time, "%Y-%m-%d")
    StartTime_7_day = (dt - datetime.timedelta(days=7)).strftime("%Y-%m-%d")

    dic_txt_BUG_rz = {
        "product": '',
        "module": module,
        "StartTime": StartTime_7_day,
        "End_Time": End_Time
    }
    txt_BUG_rz_data = API().APIall('grow_days', dic_txt_BUG_rz)
    dic_txt_BUG_rz_data = {
        "key": txt_BUG_rz_data['days_list'],
        "values": txt_BUG_rz_data["number_zs_list"],
        'titlename': "最近七日增量（BUG数）",
        'legend': Modulename,  # 图例名
         "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),

    }

    Bar_chart(dic_txt_BUG_rz_data)

    ################################################################生成BUG日增量条形图

    ##################################################生成所有BUG周期的折线图

    # key = ['星期一', '星期二', '星期三', '星期四', '星期五', '星期七', '星期日']
    # values = [100, 200, 300, 400, 100, 400, 300]
    # values2 = [200, 300, 200, 100, 200, 300, 400]
    dic_txt_BUG_all_time = {
        "product": '',
        "module": module,
        "StartTime": str(data_time["StartTime"]),
        "End_Time": End_Time
    }
    txt_BUG_rz_data_all = API().APIall('grow_days', dic_txt_BUG_all_time)
    dic_all_bug_data = {
        "key": txt_BUG_rz_data_all['days_list'],
        "values": txt_BUG_rz_data_all["number_zs_list"],
        'series_name': Modulename,  # 图例名
        'titlename': "全周期BUG日增量",
         "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
    }

    Line_chart(dic_all_bug_data)
    ##################################################生成所有BUG周期的折线图
    request_dic={
                 'synopsis':synopsis,
                 'head_addr': head_addr,
                "bug_list": data['data'],
                 "head": Modulename,
                  'entry_name_lies': entry_name_lies,
                   'zentao_zm':zentaos_zm()['zentao'],
                    'zentao_url':data['zentao_url'],
                    'data_product_sum': module_sum['data'],
                      "module_sum_html":dic_sxt['htmlname'],
                      'severity_NOclosed_1_2_sum':severity_NOclosed_1_2_sum,
                      'severity_NOclosed_html': severity_NOclosed_dic['htmlname'],
                      'severity_all_html': severity_all_dic['htmlname'],
                      "Importance_level_data_list": Importance_level_data_list,
                      'need_settle': need_settle,
                      'dic_txt_BUG_rz_data': dic_txt_BUG_rz_data['htmlname'],
                      'dic_all_bug_data': dic_all_bug_data['htmlname'],
                      'product':product,
                      'progress_chart_html': dic_progress_chart['htmlname']

                  }


    return render(request, "bug_list.html",request_dic )




def module_test(request):

    product = request.GET.get('product')
    dic_s = {"product":product,
            "module":""
           }
    data = API().APIall('get_product_sum', dic_s)


    #######################################进度图
    progress_chart_dic={
         "htmlname": '%s_%s_.html' % (time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime()), Add_call().random_str(30)),
        'titlename':'BUG修复率',
        'share':float(round(data['data']['data']['closed']/data['data']['sum_all']  if data['data']['sum_all']!=0 else 0.0,4)),

    }
    progress_chart(progress_chart_dic)
    request_dic={
        'progress_chart_dic': progress_chart_dic['htmlname']#progress_chart(progress_chart_dic).render_embed(),

    }

    # template = loader.get_template('search/test.html')
    # l = progress_chart(progress_chart_dic)  # 生成图像实例
    # context = dict(
    #     myechart=l.render_embed(),  # 必须要有
    #     host=REMOTE_HOST,  # 若前端加载了对应的echarts库，可以不需要这一句和下一句
    #     script_list=l.get_js_dependencies(),  # 以上两句代码的目的是下载该图标对应的一些echarts库
    # )
    # return HttpResponse(template.render(context, request))
    #
    # #return render(request, progress_chart(progress_chart_dic).render_embed(), request_dic)
    return render(request,'Report.html', request_dic)


    #######################################进度图


