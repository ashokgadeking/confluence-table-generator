import sys
import json
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

service = sys.argv[1]

def check_if_gr_required(property):
	gr_keywords = ["id","arn","encryption","username","password","type"]
	if any(keyword in property for keyword in gr_keywords):
	    gr_required = "Yes"
	else:
		gr_required = " "
	return gr_required

def build_table_md(resource, mode, file_mode):
	resource_name = resource.replace('::', '_').split(".",1)[0]
	file_name = resource_name
	if mode == 'PropertyTypes':
		file_name += '_subproperties'
	with open(file_name + ".md", file_mode) as f:
		if mode == 'ResourceTypes':
			f.write('||No.||Property||Description||Type||Threat Context||GR Required||Jira Story\n')
		else:
			parent_name = resource_name + ' ' + resource.split(".",1)[1]
			f.write('||No.||Subprops of '+parent_name+'||Description||Type||Threat Context||GR Required||Jira Story\n')
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
			gr_required = "Sub-property may require GR"
			if link is not None:
				new_link = link['href'].replace('./', url.rsplit("/",1)[0] + "/")
				prop_type = '[' + prop_type + '|' + new_link + ']'
			else:
				gr_required = check_if_gr_required(property)
			f.write('|'+ str(i) + '|' + property + '|' 
				+ desc.replace('\t','').replace('\n','') + '|' + prop_type
				+ '|' + ' ' + '|' + gr_required + '|' + ' ' + '|\n')
			i+=1

with open('cfn-resource-spec.json') as f:
	d = json.load(f)
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			build_table_md(resource, 'ResourceTypes', "w")
	for property in d['PropertyTypes'].keys():
		if service in property:
			build_table_md(property, 'PropertyTypes', "a")
	
			