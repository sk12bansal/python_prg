from __future__ import print_function
import sys
if sys.version_info.major==2:
    range=xrange
    from itertools import izip as zip
    from itertools import imap as map
    
    
for i in range(10):
    print("counting",i)
