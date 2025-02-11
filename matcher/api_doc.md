# 匹配工具接口文档

## 结构

* main.py: 主函数，调用；
* check_ipo.py: 查询给出公司名单的上市情况；
* check_dl_pf.py: 筛选出Deallog和Peer Funds名单中与给出公司名单匹配的部分；
* sheet_match_enable.py: 各类匹配函数的实现；（上一个项目中）若作为主函数，可以根据融资历史的条件筛选PF列表。

## 函数功能与接口

### sheet_match_enable.py

* find_substring_positions(A, substr): 找到子串substr在字符串A中的所有起始位置。
  * 参数:
    * A: 目标字符串。
    * substr: 要查找的子串。
  * 返回: 数值型list，代表所有起始位置。

* is_valid_substring(A, B): 判断公司简称B是否匹配公司全名A。
  * 采用特殊的分割关键词法:
    * B的长度为偶数时，每两个字符为一组，检查是否为A的子串；
    * B的长度为奇数时，最前面3个字符为一组，其余每两个字符为一组，检查是否为A的子串。
    * 判断时，B中的字符在A中不能重叠使用。
  * 参数:
    * A: 公司全名。
    * B: 公司简称。
  * 返回: True代表B是A的子串，False代表B不是A的子串。

* read_leftmost_column_to_list(file_path, sheet_name=0): 从指定的Excel文件中读取最左侧一列的正则表达式模式到列表中。
  * 参数:
    * file_path: Excel文件的路径。
    * sheet_name: 要读取的工作表名称或索引，默认为第一个工作表。

  * 返回: 包含所有正则表达式的列表。

* parse_string_to_dict(input_string): 将输入字符串解析为字典。
  * 参数:
    * input_string: 输入字符串。
  * 返回: 包含解析结果的字典。

* check_peer_match(test_string, peers): 检查输入字符串是否匹配Peer Funds列表中的任何一项。

  * 参数:
    * test_string: 要检查的字符串。
    * peers: 对手基金列表。

  * 返回: True代表匹配成功，False代表匹配失败。

* check_conditions(info, result, conditions): 检查结果是否满足给定的条件。

  * 参数:
    * info: 信息元组，包含所有基金数量、历史融资数量和对手基金数量。
    * result: 结果元组，包含融资数量、历史融资数量和包含对手基金数量。
    * conditions: 条件列表，每个元素是一个三元组，表示是否启用基金数量、历史融资数量和对手基金数量的条件。

  * 返回: True代表满足条件，False代表不满足条件。

* return_chinese(word, safe_suffixes): 返回字符串中的中文字符，（同时可以扩展过滤不需要的前后缀的功能）。
  * 参数:
    * word: 输入字符串。
    * safe_suffixes: （未启用）不需要过滤的后缀列表。
  * 返回: 过滤后的字符串。

* check_dl_pf_and_collect(row, column_name, companies, suffixes): 检查行中的公司名称是否包含在用来匹配的公司全名列表中。
  * 参数:
    * row: 行数据。
    * column_name: 列名。
    * companies: 用来匹配的公司全名列表。
    * suffixes: （未启用）不需要过滤的后缀列表。
  * 返回: True代表匹配成功，False代表匹配失败。

* check_and_collect(row, column_name, info, peers, conditions): 检查行中的融资历史是否满足给定的条件。
  * 参数:
    * row: 行数据。
    * column_name: 列名。
    * info: 信息元组，包含所有基金数量要求、历史融资数量要求和对手基金数量要求。
    * peers: 对手基金列表。
    * conditions: 条件列表，每个元素是一个三元组，表示是否启用基金数量、历史融资数量和对手基金数量的条件。
  * 返回: True代表满足条件，False代表不满足条件。

* filter_timestamp(df, info, peers, conditions): 根据给定的条件过滤数据。
  * 参数:
    * df: 数据框。
    * info: 信息元组，包含所有基金数量要求、历史融资数量要求和对手基金数量要求。
    * peers: 对手基金列表。
    * conditions: 条件列表，每个元素是一个三元组，表示是否启用基金数量、历史融资数量和对手基金数量的条件。
  * 返回: df_filtered: 过滤后的数据框。

* output_filtered(df, output_file): 将过滤后的数据保存到Excel文件中。
  * 参数:
    * df: 过滤后的数据框。
    * output_file: 输出文件名。
  * 返回: 无。

### track_modify.py

* clean_and_add_wildcards(value, refixes_to_remove, suffixes_to_remove, check_list): 从字符串中删除前缀和后缀，然后添加通配符。
  * 参数:
    * value: 要清理和添加通配符的字符串。
    * prefixes_to_remove: 要从字符串中删除的前缀。
    * suffixes_to_remove: 要从字符串中删除的后缀（在中间的出现也可删去）。
    * check_list: 检查字符串是否以 '.*' 结尾或开始
  * 返回: 清理和添加通配符后的字符串。

* read_and_clean(input_file_path, output_file_path, prefixes, suffixes, check_list): 读取Excel文件，清理并添加通配符，然后将结果写入新的Excel文件。
  * 参数:
    * input_file_path: 输入Excel文件的路径。
    * output_file_path: 输出Excel文件的路径。
    * prefixes: 要从字符串中删除的前缀。
    * suffixes: 要从字符串中删除的后缀。
    * check_list: 检查字符串是否以 '.*' 结尾或开始。
  * 返回: 无。

### check_ipo.py

* check_name_ipo(check_name, ipo_list_a, ipo_list_h): 检查企业名称是否在A股和港股IPO列表中。
  * 参数:
    * check_name: 要检查的企业名称。
    * ipo_list_a: A股IPO列表。
    * ipo_list_h: 港股IPO列表。
  * 返回: A股和港股名称。
* output_list_ipo(input_file, ipo_a, ipo_h, places, output_file): 从输入文件中读取企业名称，然后在A股和港股IPO列表中查找匹配的企业名称，将匹配的企业名称写入输出文件。
* 参数:
  * input_file: 输入文件的路径。
  * ipo_a: A股IPO列表的路径。
  * ipo_h: 港股IPO列表的路径。
  * places: （未启用）不需删去的地名列表。
  * output_file: 输出文件的路径。
* 返回: 匹配的企业名称的DataFrame。

### check_dl_pf.py

* output_list_dl_pf(input_file, dl_file, pf_file, dl_out_file, pf_out_file, check_suffixes): 从输入文件中读取企业名称，然后在DL和PF文件中查找匹配的企业名称，将匹配的企业名称写入DL和PF输出文件。
* 参数:
  * input_file: 输入文件的路径。
  * dl_file: DL文件的路径。
  * pf_file: PF文件的路径。
  * dl_out_file: 输出DL文件的路径。
  * pf_out_file: 输出PF文件的路径。
  * check_suffixes: （未启用）不需删去的后缀列表。
* 返回: 匹配的DL和PF文件的DataFrame
