import re
import sys
#coding:utf-8

infile = open(sys.argv[1], 'r')
topk = int(sys.argv[2])
total_list= []
dict1 = {}

for line in infile:
	url = re.findall('"WARC-Target-URI":"[^"]*"', line) 
	str_url = ''.join(url)
	url2 = re.findall('"([^"]*)"', str_url)
	str_url = ''.join(url2)

	links = re.findall('"Links":((?=\[)\[[^]]*\]|(?=\{)\{[^\}]*\}|\"[^"]*\")', line)
	str_tmp = ''.join(links)

	href = re.findall('"href":"[^"]*"', str_tmp)
	num_href = len(href)

	url = re.findall('"url":"[^"]*"', str_tmp)
	num_url = len(url)

	total = num_href + num_url

	total_list.append(total)
	dict1.setdefault(total, []).append(str_url) #dict with list

def merge_sort(m):
   	if len(m) <= 1:
        		return m
 
   	middle = len(m) / 2
    	left = m[:middle] #above middle
   	right = m[middle:] #behind middle
 
   	left = merge_sort(left)
   	right = merge_sort(right)
   	return list(merge(left, right))

def merge(left, right):
	result = []
	left_idx, right_idx = 0, 0
	while left_idx < len(left) and right_idx < len(right):
		if left[left_idx] >= right[right_idx]:
			result.append(left[left_idx])
			left_idx += 1
		else:
			result.append(right[right_idx])
			right_idx += 1
	if left:
		result.extend(left[left_idx:])
	if right:
		result.extend(right[right_idx:])
	return result

#print total_list
total_list = merge_sort(total_list) #do merge_sort
'''print total_list
print
print 'topk:'
print total_list[:topk]'''


count = 0
for i in range(0, topk):
	tmplist = dict1.get(total_list[i]) #find key in dict1
	if tmplist == None:
		continue

	for item in tmplist:
		print item + " : " + str(total_list[i]) #print list

	dict1.pop(total_list[i], None) #pop the key(= total_list[i])
	count += len(tmplist) 
	if count >= topk: #in case lenth of list exceed topk
		break