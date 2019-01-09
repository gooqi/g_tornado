#coding:utf-8
from handlers.index import MainHandler
from handlers.upload import UploadHandler
from handlers.websocket import WebSocketHandler
from handlers.login import LoginHandler
from handlers.room import RoomHandler

urls = [
(r'/', MainHandler),
(r'/upload',UploadHandler),
(r'/websocket', WebSocketHandler),
(r'/onLogin', LoginHandler),
(r'/room', RoomHandler),
]
