def delete_comment(data):
	data = open(data).readlines()

	del_num = [-1]
	del_flag = False

	for i in range(0,len(data)):
		for j in range(0,len(data[i])):
			if(data[i][j] == ' '):
				continue
			if(del_flag):
				if(data[i][j] == '*'):
					if(data[i][j+1] == '/'):
						del_num.append(i)
						del_flag = False
						#print(data[i])
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

def divide(data):
	data = open(data).readlines()

	data_div = {}
	key = ''
 
	for i in range(0,len(data)):
		if(data[i].find('contract ') == 0 or data[i].find('interface') == 0 or data[i].find('library') == 0):
			key = data[i]
			data_div[key] = ''
			
		else:
			if(key == ''):
				continue
			data_div[key] += data[i]

	#############save##############
	f = open("check.sol",'w')
	for i in range(0,len(data_div.keys())):
		f.write(data_div.keys()[i])
		f.write(data_div[data_div.keys()[i]])
		f.write("/*#######################div###############################*/\n")
	f.close()

	return data_div