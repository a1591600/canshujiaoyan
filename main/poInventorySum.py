	# -*- coding:utf-8 -*-
# coding=gbk
import time
import os



def poInventorySum():
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
				# 	"currentDate": "2018-12-17",
				# 	"summary": [{
				# 		"bloodType": 1,
				# 		"aPosVol": 0,
				# 		"bPosVol": 1,
				# 		"oPosVol": 0,
				# 		"abPosVol": 0,
				# 		"aNegVol": 0,
				# 		"bNegVol": 0,
				# 		"oNegVol": 0,
				# 		"abNegVol": 0,
				# 		"unit": "ml"
				# 	}]
				# }
				key = a.keys()
				# print(type(key))
				# print(key)
				try:

					currentDate = a["currentDate"]
					date_format = "%Y-%m-%d"
					try:
						time.strptime(currentDate, date_format)
					# print("袋血donationDate数据格式不正确")
					except ValueError:
						print("currentDate数据格式不正确")
				except:
					print("缺少currentDate字段")

				try:
						summary = a["summary"]
						# print(summary)
						for i in range(0,len(summary)):
							c = summary[i]
							c = dict(c)
							try:
								# print(type(c))
								bloodType = c["bloodType"]
								bloodType=str(bloodType)
								bloodType = bloodType.isdigit()
								if bloodType !=True:
									print("第%s袋血bloodType数据格式不正确"% i)
									print(c)
							except:
								print("缺少bloodType字段")
								print(c)
							try:
								aPosVol = c["aPosVol"]
								aPosVol=str(aPosVol)
								aPosVol = aPosVol.isdigit()
								if aPosVol !=True:
									print("第%s袋血aPosVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少aPosVol字段")
								print(c)

							try:
								bPosVol = c["bPosVol"]
								bPosVol=str(bPosVol)
								bPosVol = bPosVol.isdigit()
								if bPosVol !=True:
									print("第%s袋血bPosVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少bPosVol字段")
								print(c)
							try:
								oPosVol = c["oPosVol"]
								oPosVol=str(oPosVol)
								oPosVol = oPosVol.isdigit()
								if oPosVol !=True:
									print("第%s袋血oPosVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少oPosVol字段")
								print(c)


							try:
								abPosVol = c["abPosVol"]
								abPosVol=str(abPosVol)
								abPosVol = abPosVol.isdigit()
								if abPosVol !=True:
									print("第%s袋血abPosVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少abPosVol字段")
								print(c)


							try:
								aNegVol = c["aNegVol"]
								aNegVol=str(aNegVol)
								aNegVol = aNegVol.isdigit()
								if aNegVol !=True:
									print("第%s袋血aNegVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少aNegVol字段")
								print(c)


							try:
								bNegVol = c["bNegVol"]
								bNegVol=str(bNegVol)
								bNegVol = bNegVol.isdigit()
								if bNegVol !=True:
									print("第%s袋血bNegVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少bNegVol字段")
								print(c)

							try:
								oNegVol = c["oNegVol"]
								oNegVol=str(oNegVol)
								oNegVol = oNegVol.isdigit()
								if oNegVol !=True:
									print("第%s袋血oNegVol数据格式不正确"% i)
									print(c)

							except:
								print("缺少oNegVol字段")
								print(c)


							try:
								abNegVol = c["abNegVol"]
								abNegVol=str(abNegVol)
								abNegVol = abNegVol.isdigit()
								if abNegVol !=True:
									print("第%s袋血abNegVol数据格式不正确"% i)
									print(c)
							except:
								print("缺少abNegVol字段")
								print(c)


							try:
								unit = c["unit"]
								if unit not in ("ml","ML","Ml","mL","单位","治疗","u","U"):
									print("第%s袋血单位格式错误"% i)
									print(c)
							except:
								print("缺少unit字段")
								print(c)

							i=i+1
							print("第%s袋血----------------------------------------------------------------------------------------------------------------->"% i)
				except:
					print("传参缺少summary字段")
			except:
				print("数据格式错误，请检查是否少标点或使用了中文标点符号")
		except:
			print("您选择的text文件参数与您选择的接口不符，请核对文件内容是否是该接口的参数")
	except:
		print("您输入的text地址错误")
	os.system("pause")