#!/usr/bin/python
# 此脚本仅用于连通测试

import datetime
from wcferry import Wcf

at_list = 'filehelper'	# 可改为自己的wxid用于测试

def main():
	wcf = Wcf(host = '127.0.0.1', port = 18001)
	wcf.send_text(f'当前时间: {datetime.datetime.now()}', at_list)
	print(f'My wxid is {wcf.get_self_wxid()}, 消息已发送')

if __name__ == '__main__':
	main()

