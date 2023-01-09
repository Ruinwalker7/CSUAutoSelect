#!
# coding=utf-8
import re
import sys
import time
import requests
import base64
import configparser

file = 'config.ini'
con = configparser.ConfigParser()
con.read(file, encoding='utf-8')

item = con.items('config')
item = dict(item)

global username, password

Img_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/verifycode.servlet'
LOGIN_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xk/LoginToXk'
MAIN_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/framework/xsMain.jsp'

# REQUEST_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/ggxxkxkOper'
REQUEST_URL = 'http://csujwc.its.csu.edu.cn/jsxsd/xsxkkc/bxqjhxkOper'

session = requests.Session()
respond = session.get(Img_URL)

with open('code.jpg', 'wb') as file:
	file.write(respond.content)
	file.close

respond = session.get(LOGIN_URL)
qrcode = input("输入验证码：")


def login():
	username = item['username']
	password = item['password']
	s1 = base64.b64encode(username.encode())
	s2 = base64.b64encode(password.encode())
	
	data = {'encoded': s1.decode() + '%%%' + s2.decode(), 'RANDOMCODE': qrcode}
	respond = session.post(LOGIN_URL, data)
	respond = session.get(MAIN_URL)
	return respond


respond = login()

if respond.status_code != requests.codes.ok:
	print('学号或密码或验证码错误，请退出修改配置重启')
	sys.exit()
else:
	print('成功登录教务系统')

num = int(item['num'])

list = []

for i in range(1, num + 1):
	id = item['id' + str(i)]
	list.append('202220232' + id)

while True:
	respond = session.get('http://csujwc.its.csu.edu.cn/jsxsd/xsxk/xklc_list')
	key = re.findall('href="(.+?)" target="blank">进入选课', respond.text)
	if len(key) >= 1:
		break
	print('寻找选课列表中')
	time.sleep(1)

respond = session.get('http://csujwc.its.csu.edu.cn' + key[0])

print('成功进入选课页面')


def work(id, num):
	# print(REQUEST_URL + '?jx0404id=' + id +'&xkzy=&trjf=')
	respond = session.get(REQUEST_URL + '?jx0404id=' + id +'&xkzy=&trjf=')
	if re.search('true', respond.text):
		print("成功抢到第 %d 门课", i)
		return True
	if re.search('null', respond.text):
		print("没有该 ID 所对应的课程")
	else:
		print(re.search('"选课失败：(.+)"', respond.text))
	return True


while True:
	for i in range(0, num):
		print('第 {} 门课选课开始，课程 ID: {}'.format(i + 1, list[i]))
		work(list[i], i)
		time.sleep(1)

input('输入回车以结束程序')
