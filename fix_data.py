import pymysql
import configparser
import sys
import redis

config = configparser.ConfigParser()
config.read('config.ini')
try:
    db_host = config.get("db", "host")
    db_port = int(config.get("db", "port"))
    db_user = config.get("db", "user")
    db_pass = config.get("db", "password")
    db_db = config.get("db", "db")
    db_charset = config.get("db", "charset")
    db = pymysql.connect(host=db_host, port=db_port, user=db_user, passwd=db_pass, db=db_db,
                              charset=db_charset)
    db_cursor = db.cursor()
except:
    print("请检查数据库配置")
    sys.exit()

# 初始化redis连接
try:
    redis_host = config.get("redis", "host")
    redis_port = config.get("redis", "port")
    redis_con = redis.Redis(host=redis_host, port=redis_port, db=0)
except Exception as err:
    print("请安装redis或检查redis连接配置")
    sys.exit()


# 查询部分
sql = '''
    UPDATE user SET location=REPLACE(location,'市','');
    UPDATE user SET school=REPLACE(school,'(SYSU）','');
    UPDATE user SET major=REPLACE(major,'专业','');
    UPDATE user SET major=REPLACE(major,'学生','') WHERE length(major)>4;
    UPDATE user SET company=REPLACE(company,'知乎公共领域编辑计划','知乎');
'''
db_cursor.execute(sql)
db.commit()


db_cursor.close()
db.close()
