	# -*- coding:utf-8 -*-
	# coding=gbk
import json
import time
import os

def poApplication():
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
				# # print(type(b))
				# a = {
				# 	"id": "2333",
				# 	"applyDate": "2018-01-01 00:00:00",
				# 	"applyBy": "王小二",
				# 	"approveDate": "2018-01-01 00:00:00",
				# 	"approveBy": "王大二",
				# 	"applyType": 1,
				# 	"planDate": "2018-01-01 00:00:00",
				# 	"transPurpose": 1,
				# 	"isConsentSigned": 1,
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
				# 	"bloodTest": {
				# 		"HB": 1.0,
				# 		"HCT": 1.0,
				# 		"PLT": 1.0,
				# 		"PT": 1.0,
				# 		"APTT": 1.0,
				# 		"FIB": 1.0,
				# 		"hbsag": "POSTIVE",
				# 		"antiHbs": "NEGATIVE",
				# 		"hbeag": "POSTIVE",
				# 		"antiHbe": "POSTIVE",
				# 		"antiHbc": "POSTIVE",
				# 		"antiHcv": "NEGATIVE",
				# 		"antiHiv": "NEGATIVE",
				# 		"syphilis": "NEGATIVE",
				# 		"INR": 1,
				# 		"ALT": "haha",
				# 		"TEG": 1.0,
				# 		"RPR":"NEGATIVE",
				# 		"TEGR":1.0,
				# 		"TEGMA":1.0,
				# 		"TEGA":1.0,
				# 		"TEGCI":1.0,
				# 		"HBVDNA":1.0,
				# 		"WBC":1.0,
				# 		"ALB":1.0,
				# 		"antiScreeningResult":"NO",
				# 		"rhTyping":"CCDEE",
				# 		"RPR":"NEGATIVE"
				# 	},
				# 	"applyBloods": [{
				# 		"bloodType": 13,
				# 		"aboGroup": 1,
				# 		"rhGroup": 1,
				# 		"applyVolume": 1.0,
				# 		"applyUnit": "ml"
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
					applyDate = a["applyDate"]
					date_format = "%Y-%m-%d %H:%M:%S"
					try:
						time.strptime(applyDate, date_format)
					# print("第%s袋血applyDate数据格式不正确"% i)
					except ValueError:
						print("applyDate数据格式不正确")
				except:
					print("缺少applyDate字段")



				try:
					applyBy = a["applyBy"]
					if applyBy is None or applyBy == "":
						print("applyBy值为空")
				except:
					print("缺少applyBy字段")

				try:
					approveDate = a["approveDate"]
					date_format = "%Y-%m-%d %H:%M:%S"
					try:
						time.strptime(approveDate, date_format)
					# print("第%s袋血approveDate数据格式不正确"% i)
					except ValueError:
						print("approveDate数据格式不正确")
				except:
					print("缺少approveDate字段")


				try:
					approveBy = a["approveBy"]
					if approveBy is None or approveBy == "":
						print("approveBy值为空")
				except:
					print("缺少approveBy字段")


				try:
					applyType = a["applyType"]
					applyType = str(applyType)
					applyType = applyType.isdigit()
					if applyType != True:
						print("袋血applyType数据格式不正确")
				except:
					print("缺少applyType字段")


				try:
					planDate = a["planDate"]
					date_format = "%Y-%m-%d %H:%M:%S"
					try:
						time.strptime(planDate, date_format)
					# print("第%s袋血planDate数据格式不正确"% i)
					except ValueError:
						print("planDatee数据格式不正确")
				except:
					print("缺少planDate字段")

				try:
					transPurpose = a["transPurpose"]
					transPurpose = str(transPurpose)
					transPurpose = transPurpose.isdigit()
					if transPurpose != True:
						print("袋血transPurpose数据格式不正确" )
				except:
					print("缺少transPurpose字段")


				try:
					isConsentSigned = a["isConsentSigned"]
					isConsentSigned = str(isConsentSigned)
					isConsentSigned = isConsentSigned.isdigit()
					if isConsentSigned != True:
						print("袋血isConsentSigned数据格式不正确" )
				except:
					print("缺少isConsentSigned字段")

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
							applyDate = a["applyDate"]
							date_format = "%Y-%m-%d %H:%M:%S"
							try:
								time.strptime(applyDate, date_format)
							# print("第%s袋血applyDate数据格式不正确"% i)
							except ValueError:
								print("applyDate数据格式不正确")
						except:
							print("缺少applyDate字段")

						try:
							applyBy = a["applyBy"]
							if applyBy is None or applyBy == " ":
								print("applyBy值为空")
						except:
							print("缺少applyBy字段")

						try:
							approveDate = a["approveDate"]
							date_format = "%Y-%m-%d %H:%M:%S"
							try:
								time.strptime(approveDate, date_format)
							# print("第%s袋血approveDate数据格式不正确"% i)
							except ValueError:
								print("approveDate数据格式不正确")
						except:
							print("缺少approveDate字段")

						try:
							approveBy = a["approveBy"]
							if approveBy is None or approveBy == " ":
								print("approveBy值为空")
						except:
							print("缺少approveBy字段")

						try:
							applyType = a["applyType"]
							applyType = str(applyType)
							applyType = applyType.isdigit()
							if applyType != True:
								print("袋血applyType数据格式不正确")
						except:
							print("缺少applyType字段")

						try:
							planDate = a["planDate"]
							date_format = "%Y-%m-%d %H:%M:%S"
							try:
								time.strptime(planDate, date_format)
							# print("第%s袋血planDate数据格式不正确"% i)
							except ValueError:
								print("planDatee数据格式不正确")
						except:
							print("缺少planDate字段")

						try:
							transPurpose = a["transPurpose"]
							transPurpose = str(transPurpose)
							transPurpose = transPurpose.isdigit()
							if transPurpose != True:
								print("袋血transPurpose数据格式不正确")
						except:
							print("缺少transPurpose字段")

						try:
							isConsentSigned = a["isConsentSigned"]
							isConsentSigned = str(isConsentSigned)
							isConsentSigned = isConsentSigned.isdigit()
							if isConsentSigned != True:
								print("袋血isConsentSigned数据格式不正确")
						except:
							print("缺少isConsentSigned字段")
				except:
					print("缺少patient字段")

				# ----------------------------------------------------------------------------------------------------------------------
				try:
					bloodTest = a["bloodTest"]
					# print(bloodTest)
					# print(type(bloodTest))
					# print(len(bloodTest))
					if bloodTest is None or bloodTest == "":
						print("bloodTest值为空")

					else:
						# for i in range(0,len(bloodTest)):
							# c = patient[i]
							# print(c)
							# c = dict(c)
						try:
							HB = bloodTest["HB"]
							HB = str(HB)
							if HB.count(".") != 1 and not HB.startswith(".") and HB.endswith("."):
								print("袋血HB格式错误")
						except:
							print("缺少HB字段")

						try:
							HCT = bloodTest["HCT"]
							HCT = str(HCT)
							if HCT.count(".") != 1 and not HCT.startswith(".") and HCT.endswith("."):
								print("袋血HCT格式错误")
						except:
							print("缺少HCT字段")


						try:
							PLT = bloodTest["HCT"]
							PLT = str(PLT)
							if PLT.count(".") != 1 and not PLT.startswith(".") and PLT.endswith("."):
								print("袋血PLT格式错误")
						except:
							print("缺少PLT字段")

						try:
							PT = bloodTest["PT"]
							PT = str(PT)
							if PT.count(".") != 1 and not PT.startswith(".") and PT.endswith("."):
								print("袋血PT格式错误")
						except:
							print("缺少PT字段")


						try:
							APTT = bloodTest["APTT"]
							APTT = str(APTT)
							# print(PAPTTT)
							if APTT.count(".") != 1 and not APTT.startswith(".") and APTT.endswith("."):
								print("袋血APTT格式错误")
						except:
							print("缺少APTT字段")

						try:
							FIB = bloodTest["FIB"]
							FIB = str(FIB)
							if FIB.count(".") != 1 and not FIB.startswith(".") and FIB.endswith("."):
								print("袋血FIB格式错误")
						except:
							print("缺少FIB字段")


						try:
							hbsag = bloodTest["hbsag"]
							hbsag = str(hbsag)
							if hbsag not in ("POSTIVE","NEGATIVE",):
								print("袋血hbsag格式错误")
						except:
							print("缺少hbsag字段")


						try:
							antiHbs = bloodTest["antiHbs"]
							antiHbs = str(antiHbs)
							if antiHbs not in ("POSTIVE","NEGATIVE",):
								print("袋血antiHbs格式错误")
						except:
							print("缺少antiHbs字段")


						try:
							hbeag = bloodTest["hbeag"]
							hbeag = str(hbeag)
							if hbeag not in ("POSTIVE","NEGATIVE",):
								print("袋血hbeag格式错误")
						except:
							print("缺少hbeag字段")

						try:
							antiHbe = bloodTest["antiHbe"]
							antiHbe = str(antiHbe)
							if antiHbe not in ("POSTIVE","NEGATIVE",):
								print("袋血antiHbe格式错误")
						except:
							print("缺少antiHbe字段")

						try:
							antiHbc = bloodTest["antiHbc"]
							antiHbc = str(antiHbc)
							if antiHbc not in ("POSTIVE","NEGATIVE",):
								print("袋血antiHbc格式错误")
						except:
							print("缺少antiHbc字段")

						try:
							antiHcv = bloodTest["antiHcv"]
							antiHcv = str(antiHcv)
							if antiHcv not in ("POSTIVE","NEGATIVE",):
								print("袋血antiHcv格式错误")
						except:
							print("缺少antiHcv字段")


						try:
							antiHiv = bloodTest["antiHiv"]
							antiHiv = str(antiHiv)
							if antiHiv not in ("POSTIVE","NEGATIVE",):
								print("袋血antiHiv格式错误")
						except:
							print("缺少antiHiv字段")


						try:
							syphilis = bloodTest["syphilis"]
							syphilis = str(syphilis)
							if syphilis not in ("POSTIVE","NEGATIVE",):
								print("袋血syphilis格式错误")
						except:
							print("缺少syphilis字段")

						try:
							INR = bloodTest["INR"]
							INR = str(INR)
							if INR.count(".") != 1 and not INR.startswith(".") and INR.endswith("."):
								print("袋血INR格式错误")
						except:
							print("缺少INR字段")


						try:
							ALT = bloodTest["ALT"]
							ALT = str(ALT)
							if ALT.count(".") != 1 and not ALT.startswith(".") and ALT.endswith("."):
								print("袋血ALT格式错误")
						except:
							print("缺少ALT字段")

						try:
							TEG = bloodTest["TEG"]
							# print(TEG)
							TEG = str(TEG)
							if TEG.count(".") != 1 and not TEG.startswith(".") and TEG.endswith("."):
								print("袋血TEG格式错误")
						except:
							print("缺少TEG字段")


						try:
							RPR = bloodTest["RPR"]
							RPR = str(RPR)
							if RPR.count(".") != 1 and not RPR.startswith(".") and RPR.endswith("."):
								print("袋血RPR格式错误")
						except:
							print("缺少RPR字段")


						try:
							TEGR = bloodTest["TEGR"]
							TEGR = str(TEGR)
							if TEGR.count(".") != 1 and not TEGR.startswith(".") and TEGR.endswith("."):
								print("袋血TEGR格式错误")
						except:
							print("缺少TEGR字段")

						try:
							TEGMA = bloodTest["TEGMA"]
							TEGMA = str(TEGMA)
							if TEGMA.count(".") != 1 and not TEGMA.startswith(".") and TEGMA.endswith("."):
								print("袋血TEGMA格式错误")
						except:
							print("缺少TEGMA字段")


						try:
							TEGA = bloodTest["TEGA"]
							TEGA = str(TEGA)
							if TEGA.count(".") != 1 and not TEGA.startswith(".") and TEGA.endswith("."):
								print("袋血TEGA格式错误")
						except:
							print("缺少TEGA字段")

						try:
							TEGCI = bloodTest["TEGCI"]
							TEGCI = str(TEGCI)
							if TEGCI.count(".") != 1 and not TEGCI.startswith(".") and TEGCI.endswith("."):
								print("袋血TEGCI格式错误")
						except:
							print("缺少TEGCI字段")

						try:
							HBVDNA = bloodTest["HBVDNA"]
							HBVDNA = str(HBVDNA)
							if HBVDNA.count(".") != 1 and not HBVDNA.startswith(".") and HBVDNA.endswith("."):
								print("袋血HBVDNA格式错误")
						except:
							print("缺少HBVDNA字段")


						try:
							WBC = bloodTest["WBC"]
							WBC = str(WBC)
							if WBC.count(".") != 1 and not WBC.startswith(".") and WBC.endswith("."):
								print("袋血WBC格式错误")
						except:
							print("缺少WBC字段")


						try:
							ALB = bloodTest["ALB"]
							ALB = str(ALB)
							if ALB.count(".") != 1 and not ALB.startswith(".") and ALB.endswith("."):
								print("袋血ALB格式错误")
						except:
							print("缺少ALB字段")

						try:
							antiScreeningResult = bloodTest["antiScreeningResult"]
							antiScreeningResult = str(antiScreeningResult)
							if antiScreeningResult.count(".") != 1 and not antiScreeningResult.startswith(".") and antiScreeningResult.endswith("."):
								print("袋血antiScreeningResult格式错误")
						except:
							print("缺少antiScreeningResult字段")


						try:
							rhTyping = bloodTest["rhTyping"]
							rhTyping = str(rhTyping)
							if rhTyping not in ("CcEe","CCEEE","ccEE","ccee","CCEe",
												"CcEE","ccEe","Ccee","CCee","CcDEe",
												"CCDEe","CCDee","CCDEE","CcDEE","CcDee",
												"ccDEe","ccDEE","ccDee","CcdEe","CCdEe",
												"CCdee","CCdEE""CcdEE","Ccdee","ccdEe","ccdEE",
												"ccdee","BEENSEND"):
								print("袋血rhTyping格式错误")
						except:
							print("缺少rhTyping字段")


						try:
							RPR = bloodTest["RPR"]
							RPR = str(RPR)
							if RPR not in ("NEGATIVE","POSTIVE"):
								print("袋血RPR格式错误")
						except:
							print("缺少RPR字段")

				except:
					print("缺少bloodTest字段")




				# ----------------------------------------------------------------------------------------------------------------------

				try:
					applyBloods = a["applyBloods"]
					# print(applyBloods)
					# print(bloodTest)
					# print(type(bloodTest))
					# print(len(bloodTest))
					if applyBloods is None or applyBloods == "":
						print("bloodTest值为空")

					else:
						for i in range(0,len(applyBloods)):
							c = applyBloods[i]
							try:
								bloodType = c["bloodType"]
								bloodType = str(bloodType)
								bloodType = bloodType.isdigit()
								if bloodType != True:
									print("第%s袋血bloodType数据格式不正确" % i)
									print(c)
							except:
								print("第%s袋缺少bloodType字段" % i)
								print(c)


							try:
								aboGroup = c["aboGroup"]
								aboGroup = str(aboGroup)
								aboGroup = aboGroup.isdigit()
								if aboGroup != True:
									print("第%s袋血aboGroup数据格式不正确" % i)
									print(c)
							except:
								print("第%s袋缺少aboGroup字段" % i)
								print(c)


							try:
								rhGroup = c["rhGroup"]
								rhGroup = str(rhGroup)
								rhGroup = rhGroup.isdigit()
								if rhGroup != True:
									print("第%s袋血rhGroup数据格式不正确" % i)
									print(c)
							except:
								print("第%s袋缺少rhGroup字段" % i)
								print(c)


							try:
								applyVolume = c["applyVolume"]
								applyVolume = str(applyVolume)
								if applyVolume.count(".") != 1 and not applyVolume.startswith(".") and  applyVolume.endswith("."):
									print("第%s袋血applyVolume数据格式不正确" % i)
									print(c)
							except:
								print("第%s袋缺少applyVolume字段" % i)
								print(c)

							try:
								applyUnit = c["applyUnit"]
								if applyUnit not in ("ml","ML","Ml","mL","单位","治疗","u","U"):
									print("第%s袋血单位格式错误"% i)
									print(c)
							except:
								print("第%s袋缺少applyUnit字段" % i)
								print(c)
							i = i + 1
							print("第%s袋血----------------------------------------------------------------------------------------------------------------->" % i)
				except:
					print("缺少applyBloods字段")

			except:
				print("数据格式错误，请检查是否少标点或使用了中文标点符号")

		except:
			print("您选择的text文件参数与您选择的接口不符，请核对文件内容是否是该接口的参数")
	except:
		print("您输入的text地址错误")

	os.system("pause")


