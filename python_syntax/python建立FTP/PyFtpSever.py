from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer


authorizer = DummyAuthorizer()
authorizer.add_user("user", "12345", "/home/dennis/Documents", perm="elradfmwMT")
handler = FTPHandler
handler.authorizer = authorizer
server = FTPServer(("0.0.0.0", 9999), handler)
server.serve_forever()