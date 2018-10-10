import argparse
import sys
import re

# Usage : python ./mysolgraph.py -s example.sol

def analyze_sol(sol):
	code = sol.read()

	# finding contract name in code
	pattern1 = re.compile("contract\s\w.*")
	matched1 = pattern1.findall(code)
	contract_list = []
	
	for i in range(len(matched1)):
		contract_list.append(matched1[i].split()[1])
	print contract_list

	# finding function name in code and save visibility
	pattern2 = re.compile("function\s\w.*")
	matched2 = pattern2.findall(code)
	

	# finding constructor in code
	#if (func_name == contract_name):
	#	constructor = func_name


def main():
	global args

	parser = argparse.ArgumentParser()

	parser.add_argument("-s",  "--source", type=str, help="local source file name. Solidity by default.")
	args = parser.parse_args()
	sol = open(args.source,'r')

	analyze_sol(sol)

if __name__ == '__main__':
    main()