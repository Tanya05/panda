#/usr/bin/env python
import sys
from nlp import *
from pandawiki import *

(t,word) = getMeaning(sys.argv)
if(t == 1):
    print "Looking up wiki entry for",word
    wikisearch(word)
