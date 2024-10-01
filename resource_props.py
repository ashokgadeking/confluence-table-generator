import sys
import json
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

service = sys.argv[1]

def get_prop_dict(d, mode):
	prop_dict = defaultdict(list)
	for resource in d[mode].keys():
		if service in resource:
			properties = d[mode][resource]['Properties'].keys()
			for property in properties:
				prop_dict[property].append(resource)

	return prop_dict

def check_if_gr_required(property):
	gr_keywords = ["Id","Arn","Encryption","Password","Role","SecurityGroup"]
	if any(keyword in property for keyword in gr_keywords):
	    gr_required = "Yes"
	else:
		gr_required = " "
	return gr_required

def build_table_md(resource, mode, file_mode, prop_dict):
	resource_name = resource.replace('::', '_').split(".",1)[0]
	file_name = resource_name
	if mode == 'PropertyTypes':
		file_name += '_subproperties'
	with open(file_name + ".md", file_mode) as f:
		if mode == 'ResourceTypes':
			f.write('||No.||Property||Description||Type||Threat Context||Common Property||GR Required||Jira Story\n')
		else:
			parent_name = resource_name + ' ' + resource.split(".",1)[1]
			f.write('||No.||Subprops of '+parent_name+'||Description||Type||Threat Context||Common Property||GR Required||Jira Story\n')
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
			common_property = "No"
			if len(prop_dict[property]) > 1:
				common_property = "Yes"
			if property != "Tags":
				gr_required = "Sub-property may require GR"
			if link is not None:
				new_link = link['href'].replace('./', url.rsplit("/",1)[0] + "/")
				prop_type = '[' + prop_type + '|' + new_link + ']'
			else:
				gr_required = check_if_gr_required(property)
				print(property + ' ' + gr_required)
			f.write('|'+ str(i) + '|' + property + '|' 
				+ desc.replace('\t','').replace('\n','') + '|' + prop_type + '|' + ' '
				+ '|' + common_property + '|' + gr_required + '|' + ' ' + '|\n')
			i+=1

with open('cfn-resource-spec.json') as f:
	d = json.load(f)
	res_prop_dict = get_prop_dict(d, 'ResourceTypes')
	sub_prop_dict = get_prop_dict(d, 'PropertyTypes')
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			build_table_md(resource, 'ResourceTypes', "w", res_prop_dict)
	for property in d['PropertyTypes'].keys():
		if service in property:
			build_table_md(property, 'PropertyTypes', "a", sub_prop_dict)
	
			