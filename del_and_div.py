def delete_comment(data):
	data = open(data).readlines()

	del_num = [-1]
	del_flag = False

	for i in range(0,len(data)):
		for j in range(0,len(data[i])):
			if(data[i].find(';') < data[i].find('/') and data[i].find(';') != -1):
				data[i] = data[i][0:data[i].find('/')-1]
				continue
			if(data[i][j] == ' '):
				continue
			if(del_flag):
				if(data[i][j] == '*'):
					if(data[i][j+1] == '/'):
						del_num.append(i)
						del_flag = False
						break
					else:
						continue
				del_num.append(i)
				continue	

			if(data[i][j] == '/'):
				if(data[i][j+1] == '/'):
					del_num.append(i)
					break
				if(data[i][j+1] == '*'):
					del_flag = True
					del_num.append(i)
					break
			else:
				break
	del del_num[0]
	del_num = list(set(del_num))
	del_num.reverse()
	for i in range(0,len(del_num)):
		del data[del_num[i]]


    #############save##############
	f = open("check.sol",'w')
	for i in range(0,len(data)):
		f.write(data[i])
	f.close()

	return data

def beautifier(data):
	data = "".join(open(data).readlines()).replace('\n','')
	data = data.replace(';',';\n').replace('{','{\n').replace('}','}\n')
	f = open("check.sol",'w')
	f.write(data)
	f.close()

def relation(data):
	data = open(data).readlines()

	data_div = {}
	key = ''
	key2= ''

	for i in range(0,len(data)):
		if(data[i].find('contract') != -1):
			key = data[i]
			key2 = ''
			data_div[key] = {}
			continue

		elif(data[i].find('interface') != -1 or data[i].find('library') != -1 ):
			key = ''
			key2 = ''
			continue

		elif(key != ''):
			if(data[i].find("function") != -1):
				key2 = data[i]
				data_div[key][key2] = ''
				continue

		if(key2 != ''):
			data_div[key][key2] += data[i]

	return data_di
