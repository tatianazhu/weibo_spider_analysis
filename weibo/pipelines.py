# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import copy
import csv
import os

import scrapy
from scrapy.exceptions import DropItem
from scrapy.pipelines.files import FilesPipeline
from scrapy.pipelines.images import ImagesPipeline
from scrapy.utils.project import get_project_settings

settings = get_project_settings()


class CsvPipeline(object):
    def process_item(self, item, spider):
        # base_dir = 'output' + os.sep + item['keyword']
        base_dir = 'output' + os.sep
        if not os.path.isdir(base_dir):
            os.makedirs(base_dir)
        file_path = base_dir + os.sep + item['keyword'] + '.csv'
        if not os.path.isfile(file_path):
            is_first_write = 1
        else:
            is_first_write = 0
        if item:
            with open(file_path, 'a', encoding='utf-8-sig', newline='') as f:
                writer = csv.writer(f)
                if is_first_write:
                    header = ['id', 'user_id', '用户昵称', '微博正文', '话题', '转发数', '评论数', '点赞数', '发布时间']
                    writer.writerow(header)
                keys = ['id', 'user_id', 'screen_name', 'text', 'topics', 'reposts_count', 'comments_count', 'attitudes_count', 'created_at']
                writer.writerow(
                    # [item['weibo'][key] for key in item['weibo'].keys()])
                    [item['weibo'][key] for key in keys])
        return item


class MysqlPipeline(object):
    def create_database(self, mysql_config):
        """创建MySQL数据库"""
        import pymysql
        sql = """CREATE DATABASE IF NOT EXISTS %s DEFAULT
            CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci""" % settings.get(
            'MYSQL_DATABASE', 'weibo')
        db = pymysql.connect(**mysql_config)
        cursor = db.cursor()
        cursor.execute(sql)
        db.close()

    def create_table(self):
        """创建MySQL表"""
        sql = """
                CREATE TABLE IF NOT EXISTS weibo (
                id varchar(20) NOT NULL,
                user_id varchar(20),
                screen_name varchar(30),
                text varchar(2000),
                topics varchar(200),
                created_at DATETIME,
                attitudes_count INT,
                comments_count INT,
                reposts_count INT,
                PRIMARY KEY (id)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4"""
        self.cursor.execute(sql)

    def open_spider(self, spider):
        try:
            import pymysql
            mysql_config = {
                'host': settings.get('MYSQL_HOST', 'localhost'),
                'port': settings.get('MYSQL_PORT', 3306),
                'user': settings.get('MYSQL_USER', 'root'),
                'password': settings.get('MYSQL_PASSWORD', '2021/11/21'),
                'charset': 'utf8mb4'
            }
            self.create_database(mysql_config)
            mysql_config['db'] = settings.get('MYSQL_DATABASE', 'weibo')
            self.db = pymysql.connect(**mysql_config)
            self.cursor = self.db.cursor()
            self.create_table()
        except ImportError:
            spider.pymysql_error = True
        except pymysql.OperationalError:
            spider.mysql_error = True

    def process_item(self, item, spider):
        data = dict(item['weibo'])
        not_keys = ['bid','article_url','location','at_users','source','pics','video_url','retweet_id']
        for not_key in not_keys:
            data.pop(not_key)
        keys = ', '.join(data.keys())
        print(keys)
        values = ', '.join(['%s'] * len(data))
        print(values)
        sql = """INSERT INTO {database}.{table}({keys}) VALUES ({values}) ON
                     DUPLICATE KEY UPDATE""".format(database='weibo',
                                                    table='weibo',
                                                    keys=keys,
                                                    values=values)
        print(sql)
        update = ','.join([" {key} = {key}".format(key=key) for key in data])
        print(update)
        sql += update
        print(sql)
        try:
            self.cursor.execute(sql, tuple(data.values()))
            self.db.commit()
        except Exception:
            self.db.rollback()
        return item

    def close_spider(self, spider):
        try:
            self.db.close()
        except Exception:
            pass


class DuplicatesPipeline(object):
    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['weibo']['id'] in self.ids_seen:
            raise DropItem("过滤重复微博: %s" % item)
        else:
            self.ids_seen.add(item['weibo']['id'])
            return item
