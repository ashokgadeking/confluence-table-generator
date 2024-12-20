import sys
import json
from collections import defaultdict
import requests

# This script generates confluenct tables for 3rd party AWS services like MongoDb:Atlas. It takes the generated spec file as input
# and build confluence tables while taking common props and sub props into account.

# USAGE $python generate_conf_table_third_party.py MongoDb::Atlas::Cluster
##OR
# USAGE $python generate_conf_table_third_party.py MongoDb::Atlas

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
		print("\n"+resource)
		properties = d[mode][resource]['Properties'].keys()

		if len(properties) < 1:
			return

		print(len(properties))

		if mode == 'ResourceTypes':
			f.write('||No.||Property||Description||Type||Property Required||Threat Context||Common Property||GR Required||Jira Story\n')
		else:
			parent_name = resource_name + ' ' + resource.split(".",1)[1]
			f.write('||No.||Subprops of '+parent_name+'||Description||Type||Property Required||Threat Context||Common Property||GR Required||Jira Story\n')
		i=1

		for property in properties:

			desc = d[mode][resource]['Properties'][property]['Description']
			req = d[mode][resource]['Properties'][property]['Required']
			docs = d[mode][resource]['Properties'][property]['Documentation']

			common_property = "No"
			if len(prop_dict[property]) > 1:
				common_property = "Yes"
			if property != "Tags":
				gr_required = "Sub-property may require GR"

			if "PrimitiveType" in d[mode][resource]['Properties'][property]:
				prop_type = d[mode][resource]['Properties'][property]["PrimitiveType"]
			elif "Type" in d[mode][resource]['Properties'][property]:
				if d[mode][resource]['Properties'][property]["Type"] in ["List","Map"] and "ItemType" in d[mode][resource]['Properties'][property]:
					prop_type = d[mode][resource]['Properties'][property]["Type"] + " of " + d[mode][resource]['Properties'][property]["ItemType"]
				else:
					prop_type = d[mode][resource]['Properties'][property]["Type"]
					prop_type = '[' + prop_type + '|' + docs + ']'

			gr_required = check_if_gr_required(property)
			print(property + ' ' + gr_required)

			f.write('|'+ str(i) + '|' + property + '|' 
				+ desc.replace('\t','').replace('\n','').replace('{','').replace('}','') + '|' + prop_type + '|' + str(req) + '|' + ' '
				+ '|' + common_property + '|' + gr_required + '|' + ' ' + '|\n')
			i+=1

with open('conversion.json') as f:
	d = json.load(f)
	res_prop_dict = get_prop_dict(d, 'ResourceTypes')
	sub_prop_dict = get_prop_dict(d, 'PropertyTypes')
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			build_table_md(resource, 'ResourceTypes', "w", res_prop_dict)
	for property in d['PropertyTypes'].keys():
		if service in property:
			build_table_md(property, 'PropertyTypes', "a", sub_prop_dict)
	
			