import re
import sys
import os.path
#import time
#tStart = time.time()

#f = open('outfile.txt', 'w')

def verify_inputfile():
	inputfile = sys.argv[1]
	if os.path.exists(inputfile):
		pass
	elif not os.path.exists(inputfile):
		print "There is no " + inputfile
		sys.exit(0)
	else:
		print "There is no input file !"
		sys.exit(0)
		
	return inputfile

def verify_topk():
	if len(sys.argv) > 2:
		topk = int(sys.argv[2])
	else:
		print "There is no topk !"
		sys.exit(0)

	if topk < 0:
		print "The topk should be positive !"
		sys.exit(0)
		
	return topk

valid_infile = verify_inputfile()
infile = open(valid_infile, 'r')
topk = verify_topk()

total_list= []
dict1 = {}

for line in infile:
	url = re.findall('"WARC-Target-URI":"([^"]*)"', line) 
	str_url = ''.join(url)

	links = re.findall('"Links":\[(.+)\](,"Head"|\},"Entity-Digest")', line)
	str_links = ''.join(str(i) for i in links)

	href = re.findall('"href"[ :]+\"([^"]*)\"', str_links)
	num_href = len(href)

	url = re.findall('"url"[ :]+\"([^"]*)\"', str_links)
	num_url = len(url)

	total = num_href + num_url

	total_list.append(total)
	dict1.setdefault(total, []).append(str_url) #dict with list
#print total_list
#total_list = merge_sort(total_list) #do merge_sort
total_list.sort(reverse=True) #do merge_sort

count = 0
for i in range(0, topk):
	tmplist = dict1.get(total_list[i]) #find key in dict1
	if tmplist == None:
		continue
	for item in tmplist:
		if item != "":
			#f.write( item + ":" + str(total_list[i]) + "\n") #print list
			print item + ":" + str(total_list[i]) #print list

	dict1.pop(total_list[i], None) #pop the key(= total_list[i])
	count += len(tmplist) 
	if count >= topk: #in case lenth of list exceed topk
		break
#f.close()
#tEnd = time.time()
#print "It cost %f sec" % (tEnd - tStart)