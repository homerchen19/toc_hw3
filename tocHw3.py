import re
import sys

infile = open(sys.argv[1], 'r') #輸入的檔案名
minlink = int(sys.argv[2]) #最小的個數
a = 0

for line in infile: #一行一行讀檔
	url = re.findall('"WARC-Target-URI"[ :]+((?=\[)\[[^]]*\]|(?=\{)\{[^\}]*\}|\"[^"]*\")', line) #抓"WARC-Target-URI"
	str_url = ''.join(url) #把list轉成str
	url2 = re.findall('"([^"]*)"', str_url) #抓str裡雙引號中間的字串
	str_url = ''.join(url2) #得到最後完整的網址

	links = re.findall('"Links"[ :]+((?=\[)\[[^]]*\]|(?=\{)\{[^\}]*\}|\"[^"]*\")', line) #抓"Links"裡的東西
	str_tmp = ''.join(links) #把list轉成str

	href = re.findall('"href"[ :]+\"[^"]*\"', str_tmp) #抓"herf:"後面的東西
	num_href = len(href) #直接算list裡面有幾個東西就可以了

	url = re.findall('"url"[ :]+\"[^"]*\"', str_tmp) #抓"url:"後面的東西
	num_url = len(url) #直接算list裡面有幾個東西就可以了

	total = num_href + num_url #總合

	if total >= minlink: #跟要求的最小個數比較
		'''a += 1
		print ""
		print a
		print 'url: '  
		print str_url'''
		'''print 'href: '  
		print href
		print len(href)
		print 'url: '  
		print url
		print len(url)
		print total'''
		print '%s : %d' % (str_url, total); #print答案