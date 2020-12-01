
def terminal_server():#服务器地址
	dic={
		"host":"192.168.1.182",
		'port':9001

	}
	return dic
def head_server():#前端访问地址
	dic={
		"host":"192.168.1.182",
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
	module_list = ['编号', '模块名称', '总数', '已修复', '未修复', '待验证','致命级','严重级','一般级','轻微级','修复率','责任人','发布建议','详情']
	bug_list = ['序列', '项目', '模块', 'BUG编号', 'BUG标题', '严重程度', '优先级', 'BUG状态', '创建日期', '指派给', '由谁创建', '详情']
	pro_list = [ '编号', '项目名称', 'BUG总数', '已修复', '未修复', '待验证','致命级','严重级','一般级','轻微级','修复率','责任人','发布建议','详情']
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
		'brief_4':'%s项目，已提交%s个BUG，已修复解决%s个BUG；当前待解决BUG数为%s，待验证BUG数为%s；有%s个较严重BUG（严重/致命）需要优先处理。'%(dic['product'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_2'] + dic['severity_1']),
		'brief_3':'%s项目，已提交%s个BUG，已修复解决%s个BUG；当前待解决BUG数为%s，待验证BUG数为%s；暂无较严重问题（严重/致命），可发布试用版本，但仍需要对剩余%s个一般级BUG进行修复。'%(dic['product'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_3'] ),
		'brief_2':'%s项目，已提交%s个BUG，已修复解决%s个BUG；当前待解决BUG数为%s，待验证BUG数为%s；暂无一般级（一般/严重/致命）以上BUG，可发布正式版本，剩余%s个轻微级BUG可在后续版本迭代中处理。'%(dic['product'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_4'] ),
		'brief_1':'%s项目，已提交%s个BUG，已修复解决%s个BUG，所有BUG均已解决，可交付正式版本。'%(dic['product'],dic['bug_total'],dic['closed_sum']),
		'brief_-1': '%s项目，暂未开始。' % (dic['product']),
	}
	return lusion
def module_lusion(dic):


	lusion={
		'brief_4':'%s项目，%s模块，已提交%s个BUG，已修复解决%s个BUG；当前待解决BUG数为%s，待验证BUG数为%s；有%s个较严重BUG（严重/致命）需要优先处理。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_2'] + dic['severity_1']),
		'brief_3':'%s项目，%s模块，已提交%s个BUG，已修复解决%s个BUG；当前待解决BUG数为%s，待验证BUG数为%s；暂无较严重问题（严重/致命），但仍需要对剩余%s个一般级BUG进行修复处理。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_3'] ),
		'brief_2':'%s项目，%s模块，已提交%s个BUG，已修复解决%s个BUG；当前待解决BUG数为%s，待验证BUG数为%s；暂无一般级（一般/严重/致命）以上BUG，可发布正式版本，剩余%s个轻微级BUG可在后续版本迭代处理。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum'],dic['active_sum'],dic['resolved_sum'],dic['severity_4'] ),
		'brief_1':'%s项目，%s模块，已提交%s个BUG，已修复解决%s个BUG；所有BUG均已解决，可交付正式版本。'%(dic['product'],dic['module'],dic['bug_total'],dic['closed_sum']),
		'brief_-1': '%s项目，%s模块，暂未开始。' % (dic['product'], dic['module']),
	}
	return lusion
def product_Next_step(dic):

	'项目，各模块以下BUG需要优先处理（严重级以上）：'
	lusion={
		'brief_4':'%s项目，以下较严重BUG（致命/严重）需要优先处理：（%s）'%(dic['product'],zentaos_zm()['zentao']),
		'brief_3':'%s项目，以下BUG（一般）处理完成可发布正式版本：（%s）'%(dic['product'],zentaos_zm()['zentao']),
		'brief_2':'%s项目，以下BUG（轻微）可在后续版本迭代中解决处理：（%s）'%(dic['product'],zentaos_zm()['zentao']),
		'brief_1': '%s项目，暂无需要处理的BUG' % (dic['product']),
		'brief_-1': '%s项目，暂未开始。' % (dic['product']),
	}
	return lusion
def module_Next_step(dic):
	lusion={
		'brief_4':'%s项目，%s模块，以下BUG（致命/严重）需要优先处理：（%s）'%(dic['product'],dic['module'],zentaos_zm()['zentao']),
		'brief_3':'%s项目，%s模块，以下BUG（一般）处理完成可发布正式版本：（%s）'%(dic['product'],dic['module'],zentaos_zm()['zentao']),
		'brief_2':'%s项目，%s模块，以下BUG（轻微）可在后续版本迭代中解决处理：（%s）'%(dic['product'],dic['module'],zentaos_zm()['zentao']),
		'brief_1': '%s项目，%s模块，暂无需要处理的BUG' % (dic['product'], dic['module']),
		'brief_-1': '%s项目，%s模块，暂未开始。' % (dic['product'], dic['module']),
	}
	return lusion
