import sys
import json
import os
from collections import defaultdict
from pprint import pprint

# This Python script can be used to generate the json spec file that is necessary to make Mongo DB Atlas resources compatible with
# scripts initially written for AWS resources. AWS provides a file called the cfn-resource-spec.json on which most of the 
# scripts initially written in this repository were based on. It is basically a JSON file that contains every single property 
# under every single resource that is supported by AWS Cloud formation. What this script does is basically take all the 
# schema files of every single MongoDB Atlas resource and combine them into a spec file.

## USAGE
## python ./generate_mongodb_cfn_resource_spec.py > mongodb-atlas-resource-spec.json

def convert_schema(json, cfn_resource_spec, filename, mode, resource, read_only_props):

	cfn_resource_spec[mode][resource] = { "Properties": {} }

	if mode == "PropertyTypes" and "properties" not in json:

		if json['type'] != "array":
			cfn_resource_spec[mode][resource]['Type'] = json['type']
		else:
			cfn_resource_spec[mode][resource]['Type'] = "List"
			cfn_resource_spec[mode][resource]['ItemType'] = json['items']['$ref'].rsplit('/', 1)[-1]

		return cfn_resource_spec

	for prop in json['properties']:

		if prop in read_only_props:
			continue

		cfn_resource_spec[mode][resource]['Properties'][prop] = {}

		prop_dict = cfn_resource_spec[mode][resource]['Properties'][prop]

		desc = "Description unavailable"
		prop_type = "Property type unavailable"
		prop_key = "Type"

		if "description" in json['properties'][prop]:
			desc = json['properties'][prop]["description"]
		elif "$ref" in json['properties'][prop]:
			desc = desc = "Refer sub property " + json['properties'][prop]["$ref"].rsplit('/', 1)[-1]
		elif "items" in json['properties'][prop]:
			desc = "Refer sub property " + json['properties'][prop]["items"]["$ref"].rsplit('/', 1)[-1]

		prop_dict["Description"] = desc
		prop_dict["Required"] = False

		if 'sourceUrl' in json:
			if mode == "ResourceTypes":
				prop_dict["Documentation"] = json['sourceUrl'] + "/docs/README.md"+ "#" + prop
			elif mode == "PropertyTypes":
				prop_dict["Documentation"] = json['sourceUrl'] + "/docs/" + resource.lower().rsplit('.', 1)[-1] + ".md#" + prop

		if "type" in json['properties'][prop]:
			if json['properties'][prop]["type"] in ["number", "integer", "boolean", "string"]:
				prop_dict["PrimitiveType"] = json['properties'][prop]["type"].capitalize()
			
			elif json['properties'][prop]["type"] == "array":
				prop_dict["Type"] = "List"
				if "type" in json['properties'][prop]["items"]:
					if "$ref" in json['properties'][prop]["items"]:
						prop_dict["ItemType"] = json['properties'][prop]["items"]["$ref"].rsplit('/', 1)[-1]
					else:
						prop_dict["PrimitiveType"] = json['properties'][prop]["items"]["type"].capitalize()
				elif "$ref" in json['properties'][prop]["items"]:
					prop_dict["ItemType"] = json['properties'][prop]["items"]["$ref"].rsplit('/', 1)[-1]
			
			elif json['properties'][prop]["type"] == "object" and "$ref" in json['properties'][prop]:
				prop_dict["Type"] = "Map"
				prop_dict["ItemType"] = json['properties'][prop]['$ref'].rsplit('/', 1)[-1]

			elif json['properties'][prop]["type"] == "object" and "properties" in json['properties'][prop] and mode == "PropertyTypes":
				prop_dict["PrimitiveType"] = "String"

			elif json['properties'][prop]["type"] == "object" and prop == "BiConnector":
				prop_dict["PrimitiveType"] = "String"


		elif "$ref" in json['properties'][prop] and "type" not in json['properties'][prop]:
			prop_dict["Type"] = json['properties'][prop]["$ref"].rsplit('/', 1)[-1]

		if mode == "ResourceTypes" and "required" in json:
			if prop in json["required"]:
				prop_dict["Required"] = True

	if mode == "ResourceTypes" and "definitions" in json:
		for definition in json['definitions']:
			def_name = resource + "." + definition
			cfn_resource_spec["PropertyTypes"][def_name] = {}
			if 'sourceUrl' in json:
				json['definitions'][definition]['sourceUrl'] = json['sourceUrl']
			# pprint(json['definitions'][definition])
			convert_schema(json['definitions'][definition], cfn_resource_spec, filename, "PropertyTypes", def_name, read_only_props)

	return cfn_resource_spec

def open_all_files(directory):

	cfn_resource_spec = { "PropertyTypes": {}, "ResourceTypes": {} }

	for filename in os.listdir(directory):
		filepath = os.path.join(directory, filename)

		with open(filepath, 'r') as file:
			d = json.load(file)

			stripped_read_only_props = []

			if 'readOnlyProperties' in d:
				# pprint(d['readOnlyProperties'])
				read_only_props = d['readOnlyProperties']
				stripped_read_only_props = [s.rsplit('/', 1)[-1] for s in read_only_props]

			convert_schema(d, cfn_resource_spec, filename, "ResourceTypes", d['typeName'], stripped_read_only_props)

	print(json.dumps(cfn_resource_spec, indent=2))

if __name__ == '__main__':

	open_all_files("../mongodb_atlas_schemas")

	pass



