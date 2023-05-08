# -*- coding:utf-8 -*-
# coding=gbk
import json
import os
import time

	# a = {
	# 	"id": "2333",
	# 	"stationId": 2,
	# 	"outStockId": "233",
	# 	"inStockDate": "2018-01-01 00:00:00",
	# 	"inStockBy": "王小二",
	# 	"remark": "233333333",
	# 	"bloodBags": [{
	# 		"bloodBagId": "900281470682201D6511000",
	# 		"donationId": "900281470682200",
	# 		"bloodProduct": "D6511000",
	# 		"bloodType": 13,
	# 		"aboGroup": 1,
	# 		"rhGroup": 1,
	# 		"donationDate": "2018-08-10 15:45:00",
	# 		"productionDate": "2018-08-10 10:04:32",
	# 		"expirationDate": "2018-08-10 15:45:00",
	# 		"volume": 225.0,
	# 		"unit": "ml",
	# 		"bagId": "900281470682200"
	# 	}]
	# }
def inStock():
	path1 = input("请输入文件的绝对路径如：C:\\Users\\Administrator\\Desktop\\ceshi.txt：")

	path =path1
	try:
	# 打开文件
		f=open(path,encoding='utf-8')
		# 创建空列表
		text=[]
		try:
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
			# print(text)
			# print(len(text))
			j=0
			a = ""
			for j in range(0,len(text)):
				b = text[j]
				# print(b)
				b = str(b)
				a = str(a)
				a = a+b
			# print(a)
			try:
				a = eval(a)
				# print(b)
				# print(type(b))

				key = a.keys()
				# print(type(key))
				# print(key)
				try:
					id = a["id"]
					if id is None or id == "":
						print("id值为空")
				except:
					print("缺少id字段")


				try:
					stationId = a["stationId"]
					stationId = str(stationId)
					stationId = stationId.isdigit()
					if stationId != True:
						print("袋血stationId数据格式不正确")
				except:
					print("缺少stationId字段")


				try:
					outStockId = a["outStockId"]
					outStockId = outStockId.isdigit()
					if outStockId != True:
						print("袋血outStockId数据格式不正确")
				except:
					print("缺少outStockId字段")

				try:
					inStockDate = a["inStockDate"]
					date_format = "%Y-%m-%d %H:%M:%S"
					try:
						time.strptime(inStockDate, date_format)
					# print("袋血donationDate数据格式不正确")
					except ValueError:
						print("inStockDate数据格式不正确")
				except:
					print("缺少inStockDate字段")

				try:
					inStockBy = a["inStockBy"]
					if inStockBy is None or inStockBy == "":
						print("inStockBy值为空")
				except:
					print("缺少inStockBy字段")


				try:
					remark = a["remark"]
					if remark is None or remark == "":
						print("remark值为空")
				except:
					print("缺少remark字段")




				bloodBags = a["bloodBags"]

				try:
					for i in range(0,len(bloodBags)):
						c = bloodBags[i]
						c = dict(c)

						try:
							bloodBagId = c["bloodBagId"]
							if len(bloodBagId) != 23:
								print("第%s袋bloodBagId错误" % i)
								print(c)
						except:
							print("缺少bloodBagId字段")
							print(c)


						try:
							donationId = c["donationId"]
							if len(donationId) != 15:
								print("第%s袋donationId不正确" % i)
								print(c)
						except:
							print("缺少donationId字段")
							print(c)


						try:
							bloodProduct = c["bloodProduct"]
							if len(bloodProduct) !=8:
								print("第%s袋血袋bloodProduct错误" % i)
								print(c)
						except:
							print("缺少bloodProduct字段")
							print(c)


						try:
							bloodType = c["bloodType"]
							bloodType=str(bloodType)
							bloodType = bloodType.isdigit()
							if bloodType !=True:
								print("第%s袋血bloodType数据格式不正确" % i)
								print(c)
						except:
							print("缺少bloodType字段")
							print(c)



						try:
							aboGroup = c["aboGroup"]
							aboGroup = str(aboGroup)
							aboGroup = aboGroup.isdigit()
							if aboGroup !=True:
								print("第%s袋血aboGroup数据格式不正确" % i)
								print(c)
						except:
							print("缺少aboGroup字段")
							print(c)


						try:
							rhGroup = c["rhGroup"]
							rhGroup = str(rhGroup)
							rhGroup = rhGroup.isdigit()
							if rhGroup !=True:
								print("第%s袋血rhGroup数据格式不正确"% i)
								print(c)
						except:
							print("缺少rhGroup字段")
							print(c)



						try:
							donationDate = c["donationDate"]
							date_format = "%Y-%m-%d %H:%M:%S"
							try:
								time.strptime(donationDate, date_format)
								# print("第%s袋血donationDate数据格式不正确"% i)
							except ValueError:
								print("第%s袋血donationDate数据格式不正确e"% i)
								print(c)
						except:
							print("缺少donationDate字段")
							print(c)



						try:
							productionDate = c["productionDate"]
							date_format = "%Y-%m-%d %H:%M:%S"
							try:
								time.strptime(productionDate, date_format)
								# print("第%s袋血productionDate数据格式不正确"% i)
							except ValueError:
								print("第%s袋血productionDate数据格式不正确"% i)
								print(c)
						except:
							print("缺少productionDate字段")
							print(c)



						try:
							donexpirationDateationId = c["expirationDate"]
							donexpirationDateationId = str(donexpirationDateationId)
							date_format = "%Y-%m-%d %H:%M:%S"
							try:
								time.strptime(donexpirationDateationId, date_format)
								# print("第%s袋血donexpirationDateationId数据格式不正确"% i)
							except ValueError:
								print("i第%s袋血donexpirationDateationId数据格式不正确"% i)
								print(c)
						except:
							print("缺少donexpirationDateationId字段")
							print(c)



						try:
							volume = c["volume"]
							volume = str(volume)
							if volume.count(".") != 1 and not volume.startswith(".") and  volume.endswith("."):
								print("第%s袋血volume格式错误"% i)
								print(c)
						except:
							print("缺少volume字段")
							print(c)


						try:
							bagId = c["bagId"]
							if len(bagId) != 15:
								print("第%sbagId不正确" % i)
								print(c)
						except:
							# print("缺少bagId字段")
							# print(c)
							print( )



						try:
							unit = c["unit"]
							if unit not in ("ml","ML","Ml","mL","单位","治疗","u","U"):
								print("第%s袋血unit格式错误"% i)
								print(c)
						except:
							print("缺少unit字段")
							print(c)
						i = i + 1
						print("第%s袋血----------------------------------------------------------------------------------------------------------------->" % i)
				except:
					print("缺少bloodBags字段信息")
			except:
				print("数据格式错误，请检查是否少标点或使用了中文标点符号")
		except:
			print("您选择的text文件参数与您选择的接口不符，请核对文件内容是否是该接口的参数")
	except:
		print("您输入的text地址错误")


	os.system("pause")



