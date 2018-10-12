def delete_comment(data):
	data = open(data).readlines()

	del_num = [-1]
	del_flag = False

	for i in range(0,len(data)):
		for j in range(0,len(data[i])):
			if(data[i].find(';') < data[i].find('/') and data[i].find(';') != -1):
				data[i] = data[i][0:data[i].find('/')-1]
				break;

			if(data[i][j] == ' '):
				continue

			if(data[i][j] == '/'):
				if(data[i][j+1] == '/'):
					del_num.append(i)
					break
				if(data[i][j+1] == '*'):
					if(data[i].find('*/') != -1):
						del_num.append(i)
						break

					del_flag = True
					del_num.append(i)
					break

			if(del_flag):
				if(data[i].find('*/') != -1):
					del_num.append(i)
					del_flag = False
					break

				del_num.append(i)

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
			if(key != '' and key2 != ''):
				data_div[key][key2] = data_div[key][key2].replace('  ','')[:-5]

			key = data[i].replace('{\n','').replace(' ','').replace('contract','contract_').replace('is','_')
			key2 = ''
			data_div[key] = {}
			continue

		elif(data[i].find('interface') != -1 or data[i].find('library') != -1 ):
			if(key != '' and key2 != ''):
				data_div[key][key2] = data_div[key][key2].replace('  ','')[:-3]

			key = ''
			key2 = ''
			continue

		elif(key != ''):
			if(data[i].find("function") != -1):
				if(key2 != ''):
					data_div[key][key2] = data_div[key][key2].replace('  ','')[:-3]

				key2 = data[i].replace('{\n','').replace(' ','').replace('function','function_')
				key2 = key2.replace('public','_public_').replace('internal','_internal_').replace('private','_private_').replace('external','_external_')
				key2 = key2.replace('view','_view_').replace('pure','_pure_').replace('constant','_constant_')
				key2 = key2.replace('__','_')
				if(key2[-1:] == '_'):
					key2 = key2[:-1]

				data_div[key][key2] = ''
				continue

		if(key2 != ''):
			data_div[key][key2] += data[i]

	return data_div

def view(a):
	for i in range(0,len(a.keys())):
		print '\033[34m---------------contract--------------------------'
		print "\033[35m"+a.keys()[i]+"\033[0m"
		print '\033[34m---------------function--------------------------'
		if(len(a[a.keys()[i]].keys()) == 0):
			print '               NO FUNCTION'
		for j in range(0,len(a[a.keys()[i]].keys())):
			print '\033[31m'+a[a.keys()[i]].keys()[j]+"\033[0m" + '\n\033[33m'+a[a.keys()[i]][a[a.keys()[i]].keys()[j]]+"\033[0m\n"
		print'\033[34m-------------------------------------------------\n\n\033[0m'

delete_comment('flag.sol')
beautifier("check.sol")
view(relation("check.sol"))
