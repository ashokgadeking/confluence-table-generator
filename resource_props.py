import sys
import json
import os
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

service = sys.argv[1]

def build_table_md(resource, mode):
	path = resource.replace('::', '_').split(".",1)[0]
	if mode == 'ResourceTypes':
		os.mkdir(path)
	with open(path + "/" + resource.replace('::', '_').replace('.', '_') + ".md", "w") as f:
		f.write('||No.||Property||Description||Type||Threat Context||GR Required||Jira Story\n')
		mode_contents = d[mode]
		if resource in d[mode].keys():
			print("\n"+resource)
			properties = d[mode][resource]['Properties'].keys()
			i=1
			for property in properties:
				url = d[mode][resource]['Properties'][property]['Documentation']
				response = requests.get(url)
				soup = BeautifulSoup(response.content, "html.parser")
				tag = soup.find(id=url.split("#",1)[1])
				desc = str(tag.next_sibling.p.get_text())
				while desc.find("  ") != -1:
					desc = desc.replace("  ", " ")
				parent_tag = tag.next_sibling.find_all(string="Type")[0].parent.parent
				prop_type = parent_tag.get_text().split(" ",1)[1]
				link = parent_tag.find('a', href=True)
				if link is not None:
					new_link = link['href'].replace('./', url.rsplit("/",1)[0] + "/")
					prop_type = '[' + prop_type + '|' + new_link + ']'
					if mode != 'PropertyTypes':
						build_table_md(resource + '.' + property, 'PropertyTypes')
				f.write('|'+ str(i) + '|' + property + '|' 
					+ desc.replace('\t','').replace('\n','') + '|' + prop_type
					+ '|' + ' ' + '|' + ' ' + '|' + ' ' + '|\n')
				i+=1

with open('cfn-resource-spec.json') as f:
	d = json.load(f)
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			build_table_md(resource, 'ResourceTypes')
			