import traceback
import pymysql
import sys
import redis
import configparser
import json
from collections import OrderedDict


class Analyse:
    config = ''
    db_cursor = ''

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        try:
            db_host = self.config.get("db", "host")
            db_port = int(self.config.get("db", "port"))
            db_user = self.config.get("db", "user")
            db_pass = self.config.get("db", "password")
            db_db = self.config.get("db", "db")
            db_charset = self.config.get("db", "charset")
            self.db = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_db,
                                      charset=db_charset)
            self.db_cursor = self.db.cursor()
        except:
            print("请检查数据库配置")
            sys.exit()

        # 初始化redis连接
        try:
            redis_host = self.config.get("redis", "host")
            redis_port = self.config.get("redis", "port")
            self.redis_con = redis.Redis(host=redis_host, port=redis_port, db=0)
        except Exception as err:
            print("请安装redis或检查redis连接配置")
            sys.exit()

    # 获取用户总数
    def get_user_num(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("user_num").decode('utf-8'))
        except:
            result = None
        if not result:
            sql = '''
                SELECT COUNT(*),(SELECT update_time FROM user ORDER BY update_time DESC LIMIT 1 ) FROM user
            '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取用户数量失败")
                return None
            data = self.db_cursor.fetchone()
            result = {'num': data[0], 'update_time': data[1].strftime("%Y-%m-%d %H:%M:%S")}

            # 保存到redis
            self.redis_con.set("user_num", result, 9600)

            return result
        else:
            return result

    # 获取用户性别数量等数据
    def get_sex(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("sex_num").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                SELECT
                (SELECT COUNT(*) FROM user WHERE gender = 1) AS male,
                (SELECT COUNT(*) FROM user WHERE gender = 2) AS female,
                (SELECT COUNT(*) FROM user WHERE gender = 3) AS other,
                (SELECT COUNT(*) FROM user) AS total
            '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取性别比例失败")
                return None
            data = self.db_cursor.fetchone()
            result = OrderedDict([('男性', data[0]), ('女性', data[1]), ('未知', data[2])])

            # 保存到redis
            self.redis_con.set("sex_num", result, 9600)

            return result
        else:
            return result

    # 学校人数统计
    def get_school_count(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("school_count").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                 SELECT school,COUNT(*) FROM user
                 WHERE school NOT LIKE '%本科%' AND LENGTH(school) > 8
                 GROUP BY school
                 ORDER BY COUNT(*) DESC
                 LIMIT 10
             '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取学校统计失败")
                return None
            data = self.db_cursor.fetchall()
            result = OrderedDict()
            for row in data:
                result[row[0]] = row[1]

            # 保存到redis
            self.redis_con.set("school_count", result, 9600)

            return result
        else:
            return result

    # 行业统计
    def get_trade_count(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("trade_count").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                 SELECT trade,COUNT(*) FROM user
                 WHERE trade <> ''
                 GROUP BY trade
                 ORDER BY COUNT(*) DESC
                 LIMIT 10
             '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取行业比例失败")
                return None
            data = self.db_cursor.fetchall()
            result = OrderedDict()
            for row in data:
                result[row[0]] = row[1]

            # 保存到redis
            self.redis_con.set("trade_count", result, 9600)

            return result
        else:
            return result

    # 地域统计
    def get_location_count(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("location_count").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                 SELECT location,COUNT(*) FROM user
                 WHERE location <> ''
                 GROUP BY location
                 ORDER BY COUNT(*) DESC
                 LIMIT 10
             '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取位置分布失败")
                return None
            data = self.db_cursor.fetchall()
            result = OrderedDict()
            for row in data:
                result[row[0]] = row[1]

            # 保存到redis
            self.redis_con.set("location_count", result, 9600)

            return result
        else:
            return result

    # 公司统计
    def get_company_count(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("company_count").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                 SELECT company,COUNT(*) FROM user
                 WHERE company <> '' AND company NOT LIKE "%学生%" AND company <> '无' AND company <> '自由职业' AND company <> '待业'
                 GROUP BY company
                 ORDER BY COUNT(*) DESC
                 LIMIT 10
             '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取公司统计失败")
                return None
            data = self.db_cursor.fetchall()
            result = OrderedDict()
            for row in data:
                result[row[0]] = row[1]

            # 保存到redis
            self.redis_con.set("company_count", result, 9600)

            return result
        else:
            return result

    # 获取赞同数统计数据
    def get_agree_count(self):
        # 检查是否缓存
        try:
            result = json.loads(self.redis_con.get("agree_count").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                SELECT
                (SELECT COUNT(*) FROM user WHERE agree_num >= 1000000) AS zero,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 100000 AND agree_num < 1000000) AS first,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 50000 AND agree_num <100000) AS second,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 10000 AND agree_num <50000) AS third,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 5000 AND agree_num <10000) AS fourth,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 1000 AND agree_num <5000) AS fifth,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 500 AND agree_num <1000) AS sixth,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 100 AND agree_num <500) AS seventh,
                (SELECT COUNT(*) FROM user WHERE agree_num >= 0 AND agree_num <100) AS eighth
             '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取赞同数统计失败")
                return None
            data = self.db_cursor.fetchone()

            result = OrderedDict(
                [('>1000000', data[0]),
                 ('100000-1000000', data[1]),
                 ('50000-100000', data[2]),
                 ('10000-50000', data[3]),
                 ('5000-10000', data[4]),
                 ('1000-5000', data[5]),
                 ('500-100', data[6]),
                 ('100-500', data[7]),
                 #('0-100', data[8])
                 ])

            # 保存到redis
            self.redis_con.set("agree_count", result, 9600)

            return result
        else:
            return result

    # 获取粉丝数统计数据
    def get_follower_count(self):
        # 检查是否缓存
        try:
            result = str(self.redis_con.get("follower_count").decode('utf-8'), object_pairs_hook=OrderedDict)
        except:
            result = None
        if not result:
            sql = '''
                SELECT
                (SELECT COUNT(*) FROM user WHERE follower >= 1000000) AS zero,
                (SELECT COUNT(*) FROM user WHERE follower >= 100000 AND follower < 1000000) AS first,
                (SELECT COUNT(*) FROM user WHERE follower >= 50000 AND follower <100000) AS second,
                (SELECT COUNT(*) FROM user WHERE follower >= 10000 AND follower <50000) AS third,
                (SELECT COUNT(*) FROM user WHERE follower >= 5000 AND follower <10000) AS fourth,
                (SELECT COUNT(*) FROM user WHERE follower >= 1000 AND follower <5000) AS fifth,
                (SELECT COUNT(*) FROM user WHERE follower >= 500 AND follower <1000) AS sixth,
                (SELECT COUNT(*) FROM user WHERE follower >= 100 AND follower <500) AS seventh,
                (SELECT COUNT(*) FROM user WHERE follower >= 0 AND follower <100) AS eighth
             '''
            try:
                self.db_cursor.execute(sql)
            except Exception as err:
                traceback.print_exc()
                print(err)
                print("获取粉丝数统计失败")
                return None
            data = self.db_cursor.fetchone()
            result = OrderedDict(
                [('>1000000', data[0]),
                 ('100000-1000000', data[1]),
                 ('50000-100000', data[2]),
                 ('10000-50000', data[3]),
                 ('5000-10000', data[4]),
                 ('1000-5000', data[5]),
                 ('500-100', data[6]),
                 ('100-500', data[7]),
                 #('0-100', data[8])
                 ])

            # 保存到redis
            self.redis_con.set("follower_count", result, 9600)

            return result
        else:
            return result

    def __del__(self):
        self.db_cursor.close()
        self.db.commit()
        self.db.close()
