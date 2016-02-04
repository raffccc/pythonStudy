#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""
Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def sort_urls(urlpath):
    match = re.search('-(\w+)-(\w+).jpg', urlpath)
    if match:
        return match.group(2)
    return urlpath

def read_urls(filename):
    """
    Returns a list of the puzzle urls from the given log file,
    extracting the hostname from the filename itself.
    Screens out duplicate urls and returns the urls sorted into
    increasing order.
    """
    
    baseurl = 'http://www.' + filename[filename.find('_') + 1:]
    
    f = open(filename, 'rU')
    
    paths = re.findall('GET (\S+puzzle\S+) HTTP', f.read())
    
    uniquePaths = []
    for path in paths:
        if baseurl+path not in uniquePaths:
            uniquePaths.append(baseurl+path)
    
    return sorted(uniquePaths, key=sort_urls)

def download_images(img_urls, dest_dir):
    """
    Given the urls already in the correct order, downloads
    each image into the given directory.
    Gives the images local filenames img0, img1, and so on.
    Creates an index.html in the directory
    with an img tag to show each local image file.
    Creates the directory if necessary.
    """
    absolute_dest_dir = os.path.abspath(dest_dir)
    if not os.path.exists(absolute_dest_dir):
        os.makedirs(absolute_dest_dir)
    
    index = 0
    imagePaths = []
    for img_url in img_urls:
        print 'Retrieving: ', img_url
        imagePath = os.path.abspath(os.path.join(dest_dir, 'img' + str(index)))
        imagePaths.append(imagePath)
        urllib.urlretrieve(img_url, imagePath)
        index += 1
        
    f = open(os.path.abspath(os.path.join(dest_dir,'index.html')), 'w')
    f.write('<verbatim>\n <html> \n <body>\n' + ''.join(['<img src="' + imagePath + '"/>'  for imagePath in imagePaths]) + '</body>\n</html>')
    f.close()
    

def main():
    args = sys.argv[1:]

    if not args:
        print 'usage: [--todir dir] logfile '
        sys.exit(1)

    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    img_urls = read_urls(args[0])

    if todir:
        download_images(img_urls, todir)
    else:
        print '\n'.join(img_urls)

if __name__ == '__main__':
    main()
