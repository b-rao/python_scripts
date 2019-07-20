#!/usr/bin/env python3
import os
import subprocess
import argparse
import hashlib

parse = argparse.ArgumentParser()
parse.add_argument("website", help="Website to check", type=str)
args = parse.parse_args()

# website user entered may be a malicious string
site = args.website.split()[0]
#store copy of website under hash + .html
hsh = hashlib.md5(site.encode())
siteHash = hsh.hexdigest() + ".html"
stored_websites = "stored_websites/"
savedsite = stored_websites + siteHash

file_exist = os.path.isfile(savedsite)
if file_exist: # have a copy to check against
    pass
else: #download a copy to check in future
	bash = "mkdir " + stored_websites
	subprocess.run(bash.split(), stdout = None)
	bash ="curl " + site +" > "+ savedsite
	subprocess.run(bash, shell =True)
	print("Made a html copy")
	quit(0)
	
#checking using diff -w
#get new copy of site
bash = "curl "+ site + " > " + stored_websites + "temp.html"
subprocess.run(bash, shell =True)
#check against the stored old
bash = "diff -w " + savedsite + " " + stored_websites+ "temp.html"
process = subprocess.run(bash ,shell=True, stdout = subprocess.PIPE)

if process.stdout == b'':
	print("No changes for {}".format(site))
else:
	print("{} has changed".format(site))
	bash = "cp " +stored_websites + "temp.html " + savedsite
	subprocess.run(bash, shell=True)
#cleanup temp.html
bash = "rm "+ stored_websites+"temp.html"
subprocess.run(bash, shell=True)