import pandas as pd
import re
import sheet_match_enable as smat

def output_list_dl_pf(input_file, dl_file, pf_file, dl_out_file, pf_out_file, check_suffixes):
	"""
	从输入文件中读取企业名称，然后在DL和PF文件中查找匹配的企业名称。
	将匹配的企业名称写入DL和PF文件。
	
	:param input_file: 输入文件的路径
	:param dl_file: DL文件的路径
	:param pf_file: PF文件的路径
	:param dl_out_file: 输出DL文件的路径
	:param pf_out_file: 输出PF文件的路径
	:param check_suffixes: （未启用）不需删去的后缀列表
	:return: 匹配的DL和PF文件的DataFrame
	"""
	df = pd.read_excel(input_file, usecols=[0], header=0)
	df = df[df.iloc[:, 0] != '企业名称'].dropna()
	# 从输入文件中读取企业名称
	check_list = df.iloc[:, 0].dropna().astype(str).tolist()

	df_dl = pd.read_excel(dl_file)
	# 从DL文件中筛选出符合条件的企业名称
	df_dl_filtered = df_dl[df_dl.apply(smat.check_dl_pf_and_collect, args=(
		"项目名称", check_list, check_suffixes), axis=1)].reset_index(drop=True)
	
	df_pf = pd.read_excel(pf_file)
	# 从PF文件中筛选出符合条件的企业名称
	df_pf_filtered = df_pf[df_pf.apply(smat.check_dl_pf_and_collect, args=(
		"Company", check_list, check_suffixes), axis=1)].reset_index(drop=True)
	
	# 输出匹配的企业名称
	print(df_dl_filtered)
	print(df_pf_filtered)
	df_dl_filtered.to_excel(dl_out_file, index=False, header=True)
	df_pf_filtered.to_excel(pf_out_file, index=False, header=True)
	return df_dl_filtered, df_pf_filtered
