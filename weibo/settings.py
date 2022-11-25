# -*- coding: utf-8 -*-

BOT_NAME = 'weibo'
SPIDER_MODULES = ['weibo']
NEWSPIDER_MODULE = 'weibo'
COOKIES_ENABLED = False
TELNETCONSOLE_ENABLED = False
LOG_LEVEL = 'ERROR'
# 访问完一个页面再访问下一个时需要等待的时间，默认为10秒
DOWNLOAD_DELAY = 10
DEFAULT_REQUEST_HEADERS = {
    'Accept':
    'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': '_ga=GA1.2.1319455029.1669267767; _gid=GA1.2.1918322031.1669267767; SINAGLOBAL=8311579724276.11.1669267770890; ULV=1669267770892:1:1:1:8311579724276.11.1669267770890:; wb_view_log=1536*8641.25; WBPSESS=Dt2hbAUaXfkVprjyrAZT_Hdk9HSYtvNEmyfVcsDlSutN9cGcr8E7skg7IlRgk42eunJ3zTIP0P1mnqZoIxyH4f-H1bbtQnrE50z-7FR0b1uFEsEnVcBrnxhtuVjaYt5Qu85QFhMBlulIilXtyDZ7kdr59QT2_MKV0yON1kPUAVXe8EKzdZ0kZDztdVEbyZOdPDm_wS8hvwqCJKfhVw8x3g==; XSRF-TOKEN=9GWLwt870-SgNxsjWMzx30Lb; PC_TOKEN=66dfaacf0f; SCF=AlUPGrF9hpWtB37SIGN-WnR4fkpxZOoDq1c_g0BgoWQLh1W92Mmd1pIdXoK-frKXQ6oQNZSuYZ4hOIAhH13bRHc.; SUB=_2A25Oe_9hDeRhGeFM6lES-C3OzzqIHXVt8VeprDV8PUNbmtAKLUulkW9NQPP7L1CABDtRXoYXQfkn1siqHh3aTnR-; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFxvZTrlWuATMgHmwfMr-Rh5JpX5KMhUgL.FoMEeKe01heEShq2dJLoI7D-qPxDqg4ywJyf'
}
ITEM_PIPELINES = {
    'weibo.pipelines.DuplicatesPipeline': 300,
    'weibo.pipelines.CsvPipeline': 301,
    'weibo.pipelines.MysqlPipeline': 302,
}
# 要搜索的关键词列表，可写多个, 值可以是由关键词或话题组成的列表，也可以是包含关键词的txt文件路径，
# 如'keyword_list.txt'，txt文件中每个关键词占一行
#KEYWORD_LIST = ['新冠肺炎', '北京冬奥会','卡塔尔世界杯']  或者 KEYWORD_LIST = 'keyword_list.txt'
KEYWORD_LIST = ['台湾是中国的']
# 要搜索的微博类型，0代表搜索全部微博，1代表搜索全部原创微博，2代表热门微博，3代表关注人微博，4代表认证用户微博，5代表媒体微博，6代表观点微博
WEIBO_TYPE = 1
# 筛选结果微博中必需包含的内容，0代表不筛选，获取全部微博，1代表搜索包含图片的微博，2代表包含视频的微博，3代表包含音乐的微博，4代表包含短链接的微博
CONTAIN_TYPE = 0
# 筛选微博的发布地区，精确到省或直辖市，值不应包含“省”或“市”等字，如想筛选北京市的微博请用“北京”而不是“北京市”，想要筛选安徽省的微博请用“安徽”而不是“安徽省”，可以写多个地区，
# 具体支持的地名见region.py文件，注意只支持省或直辖市的名字，省下面的市名及直辖市下面的区县名不支持，不筛选请用“全部”
REGION = ['全部']
# 搜索的起始日期，为yyyy-mm-dd形式，搜索结果包含该日期
START_DATE = '2022-11-24'
# 搜索的终止日期，为yyyy-mm-dd形式，搜索结果包含该日期
END_DATE = '2022-11-24'
# 进一步细分搜索的阈值，若结果页数大于等于该值，则认为结果没有完全展示，细分搜索条件重新搜索以获取更多微博。数值越大速度越快，也越有可能漏掉微博；数值越小速度越慢，获取的微博就越多。
# 建议数值大小设置在40到50之间。
FURTHER_THRESHOLD = 46
# 图片文件存储路径
IMAGES_STORE = './'
# 视频文件存储路径
FILES_STORE = './'
# 配置MongoDB数据库
# MONGO_URI = 'localhost'
# 配置MySQL数据库，以下为默认配置，可以根据实际情况更改，程序会自动生成一个名为weibo的数据库，如果想换其它名字请更改MYSQL_DATABASE值
MYSQL_HOST = 'localhost'
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = '2021/11/21'
MYSQL_DATABASE = 'weibo'
