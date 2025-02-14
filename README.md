# Lightspeed-auto-sourcing-copilot

Update: 优化总README，更新整理招投标信息的项目初稿（仅包含初步Solution文件`sol.md`）

## 介绍

共三个项目文件夹，包含Python处理脚本和内部数据表格，以及自行整理的部分数据。
脚本均可通过pyinstaller打包为应用程序。

## matcher

根据提供公司全名的表格（如单项冠军名单），匹配并筛选出A股、港股上市情况和Peer Funds和Deallog中的记录。

具体介绍见文件夹中`README.md`和`api_doc.md`。

## ex

包含如下脚本文件（均为单文件脚本）：

* `new.py`: （未启用）测试正则表达式。
* `sheet.py`: （未启用）根据Category和Update Time，筛选Peer Funds投资项目表格中信息。
* `sheet2.py`（即`sheet_match\sheet_match.py`）: 根据参数表格Param.xlsx中输入的年份、总投资机构数、单年份融资次数、位于PF Tracked List中投资机构数的四个条件，由Funding History一栏筛选Peer Funds投资项目表格中的信息。有and和or两种处理条件的形式。
* `sheet_match_enable\sheet_match_enable.py`: 功能基本同上，条件带使能端决定是否启用，通过Param输入，具体见`sheet_match_enable\README.md`。

此外，文件夹包含把追踪投资机构表格`PF Tracked List.xlsx`处理成正则表达式格式的`PF Tracked List For Match.xlsx`。相关处理函数已注释掉，在`sheet2.py`中。

## bid

无代码，关于招投标信息处理与整理的部分构思。`draft.txt`为草稿，`sol.md`为半成品初稿。
