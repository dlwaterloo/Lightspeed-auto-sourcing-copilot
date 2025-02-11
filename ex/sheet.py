import pandas as pd


def filter_category(df):

	filter = 'Category'

	# 获取用户输入的筛选字符串
	string_to_match = input("请输入要筛选的Category名称（留空则不过滤）：").strip()

	# 使用str.contains进行筛选
	if string_to_match:
		df_filtered = df[df[filter].str.contains(string_to_match, na=False)]
	else:
		df_filtered = df.copy()

	# 显示数据概览
	print(df_filtered)

	return df_filtered


def filter_peer_fund(df):

	filter = 'Peer Fund'

	# 获取用户输入的筛选字符串
	string_to_match = input("请输入要筛选的Peer Fund名称（留空则不过滤）：").strip()

	# 使用str.contains进行筛选
	if string_to_match:
		df_filtered = df[df[filter].str.contains(string_to_match, na=False)]
	else:
		df_filtered = df.copy()

	# 显示数据概览
	print(df_filtered)

	return df_filtered


def filter_timestamp(df):

	date_column = 'Updated'

	# 检查日期列是否被正确解析为 datetime 类型
	if not pd.api.types.is_datetime64_any_dtype(df[date_column]):
		raise ValueError(f"Column '{date_column}' is not parsed as a datetime type.")

	# 获取用户输入的筛选字符串
	date_start = input("请输入要筛选的起始日期（格式YYYY-MM-DD，留空则不过滤）：").strip()

	if date_start:
		df_date = df[df[date_column] >= date_start]
	else:
		df_date = df.copy()

	# 获取用户输入的筛选字符串
	date_end = input("请输入要筛选的终止日期（格式YYYY-MM-DD，留空则不过滤）：").strip()

	if date_end:
		df_date_out = df_date[df_date[date_column] <= date_end]
	else:
		df_date_out = df_date.copy()

	# 显示数据概览
	print(df_date_out)

	return df_date_out


# 读取Excel文件
input_file = 'Peer Funds 20250120-New Investment.xlsx'  # 输入文件名
output_file = 'Filtered Timestamp Peer Funds 20250120-New Investment.xlsx'  # 输出文件名

df = pd.read_excel(input_file)

df_category = filter_category(df)

df_peer_fund = filter_peer_fund(df_category)

df_date = filter_timestamp(df_peer_fund)

df_date.to_excel(output_file, index=True)
