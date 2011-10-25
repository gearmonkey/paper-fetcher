#!/usr/bin/env python
# encoding: utf-8
"""
ismir_papers.py

Gathers all the ISMIR 2011 papers, downloading them all in one go.

creates (via an append) a tsv file of the metadata (paper number, title, authors) 
	as the papers are fetched.

optionally will take a runtime arg of an int specifying how many items to skip to help 
	recovery and restart during dropped connections.

Created by Benjamin Fields on 2011-10-25. 
Copyleft 2011. 
"""

import sys
import os, os.path
import urllib
import re
import csv

ISMIR_BASE = 'http://ismir2011.ismir.net'
ISMIR_PROGRAM = ISMIR_BASE + '/program2011.html'


def main():
	try:
		start = int(sys.argv[2])
	except IndexError:
		start = 0
	fields = ("num", "title", "authors")
	meta_writer = csv.DictWriter(open('metadata.tsv', 'a'), 
	                            fieldnames = fields, 
	                            delimiter='\t')
	meta_writer.writerow(dict(zip(fields, fields)))
	pat = re.compile("""<li>\((.*?)\).*?<a href="(.*?)">(.*?)</a><br>(.*?)</li>""")
	print 'fetching schedule from', ISMIR_PROGRAM
	page = urllib.urlopen(ISMIR_PROGRAM).read()
	metadata = pat.findall(page)
	print "found {0} papers".format(len(metadata))
	for num, path, title, authors in metadata[start:]:
		local_path = os.path.split(path)[1]
		remote_path = ISMIR_BASE+path
		print "fetching", remote_path
		urllib.urlretrieve(remote_path, local_path)
		meta_writer.writerow({"num":num, "title":title, "authors":authors})


if __name__ == '__main__':
	main()

