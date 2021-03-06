#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File Name:    scan_same_pic.py
@Author:       shaozengguang
@Mail:         shaozg1101@126.com
@Created Time: 五, 12/23/2016, 14时08分10秒
@Copyright:    GPL 2.0
@Description:  
"""

import os
import hashlib
import sys

# key 文件的md5值，value 所有的文件
g_dict = {'':[]}

# md5
def md5sum(filename):
	fd = open(filename, 'r')
	content = fd.read()
	fd.close()
	md5 = hashlib.md5(content).hexdigest()
	return md5

# 遍历目录
def walk_dir(path):
	global g_dict
	for root, dirs, files in os.walk(path):
		for fn in files:
			f = root + '/' + fn
			if os.path.isfile(f) and (f.find('.png') >= 0 or f.find('.jpg') >= 0):
				k = md5sum(f)
				if g_dict.has_key(k):
					g_dict[k].append(f)
				else:
					g_dict[k] = [f]
				
# 只有value中有多个图片的时候，才处理
def check_dict():
	global g_dict
	count = 0
        same_item_total_size = 0
        same_item_pure_size = 0
	for k, v in g_dict.items():
		if len(v) > 1:
			count = count + 1
			print k, v
                        same_item_pure_size = same_item_pure_size + os.path.getsize(v[0])
                        same_item_total_size = same_item_total_size + len(v) * os.path.getsize(v[0])

        print 'count:%d--total size:%d--pure size:%d' % (count, same_item_total_size, same_item_pure_size)

if __name__ == "__main__":
	# global g_dict
        dir=sys.argv[1]
        if (os.path.exists(dir)):
	    walk_dir(dir)
	    check_dict()
        else:
            print 'Please input correct directory!'

