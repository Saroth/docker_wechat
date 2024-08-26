#!/usr/bin/python
# 此脚本仅用于连通测试

import atexit
import ctypes
import os
from queue import Queue
import pynng
import logging
from time import sleep
import datetime
from wcferry import Wcf

at_list = 'filehelper'	# 可改为自己的wxid用于测试

class WcfCustom(Wcf):
	def __init__(self, host: str|None = None, port: int = 10086, debug: bool = True, block: bool = True) -> None:
		self._local_mode = False
		self._is_running = False
		self._is_receiving_msg = False
		self._wcf_root = os.path.abspath(os.path.dirname(__file__))
		self._dl_path = f"{self._wcf_root}/.dl"
		os.makedirs(self._dl_path, exist_ok=True)
		self.LOG = logging.getLogger("WCF")
		self.LOG.setLevel(logging.DEBUG)
		self.LOG.addHandler(logging.StreamHandler())
		self.LOG.info(f"wcferry version: 39.2.4.0-custom")
		self.LOG.info(f"wcf_root: {self._wcf_root}")
		self.port = port
		self.host = host
		self.sdk = None
		if host is None:
			self._local_mode = True
			self.host = "127.0.0.1"
			self.sdk = ctypes.cdll.LoadLibrary(f"{self._wcf_root}/sdk.dll")
			if self.sdk.WxInitSDK(debug, port) != 0:
				self.LOG.error("初始化失败！")
				os._exit(-1)

		self.cmd_url = f"tcp://{self.host}:{self.port}"

		# 连接 RPC
		self.cmd_socket = pynng.Pair1()  # Client --> Server，发送消息
		self.cmd_socket.send_timeout = 5000  # 发送 5 秒超时
		self.cmd_socket.recv_timeout = 5000  # 接收 5 秒超时
		try:
			self.cmd_socket.dial(self.cmd_url, block=True)
		except Exception as e:
			self.LOG.error(f"连接失败: {e}")
			os._exit(-2)

		self.msg_socket = pynng.Pair1()  # Server --> Client，接收消息
		self.msg_socket.send_timeout = 5000  # 发送 5 秒超时
		self.msg_socket.recv_timeout = 5000  # 接收 5 秒超时
		self.msg_url = self.cmd_url.replace(str(self.port), str(self.port + 1))

		atexit.register(self.cleanup)  # 退出的时候停止消息接收，防止资源占用

		self._is_running = True
		self.contacts = []
		self.msgQ = Queue()
		self._SQL_TYPES = {1: int, 2: float, 3: lambda x: x.decode("utf-8"), 4: bytes, 5: lambda x: None}
		self.self_wxid = ""
		if block:
			self.LOG.info("等待微信登录...")
			while not self.is_login():	 # 等待微信登录成功
				sleep(1)
			self.self_wxid = self.get_self_wxid()



def main():
	wcf = Wcf(host = '127.0.0.1', port = 18001)
	#  wcf = WcfCustom()
	wcf.send_text(f'当前时间: {datetime.datetime.now()}', at_list)
	print(f'My wxid is {wcf.get_self_wxid()}, 消息已发送')

if __name__ == '__main__':
	main()

