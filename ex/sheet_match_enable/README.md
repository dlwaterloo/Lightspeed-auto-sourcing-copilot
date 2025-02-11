# Peer Funds 筛选工具

## 简介

根据Peer Funds 20250120-New Investment表格中Funding History中的数据，结合本地的PF Tracked List For Match正则表达式关键词库化后的Peer Funds名单，按年份、总投资机构数量、融资次数、Tracked Peer Funds数量筛选本地的Peer Funds数据，输出为Filtered Timestamp Peer Funds 20250120-New Investment表格。

## 使用方法

### 基本操作

在Windows环境下，将Peer Funds 20250120-New Investment.xlsx、PF Tracked List For Match.xlsx与Param_enable.xlsx放在与sheet_match_enable.exe同一文件夹中，双击启动，等待运行完毕后，生成Filtered Peer Funds 20250120-New Investment.xlsx，即为筛选结果。

### 参数设置

参数由Param_enable.xlsx导入。

* Year下方一行代表筛选年份；
* Fund下方一行代表总投资机构数下限；
* Hist下方一行代表融资次数下限；
* PF下方一行代表追踪的投资机构数下限；
* Rules右下方开始，代表上方三种规则的启用方式：
  * 每行为一组条件，1代表启用上方规则，0代表不启用，启用的规则须同时满足方代表该行条件满足；
  * 数据满足任一行条件，即被筛选输出。
