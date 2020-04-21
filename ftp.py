from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
 
# 实例化DummyAuthorizer来创建ftp用户
authorizer = DummyAuthorizer()
# 参数：用户名，密码，目录，权限
authorizer.add_user('user1', '12345', '/media/mamba/Data/test/pyftpdlib_FTP', perm='elradfmwMT')
authorizer.add_user('user2', '12345', '/media/mamba/Data/test/pyftpdlib_FTP', perm='elr')
# 匿名登录
# authorizer.add_anonymous('/home/nobody')
handler = FTPHandler
handler.authorizer = authorizer
# 参数：IP，端口，handler
server = FTPServer(('192.168.24.145', 1234), handler)
server.serve_forever()