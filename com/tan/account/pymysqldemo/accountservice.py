from pymysqldemo import dbtool
import logging



class AccountService():


  def query_country_name(self):
    sql_str = ("SELECT * FROM t_user")
    logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                        # a是追加模式，默认如果不写的话，就是追加模式
                        format=
                        '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                        # 日志格式
                        )

    logging.info(sql_str)

    con = dbtool.connect_wxremit_db()
    cur = con.cursor()
    cur.execute(sql_str)
    rows = cur.fetchall()
    cur.close()
    con.close()
    print( len(rows))
    assert len(rows) == 5, 'Fatal error: country_code does not exists!'
    return rows[0][0]


accountService=AccountService();
logging.info(accountService.query_country_name())