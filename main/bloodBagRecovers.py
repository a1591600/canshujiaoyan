# -*- coding:utf-8 -*-
# coding=gbk
import json
import time
import os

def	bloodBagRecovers():
	path1 = input("请输入文件的绝对路径如：C:\\Users\\Administrator\\Desktop\\ceshi.txt：")

	path =path1
	# 打开文件
	f=open(path,encoding='utf-8')
	# 创建空列表
	text=[]
	# 读取全部内容 ，并以列表方式返回
	lines = f.readlines()
	for line in lines:
		# 如果读到空行，就跳过
		if line.isspace():
			continue
		else:
			# 去除文本中的换行等等，可以追加其他操作
			line = line.replace("\n","")
			line = line.replace("\t","")
			# 处理完成后的行，追加到列表中
			text.append(line)
	print(text)
	# print(len(text))
	j=0
	a = ""
	for j in range(0,len(text)):
		b = text[j]
		# print(b)
		b = str(b)
		a = str(a)
		a = a+b
	print(a)
	bloodBagRecovers()
	# a = list(a)
	# print(type(a))
	# a=a[0]
	# print(a)

	# print(len(a))

	# a = eval(a)
	# print(b)
	# print(type(b))


	#
	# a = [{
	# "id": "BF-20820210303-00001",
	# "recoveryTime": "2021-03-03 09:",
	# "operator": "zsf",
	# "handover": "护士小松",
	# "recoverDetails": [{
	# "bloodBagId":"900191932401155D2240600"
	# }]
	# }]
	#
	# for i in range(0,len(a)):
	# 	b = a[i]
	# 	# key = a.keys()
	# 	# print(type(key))
	# 	# print(b)
	# 	try:
	# 		id = b["id"]
	# 		if id is None or id == "":
	# 			print("id值为空")
	# 	except:
	# 		print("缺少id字段")
	#
	#
	#
	# 	try:
	# 		recoveryTime = b["recoveryTime"]
	# 		date_format = "%Y-%m-%d %H:%M:%S"
	# 		try:
	# 			time.strptime(recoveryTime, date_format)
	# 		# print("第%s袋血recoveryTime数据格式正确"% i)
	# 		except ValueError:
	# 			print("recoveryTime数据格式不正确")
	# 	except:
	# 		print("缺少recoveryTime字段")
	#
	#
	#
	# 	try:
	# 		operator = b["operator"]
	# 		if operator is None or operator == "":
	# 			print("operator值为空")
	# 	except:
	# 		print("缺少operator字段")
	#
	#
	#
	# 	try:
	# 		handover = b["handover"]
	# 		if handover is None or handover == "":
	# 			print("handover值为空")
	# 	except:
	# 		print("缺少handover字段")
	#
	#
	# 	try:
	# 		recoverDetails = b["recoverDetails"]
	# 		# print(b)
	# 		# print(recoverDetails)
	# 		if recoverDetails is None or recoverDetails == "":
	# 			print("recoverDetails值为空")
	# 		else:
	# 			for j in range(len(recoverDetails)):
	# 				c = recoverDetails[j]
	# 				c = dict(c)
	# 				try:
	# 					bloodBagId = c["bloodBagId"]
	# 					if len(bloodBagId) != 23:
	# 						print("第%s袋bloodBagId错误" % i)
	# 						print(c)
	# 				except:
	# 					print("缺少bloodBagId字段")
	# 					print(c)
	# 	except:
	# 		print("缺少recoverDetails字段")
	# os.system("pause")
