# 公司全名匹配工具

## 简介

根据提供公司全名的表格（如单项冠军名单），匹配并筛选出A股、港股上市情况和Peer Funds和Deallog中的记录。

## 环境与操作

单个可执行文件，在Windows环境下运行，若识别为恶意软件需要点击信任。创建`/dat`和`/output`两个文件夹和`/dat`中输入文件后，双击可执行文件执行，在`/output`中获取输出。

## 输入说明

* 在可执行文件目录下的`/dat`文件夹的下列Excel文件，注意第一行为表头，不为内容。
* 既有信息表格：
  * Companies.xlsx：公司全名表，仅第一列有效，须从原名单中手动复制到第一列；
  * IPO A.xlsx：A股上市情况表，万得数据删去第一列代码后得到；
  * IPO H.xlsx：港股上市情况表，万得数据删去第一列代码后得到；
  * Deallog List.xlsx：Deallog表，与飞书一致；
  * Peer Funds.xlsx：PF表，与飞书一致；
* 用来提取公司关键词的辅助表：
  * Prefix.xlsx：代表需要忽略的前缀地名（如上海、深圳等）；
  * Suffix.xlsx（暂未启用）：代表需要忽略的行业关键词（如科技、器材、电子等）和常见附属词（如地名指示词市、县和公司名后缀股份、有限公司等）；
  * Check Suffix.xlsx：带有此表格中关键词的公司，地名同时作为公司名称关键词，不筛选掉。

## 输出说明

* **注意事项**：
  * 须提前在main.exe同级文件夹创建`/output`文件夹，否则无法输出；
  * 输出结果中有部分偏差，需要人工检测。
* 输出文件列表：
  * IPO Check.xlsx：列表中公司在A股和港股的上市情况；
  * Filtered Deallog List.xlsx：列表中公司在Deallog中的出现情况；
  * Filtered Peer Fund List.xlsx：列表中公司在Peer Fund中的出现情况。
