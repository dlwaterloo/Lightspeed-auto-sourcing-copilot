# 采购/招标信息整理思路

## 获取信息

对于不同公司，招投标信息需要分别整理，以下为部分主流公司采购招标信息公开情况：

* **联通**：存在[采购网站](http://www.chinaunicombidding.cn/bidInformation)，筛选“中标候选人公示”，根据标题进入网页后格式为**可以复制**的**文本**，有中标候选人和报价金额（部分有）等信息，理论上可以爬取。
* **电信**：存在[采购网站](https://caigou.chinatelecom.com.cn/search)，筛选“采购结果”和“直接采购”，根据标题进入网页后格式为**不可复制**的**文本**，有中标候选人和报价金额（部分有）等信息，理论上可以爬取。
* **移动**：存在[采购网站](https://b2b.10086.cn/#/biddingProcurementBulletin)，筛选“中选结果公示”和“单一来源采购公告”，根据标题进入网页后格式多为**不可复制和下载**的**加盖公章pdf**，仅有中标候选人信息，难以爬取。
* **浪潮**：存在[采购网站](https://scs.inspur.com/Announcement/announce)，筛选“候选人公告”，须先注册公司账号，无法直接访问。
* **华为**：[采购网站](https://scs.huawei.com/supplier/)无公开信息。
* **中兴**：[采购网站](https://supply.zte.com.cn/Sscm/UI/Web/Application/kxscm/kxsup_manager/Portal/index.aspx)无公开信息。
* **小米**：[采购网站](https://srm.p.mi.com/portal)无公开信息。
* **比亚迪**：[采购网站](https://sp.byd.com.cn/cdc-app/portalex/html_zh_CN/article_list.html?cat=tender_notice-list)仅招标公告，无中标信息。

除采购网站外，有从第三方网站获取信息的方案：

* [比地招标](www.bidizhaobiao.com)据说有上述无公开信息的公司的数据，未注册无法查看。
* [乙方宝招标](www.yfbzb.com)主要为工程招标，其他方面信息不多。

## 整理、筛选信息

招投标信息分为货物、工程、服务等门类。目前网站中，仅联通和浪潮标记招标信息性质。

招投标信息的中标公司，可以直接和烯牛的数据比对，获取行业信息。

可以按照烯牛战新（战略新兴产业）库，重点关注部分行业？

## 整合信息入库

参考烯牛数据的数据字典，以数据库为主要整理方式。若使用excel表格整理，把id修改为实际的公司名或事件名即可，然后可以忽略创建时间、修改时间和是否有效三个维度。

采购事件信息表：

| name        | type    | description                     |
| ----------- | ------- | ------------------------------- |
| id          | INT     | 主键                            |
| corporateId | INT     | 采购公司Id                      |
| deal        | BIGINT  | 成交金额                        |
| currency    | INT     | 币种                            |
| date        | DATETIME| 交易日期                        |
| form        | INT     | 成交方式（公开招投标、直接采购）|

采购关联信息表（通常情况下可以仅关注第一候选人）：

| name        | type | description               |
| ----------- | ---- | ------------------------- |
| id          | INT  | 主键                      |
| corporateId | INT  | 关联的公司主键            |
| bidId       | INT  | 关联的采购主键            |
| bidStatus   | INT  | 候选次序（第一候选人、第二候选人等） |

采购标签关联信息表：

| name      | type  | description                                                                 |
| --------- | ----- | --------------------------------------------------------------------------- |
| id        | INT   | 主键                                                                        |
| tagId     | INT   | 关联的tag主键                                                               |
| bidId     | INT   | 关联的采购主键                                                              |
| confidence| FLOAT | 当一个bid关联多个一级Tag时，confidence最大的为主行业。 |

采购行业关联信息表：

| name      | type     | description           |
| --------- | -------- | --------------------- |
| id        | INT(11)  | 主键                  |
| bidId     | INT      | 关联的采购主键        |
| hangyeId  | INT(11)  | 行业关联的主键        |
