import pandas as pd
import re
import sheet_match_enable as smat


def check_name_ipo(check_name, ipo_list_a, ipo_list_h):
	"""
	检查企业名称是否在A股和港股IPO列表中。
	
	:param check_name: 要检查的企业名称
	:param ipo_list_a: A股IPO列表
	:param ipo_list_h: 港股IPO列表
	:return: A股和港股名称
	"""
	check_name = re.sub('有限公司$|有限责任公司$', '', check_name)
	a_name = ''
	h_name = ''
	for name in ipo_list_a:
		name = re.sub('A$', '', name)
		name = re.sub('-..?$', '', name)
		name = re.sub('^\*', '', name)
		name = re.sub('^ST', '', name)
		if smat.is_valid_substring(check_name, name):
			a_name = name
	for name in ipo_list_h:
		name = re.sub(r'\([^)]*\)|（[^）]*）', '', name)
		name = re.sub('A$', '', name)
		name = re.sub('B$', '', name)
		name = re.sub('-..?$', '', name)
		if smat.is_valid_substring(check_name, name):
			h_name = name

	return a_name, h_name


def output_list_ipo(input_file, ipo_a, ipo_h, places, output_file):
	"""
	从输入文件中读取企业名称，然后在A股和港股IPO列表中查找匹配的企业名称。
	将匹配的企业名称写入输出文件。	
	
	:param input_file: 输入文件的路径
	:param ipo_a: A股IPO列表的路径
	:param ipo_h: 港股IPO列表的路径
	:param places: （未启用）不需删去的地名列表
	:param output_file: 输出文件的路径
	:return: 匹配的企业名称的DataFrame
	"""
	# 读取IPO列表
	ipo_df_a = pd.read_excel(ipo_a, usecols=[0], header=0)
	ipo_list_a = ipo_df_a.iloc[:, 0].dropna().astype(str).tolist()
	ipo_df_h = pd.read_excel(ipo_h, usecols=[0], header=0)
	ipo_list_h = ipo_df_h.iloc[:, 0].dropna().astype(str).tolist()

	# 读取企业名称
	df = pd.read_excel(input_file, usecols=[0], header=0)
	df = df[df.iloc[:, 0] != '企业名称'].dropna()
	check_list = df.iloc[:, 0].dropna().astype(str).tolist()

	# 检查企业名称是否在A股和港股IPO列表中
	rows = []
	for check_name in check_list:
		a_name, h_name = check_name_ipo(check_name, ipo_list_a, ipo_list_h)
		row = {
			'全名': check_name,
			'A股名称': a_name,
			'港股名称': h_name
		}
		rows.append(row)
	df_out = pd.DataFrame(rows)
	print(df_out)
	df_out.to_excel(output_file, index=False, header=True)
	return df_out