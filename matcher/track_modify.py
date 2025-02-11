import pandas as pd
import re
import sheet_match_enable as smat


def replace_caret_with_wildcard(value):
    """
    如果字符串以'^'开头，则将其替换为'.*'。
    """
    if isinstance(value, str) and value.startswith('^'):
        return '.*' + value[1:]  # 替换'^'为'.*'
    return value


def clean_and_add_wildcards(value, prefixes_to_remove, suffixes_to_remove, check_list):
    """
    从字符串中删除前缀和后缀，然后添加通配符。

    :param value: 要清理和添加通配符的字符串
    :param prefixes_to_remove: 要从字符串中删除的前缀
    :param suffixes_to_remove: 要从字符串中删除的后缀（在中间的出现也可删去）
    :param check_list: 检查字符串是否以 '.*' 结尾或开始
    :return: 清理和添加通配符后的字符串
    """
    # 移除括号内的内容
    value = re.sub(r'\([^)]*\)|（[^）]*）', '', value)
    for suffix in suffixes_to_remove:
        value = re.sub(rf'{suffix}', '', value)  # 移除后缀，如果存在的话

    for prefix in prefixes_to_remove:
        value_check = re.sub(rf'{prefix}', '', value)  # 移除前缀，如果存在的话
        if all((not re.match(rf'{check_suffix}$', value_check)) for check_suffix in check_list):
            value = value_check

    # 检查字符串是否已经以 '.*' 结尾或开始
    if not value.endswith('.*'):
        value = f'{value}.*'
    if not value.startswith('.*'):
        value = f'.*{value}'
    return value



def read_and_clean(input_file_path, output_file_path, prefixes, suffixes, check_list):
    """
    读取Excel文件，清理并添加通配符，然后将结果写入新的Excel文件。
    
    :param input_file_path: 输入Excel文件的路径
    :param output_file_path: 输出Excel文件的路径
    :param prefixes: 要从字符串中删除的前缀
    :param suffixes: 要从字符串中删除的后缀
    :param check_list: 检查字符串是否以 '.*' 结尾或开始
    """
    # 读取Excel文件
    df = pd.read_excel(input_file_path, usecols=[0], header=0)
    # 删除空行和标题行
    df = df[df.iloc[:, 0] != '企业名称'].dropna()
    # 应用清理和添加前后缀的函数到整个列
    df = df.iloc[:, 0].astype(str).apply(clean_and_add_wildcards, args=(prefixes, suffixes, check_list))
    # 打印结果
    print(df)
    # 写入新的Excel文件
    df.to_excel(output_file_path, index=False, header=False)
