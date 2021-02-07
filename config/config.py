
def head_server():#前端访问地址

	import socket
	def get_host_ip():#获取电脑ip
		"""
        查询本机ip地址
        :return: ip
        """
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			s.connect(('8.8.8.8', 80))
			ip = s.getsockname()[0]
		finally:
			s.close()

		return ip


	dic={
		"host":get_host_ip(),#127.0.0.1 #192.168.1.55
		'port':9002

	}
	return dic


def config_bug():
	config = {
		"severity": {
			"1": "致命",
			"2": "严重",
			"3": "一般",
			"4": "轻微",

		},
		"status": {
			'closed': "关闭",
			'active': "激活",
			'resolved': "待验证"
		},
		'pri': {
			"1": "紧急",
			"2": "高",
			"3": "中",
			"4": "低",
		},

	}
	return config


def zentaos_zm():
	zentao_zm = {
		"zentao": '如没有禅道账户请使用访客账户查看BUG详情：fangke001  123456'
	}

	return zentao_zm


def zentao_list():
	module_list = ['编号', '模块名称', '总数', '已修复', '未修复', '待验证','致命级','严重级','一般级','轻微级','修复率 /%','责任人','发布建议','详情']
	bug_list = ['序列', '项目', '模块', 'BUG编号', 'BUG标题', '严重程度', '优先级', 'BUG状态', '创建日期', '指派给', '由谁创建', '详情']
	pro_list = [ '编号', '项目名称', 'BUG总数', '已修复', '未修复', '待验证','致命级','严重级','一般级','轻微级','修复率 /%','责任人','发布建议','详情']
	return {"module_list": module_list, 'bug_list': bug_list, 'pro_list': pro_list}

def product_lusion(dic):
	# dic={
	# 	'product':'',
	# 	'module': '',
	# 	'bug_total':"",
	# 	'closed_sum': "关闭",
	# 	'active_sum': "激活",
	# 	'resolved_sum': "待验证",
	# 	'severity_1': '',
	# 	'severity_2': '',
	# 	'severity_3': '',
	# 	'severity_4': '',
	# }

	lusion={
		'brief_4':'%s项目，提交%s个BUG，已修复解决%s个BUG；待解决BUG数为%s，待验证BUG数为%s；有%s个较严重BUG（严重/致命）需要优先处理。'%(dic['product'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_2'] + dic['severity_1']),
		'brief_3':'%s项目，提交%s个BUG，已修复解决%s个BUG；待解决BUG数为%s，待验证BUG数为%s；暂无较严重问题（严重/致命），剩余%s个一般级BUG需要进行修复。'%(dic['product'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_3'] ),
		'brief_2':'%s项目，提交%s个BUG，已修复解决%s个BUG；待解决BUG数为%s，待验证BUG数为%s；暂无一般级（一般/严重/致命）以上BUG，剩余%s个轻微级BUG可在后续版本迭代中处理。'%(dic['product'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_4'] ),
		'brief_1':'%s项目，提交%s个BUG，已修复解决%s个BUG，所有BUG均已解决，可交付正式版本。'%(dic['product'],dic['bug_total'],dic['closed_sum']),
		'brief_-1': '%s项目，暂未开始。' % (dic['product']),
	}
	return lusion
def module_lusion(dic):


	lusion={
		'brief_4':'%s项目，%s模块，提交%s个BUG，已修复解决%s个BUG；待解决BUG数为%s，待验证BUG数为%s；有%s个较严重BUG（严重/致命）需要优先处理。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_2'] + dic['severity_1']),
		'brief_3':'%s项目，%s模块，提交%s个BUG，已修复解决%s个BUG；待解决BUG数为%s，待验证BUG数为%s；暂无较严重问题（严重/致命），剩余%s个一般级BUG需要进行修复。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_3'] ),
		'brief_2':'%s项目，%s模块，提交%s个BUG，已修复解决%s个BUG；待解决BUG数为%s，待验证BUG数为%s；暂无一般级（一般/严重/致命）以上BUG，剩余%s个轻微级BUG可在后续版本迭代处理。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_4'] ),
		'brief_1':'%s项目，%s模块，提交%s个BUG，已修复解决%s个BUG；所有BUG均已解决，可交付正式版本。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum']),
		'brief_-1': '%s项目，%s模块，暂未开始。' % (dic['product'], dic['module']),
	}
	return lusion
def product_Next_step(dic):

	'项目，各模块以下BUG需要优先处理（严重级以上）：'
	lusion={
		'brief_4':'%s项目，以下较严重BUG（致命/严重）需要优先处理：（%s）'%(dic['product'],zentaos_zm()['zentao']),
		'brief_3':'%s项目，以下BUG（一般）需要进行修复：（%s）'%(dic['product'],zentaos_zm()['zentao']),
		'brief_2':'%s项目，以下BUG（轻微）可在后续版本迭代中解决处理：（%s）'%(dic['product'],zentaos_zm()['zentao']),
		'brief_1': '%s项目，暂无需要处理的BUG' % (dic['product']),
		'brief_-1': '%s项目，暂未开始。' % (dic['product']),
	}
	return lusion
def module_Next_step(dic):
	lusion={
		'brief_4':'%s项目，%s模块，以下BUG（致命/严重）需要优先处理：（%s）'%(dic['product'],dic['module'],zentaos_zm()['zentao']),
		'brief_3':'%s项目，%s模块，以下BUG（一般）需要进行修复：（%s）'%(dic['product'],dic['module'],zentaos_zm()['zentao']),
		'brief_2':'%s项目，%s模块，以下BUG（轻微）可在后续版本迭代中解决处理：（%s）'%(dic['product'],dic['module'],zentaos_zm()['zentao']),
		'brief_1': '%s项目，%s模块，暂无需要处理的BUG' % (dic['product'], dic['module']),
		'brief_-1': '%s项目，%s模块，暂未开始。' % (dic['product'], dic['module']),
	}
	return lusion
def database():#禅道数据库地址
	dic={
		"host":"192.168.1.55",#127.0.0.1"
		'user':'root',
		'password' : "hl123456",
		'DB':'zentao',
		'port':3306
	}
	return dic

def zentao_Addr():#禅道地址
	dic={
		"host":"192.168.1.55",
		'port':81

	}
	return dic




def configs():
	config = {
		"severity": {
			"1": "致命",
			"2": "严重",
			"3": "一般",
			"4": "轻微",

		},
		"status": {
			'closed': "关闭",
			'active': "激活",
			'resolved': "待验证"
		},
		'pri': {
			"1": "紧急",
			"2": "高",
			"3": "中",
			"4": "低",
		}
	}

	return config
def status():

	return ['closed','active','resolved']

def severity():
	return ["1","2","3","4"]


def Repair_threshold():#修复率阀值
	repair_threshold=80  #修复率阀值
	return repair_threshold
def Company_info():
	cominfo={
		'comname':'西安火眼猴智能科技研究院有限公司',
		'address_com':'www.hllok.com',
		'address_lxwm':'http://www.hllok.com/lianxiwomen.jsp',
		'address_cjwt': "http://www.hllok.com/index.jsp",
		'address_yjfk': "http://bbs.hllok.com/forum-4-1.html",
		'address_yqlj': "http://www.hllok.com",
		'address_work':"中国(陕西)西安高新区科技路旺座国际城C座1101室",
		'record_ICP':'陕ICP备14009079号-1',
		'record_sgwa': '51019002000701',


	}
	return cominfo
