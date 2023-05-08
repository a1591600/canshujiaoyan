# -*- coding:utf-8 -*-
# coding=gbk
import json
import re
import time
import os

import re
def poOutClinic():
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
				print(b)
				b = str(b)
				a = str(a)
				a = a+b
			# print(a)
			try:
				a = eval(a)
				# print(b)
				# # print(type(b))
				# a = {
				# 	"id": "2333",
				# 	"applicationId": "233333",
				# 	"outClinicDate": "2018-01-01 00:00:00",
				# 	"outClinicBy": "王小二",
				# 	"auditDate": "2018-01-01 00:00:00",
				# 	"auditBy": "王大二",
				# 	"remark": "233333333",
				# 	"patient": {
				# 		"id": "2333333333333",
				# 		"name": "张三",
				# 		"sex": "MALE",
				# 		"age": "18Y3M2D",
				# 		"aboGroup": 1,
				# 		"rhGroup": 1,
				# 		"idCardType": 1,
				# 		"department": "100",
				# 		"area": "华南大区",
				# 		"bedNo": "405",
				# 		"diagnosis": "情况良好",
				# 		"everPregnancy": 1,
				# 		"everChildbearing": 1,
				# 		"everTranfusion": 1,
				# 		"everReaction": 1,
				# 		"iDCardNo":"845646465465456465456465"
				# 	},
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
				# "bagId": "900281470682200"
				# 	}]
				# }
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
					applicationId = a["applicationId"]
					if applicationId is None or applicationId == "":
						print("applicationId值为空")
				except:
					print("applicationId字段")


				try:
					outClinicDate = a["outClinicDate"]
					date_format = "%Y-%m-%d %H:%M:%S"
					try:
						time.strptime(outClinicDate, date_format)
					# print("第%s袋血outClinicDate数据格式不正确"% i)
					except ValueError:
						print("outClinicDate数据格式不正确")
				except:
					print("缺少outClinicDate字段")



				try:
					outClinicBy = a["outClinicBy"]
					if outClinicBy is None or outClinicBy == "":
						print("outClinicBy值为空")
				except:
					print("缺少outClinicBy字段")

				try:
					auditDate = a["auditDate"]
					date_format = "%Y-%m-%d %H:%M:%S"
					try:
						time.strptime(auditDate, date_format)
					# print("第%s袋血auditDate数据格式不正确"% i)
					except ValueError:
						print("auditDate数据格式不正确")
				except:
					print("缺少auditDate字段")


				try:
					auditBy = a["auditBy"]
					if auditBy is None or auditBy == "":
						print("auditBy值为空")
				except:
					print("缺少auditBy字段")

				try:
					remark = a["remark"]
					if remark is None or remark == "":
						print("remark值为空")
				except:
					print("缺少remark字段")










				# print(patient)
				try:
					patient = a["patient"]
					# print(patient)
					# print(type(patient))
					# print(len(patient))
					if patient is None or patient == "":
						print("patient值为空")
					else:
						# for i in range(0,len(patient)):
						# c = patient[i]
						# print(c)
						# c = dict(c)
						try:
							id = patient["id"]
							if id is None or id == "":
								print("id值为空")
						except:
							print("缺少id字段")

						try:
							name = patient["name"]
							if name is None or name == "":
								print("name值为空")
						except:
							print("缺少name字段")

						try:
							sex = patient["sex"]
							if sex not in ("MALE","WOMALE"):
								print("sex值错误")
						except:
							print("缺少sex字段")


						try:
							age = patient["age"]
							if age is None or age == "":
								print("age值错误")
							else:
								age = re.findall("\d\d[A-Z]\d[A-Z]\d[A-Z]", age)
								try:
									age = age[0]
									# print(age)
									# print(len(age))
									if len(age) !=7:
										print("age格式错误")
								except:
									print("age格式错误")
						except:
							print("缺少age字段")


						try:
							aboGroup = patient["aboGroup"]
							aboGroup = str(aboGroup)
							aboGroup = aboGroup.isdigit()
							if aboGroup != True:
								print("袋血aboGroup数据格式不正确")
						except:
							print("缺少aboGroup字段")


						try:
							rhGroup = patient["rhGroup"]
							rhGroup = str(rhGroup)
							rhGroup = rhGroup.isdigit()
							if rhGroup != True:
								print("袋血rhGroup数据格式不正确")
						except:
							print("缺少rhGroup字段")


						try:
							idCardType = patient["idCardType"]
							idCardType = str(idCardType)
							idCardType = idCardType.isdigit()
							if idCardType != True:
								print("袋血idCardType数据格式不正确")
						except:
							print("缺少idCardType字段")

						try:
							department = patient["department"]
							department = str(department)
							department = department.isdigit()
							if department != True:
								print("袋血department数据格式不正确")
						except:
							print("缺少department字段")

						try:
							area = patient["area"]
							area = str(area)
							if area is None or area == " ":
								print("袋血area数据格式不正确")
						except:
							print("缺少area字段")


						try:
							bedNo = patient["bedNo"]
							bedNo = str(bedNo)
							if bedNo is None or bedNo == " ":
								print("袋血bedNo数据格式不正确")
						except:
							print("缺少bedNo字段")



						try:
							diagnosis = patient["diagnosis"]
							# diagnosis = str(diagnosis)
							if diagnosis is None or diagnosis == " ":
								print("袋血diagnosis数据格式不正确")
						except:
							print("缺少diagnosis字段")

						try:
							everPregnancy = patient["everPregnancy"]
							if everPregnancy not in (0,1):
								print("袋血everPregnancy数据格式不正确")
						except:
							print("缺少everPregnancy字段")


						try:
							everChildbearing = patient["everChildbearing"]
							if everChildbearing not in (0,1):
								print("袋血everChildbearing数据格式不正确")
						except:
							print("缺少everChildbearing字段")


						try:
							everTranfusion = patient["everTranfusion"]
							if everTranfusion not in (0,1):
								print("袋血everTranfusion数据格式不正确")
						except:
							print("缺少everTranfusion字段")


						try:
							everReaction = patient["everReaction"]
							if everReaction not in (0,1):
								print("袋血everReaction数据格式不正确")
						except:
							print("缺少everReaction字段")


						try:
							iDCardNo = patient["iDCardNo"]
							iDCardNo = str(iDCardNo)
							if iDCardNo is None or iDCardNo == "":
								print("袋血diagnosis数据格式不正确")
						except:
							print("缺少diagnosis字段")
				except:
					print("缺少patient字段")

				# ----------------------------------------------------------------------------------------------------------------------
				try:
					bloodBags = a["bloodBags"]
					# print(bloodTest)
					# print(type(bloodTest))
					# print(len(bloodTest))
					if bloodBags is None or bloodBags == "":
						print("bloodBags值为空")

					else:
						# for i in range(0,len(bloodTest)):
							# c = patient[i]
							# print(c)
							# c = dict(c)
						for i in range(0, len(bloodBags)):
							c = bloodBags[i]
							c = dict(c)
							try:
								bloodBagId = c["bloodBagId"]
								if len(bloodBagId) != 23:
									print("第%s袋血袋码错误" % i)
									print(c)
							except:
								print("缺少bloodBagId字段")
								print(c)

							try:
								donationId = c["donationId"]
								if len(donationId) != 15:
									print("第%s袋血袋号不正确" % i)
									print(c)
							except:
								print("缺少donationId字段")
								print(c)

							try:
								bloodProduct = c["bloodProduct"]
								if len(bloodProduct) != 8:
									print("第%s袋血袋产品码错误" % i)
									print(c)
							except:
								print("缺少bloodProduct字段")
								print(c)

							try:
								bloodType = c["bloodType"]
								bloodType = str(bloodType)
								bloodType = bloodType.isdigit()
								if bloodType != True:
									print("第%s袋血bloodType数据格式不正确" % i)
									print(c)
							except:
								print("缺少bloodType字段")
								print(c)

							try:
								aboGroup = c["aboGroup"]
								aboGroup = str(aboGroup)
								aboGroup = aboGroup.isdigit()
								if aboGroup != True:
									print("第%s袋血bloodType数据格式不正确" % i)
									print(c)
							except:
								print("缺少aboGroup字段")
								print(c)

							try:
								rhGroup = c["rhGroup"]
								rhGroup = str(rhGroup)
								rhGroup = rhGroup.isdigit()
								if rhGroup != True:
									print("第%s袋血rhGroup数据格式不正确" % i)
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
									print("第%s袋血donationDate数据格式不正确e" % i)
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
									print("第%s袋血productionDate数据格式不正确" % i)
									print(c)
							except:
								print("缺少productionDate字段")
								print(c)

							try:
								expirationDateationId = c["expirationDate"]
								expirationDateationId = str(expirationDateationId)
								date_format = "%Y-%m-%d %H:%M:%S"
								try:
									time.strptime(expirationDateationId, date_format)
								# print("第%s袋血expirationDateationId数据格式不正确"% i)
								except ValueError:
									print("i第%s袋血expirationDateationId数据格式不正确" % i)
									print(c)
							except:
								print("缺少expirationDateationId字段")
								print(c)

							try:
								volume = c["volume"]
								volume = str(volume)
								if volume.count(".") != 1 and not volume.startswith(".") and volume.endswith("."):
									print("第%s袋血volume格式错误" % i)
									print(c)
							except:
								print("缺少volume字段")
								print(c)

							try:
								bagId = c["bagId"]
								if len(bagId) != 15:
									print("第%s袋bagId不正确" % i)
									print(c)
							except:
								# print("缺少bagId字段")
								# print(c)
								print( )
							try:
								unit = c["unit"]

								if unit not in ("ml","ML","Ml","mL","单位","治疗","u","U"):
									print("第%s袋血单位格式错误" % i)
									print(c)
							except:
								print("缺少unit字段")
								print(c)
							i = i + 1
							print("第%s袋血----------------------------------------------------------------------------------------------------------------->" % i)



				except:
					print("缺少bloodBags字段")
			except:
				print("数据格式错误，请检查是否少标点或使用了中文标点符号")
		except:
			print("您选择的text文件参数与您选择的接口不符，请核对文件内容是否是该接口的参数")
	except:
		print("您输入的text地址错误")

	os.system("pause")
