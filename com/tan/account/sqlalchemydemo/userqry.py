# 导入:
from userservice import User
from userservice import DBSession


class UserQryService():

     def qryAllUser(self):
         # 创建Session:
         session = DBSession()
         # 创建Query查询，filter是where条件，最后调用one()返回唯一行，如果调用all()则返回所有行:
         # user = session.query(User).filter(User.id == '5').one()
         users = session.query(User).all();
         # 打印类型和对象的name属性:
         # print('type:', type(user))
         # print('user_name:', user.user_name)
         # 关闭Session:
         session.close()
         return users;






