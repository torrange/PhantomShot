#!/usr/bin/env python2
import os
import sys
from PIL import Image
from subprocess import call

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

sfx = "jpg"
ms =  50 if not is_number(sys.argv[-1]) else sys.argv[-1]
cpath = os.path.dirname(os.path.abspath(__file__))
make_fname = lambda url: "%s.%s" % (url.split("//")[1].replace("/", "").replace('?','')[:-1], sfx)
ghost_site = lambda url: call(['phantomjs', 'webshot.js', url, make_fname(url), str(ms)])
get_sites = lambda cpath: [ghost_site(url) for url in open(cpath+'/urls').readlines()]
cnv_image = lambda fname: Image.open(fname).save('cnv_%s'%fname, q="web-high") 
cnv_images = lambda cpath: [cnv_image(make_fname(url)) for url in open(cpath+"/urls").readlines()]

def main():
    get_sites(cpath)
    cnv_images(cpath)

if __name__=="__main__":
    main()
