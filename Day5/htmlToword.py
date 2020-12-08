
import urllib.request as url
import re
import sys

lnk='http://ramakrishnavivekananda.info/'
page=url.urlopen(lnk)
bData = page.read()
aData = bData.decode('utf-8')
txtData = re.sub('<.*?>','',aData)
print(txtData)



stdoutOrigin=sys.stdout 
sys.stdout = open("LOG.txt", "w")
sys.stdout.close()
sys.stdout=stdoutOrigin

