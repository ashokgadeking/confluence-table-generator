import sys
import json
from collections import defaultdict

## This script generates common props, common sub-props and property tree for a specific AWS service.

## Use the right input json file for the correct output. Supports third-party resources.

# USAGE $python generate_common_props_and_tree.py ../input_json_spec_files/mongodb-atlas-resource-spec.json MongoDB::Atlas
# USAGE $python generate_common_props_and_tree.py ../input_json_spec_files/cfn-resource-spec.json AWS::Quicksight

service = sys.argv[2]
input_file = sys.argv[1]
with open(input_file) as f:
	d = json.load(f)

class TreeNode:
	def __init__(self,data,data_type):
		self.data = data
		self.data_type = data_type
		self.children = []
		self.parent = None
	def add_child(self,child):
		self.child = child 
		child.parent = self
		self.children.append(child)
	def get_level(self):
		level = 0 
		p = self.parent
		while p :
			p = p.parent
			level += 1
		return level
	def get_ancestors(node,path):
		if node.parent:
			if node.parent.data_type == "List":
				path.append("*")
			path.append(node.parent.data)
			return node.parent.get_ancestors(path)
		return reversed(path[:-1])
	def print_tree(self):
		print('|--'*self.get_level(), end = '')
		if len(list(self.get_ancestors([]))) > 0:
			print(self.data + ' [' + ', '.join(self.get_ancestors([])) + ', ' + self.data + ']')
		else:
			print(self.data + ' [' + self.data + ']')
		if self.children:
			for each in self.children:
				each.print_tree()

def build_prop_tree(resource, property, json_load, parent_node):

	prop_name = resource + '.' + property

	properties = json_load['PropertyTypes'][prop_name]['Properties'].keys()

	for prop in properties:
		prop_keys = json_load['PropertyTypes'][prop_name]['Properties'][prop]
		# print(prop_name)
		if 'PrimitiveType' in prop_keys:
			data_type = prop_keys['PrimitiveType']
		else:
			data_type = prop_keys['Type']
		prop_node = TreeNode(prop,data_type)
		parent_node.add_child(prop_node)
		json_load['PropertyTypes'][prop_name]['Properties'][prop]['Path'] = prop_node.get_ancestors([])
		if 'PrimitiveType' not in prop_keys and 'PrimitiveItemType' not in prop_keys:
			if prop_keys['Type'] == 'List' or prop_keys['Type'] == 'Map':
				if prop_keys['ItemType'] != 'Tag':
					build_prop_tree(resource, prop_keys['ItemType'], json_load, prop_node)
			else:
				build_prop_tree(resource, prop_keys['Type'], json_load, prop_node)

	return properties

def run(json_load):

	for resource in d['ResourceTypes'].keys():
		if resource not in ["MongoDB::Atlas::Cluster",
							"MongoDB::Atlas::Project",
							"MongoDB::Atlas::DatabaseUser",
							"MongoDB::Atlas::EncryptionAtRest",
							"MongoDB::Atlas::PrivateEndpointService",
							"MongoDB::Atlas::Trigger",
							"MongoDB::Atlas::ThirdPartyIntegration",
							"MongoDB::Atlas::CustomDBRole",
							"MongoDB::Atlas::ProjectIpAccessList"]:
			continue
		if service in resource:
			root = TreeNode(resource,"root")
			properties = json_load['ResourceTypes'][resource]['Properties'].keys()

			for prop in properties:
				json_load['ResourceTypes'][resource]['Properties'][prop]['Path'] = []
				if prop == 'Tags':
					continue
				prop_keys = json_load['ResourceTypes'][resource]['Properties'][prop]
				if 'PrimitiveType' not in prop_keys and 'PrimitiveItemType' not in prop_keys:
					# print(prop)
					prop_node = TreeNode(prop,prop_keys['Type'])
					root.add_child(prop_node)
					if prop_keys['Type'] == 'List' or prop_keys['Type'] == 'Map':
						if prop_keys['ItemType'] != 'Tag':
							build_prop_tree(resource, prop_keys['ItemType'], json_load, prop_node)
					else:
						build_prop_tree(resource, prop_keys['Type'], json_load, prop_node)

			# print(resource)
			root.print_tree()

	return json_load

def get_resource_attribute_types(json_load):

	type_array = []

	for resource in json_load['ResourceTypes'].keys():
		if service in resource:
			if 'Attributes' in json_load['ResourceTypes'][resource].keys():
				attributes = json_load['ResourceTypes'][resource]['Attributes'].keys()
				for attribute in attributes:
					attr = json_load['ResourceTypes'][resource]['Attributes'][attribute]
					attr_type = ""
					if 'Type' in attr.keys():
						if attr['Type'] == 'List' and 'PrimitiveItemType' in attr.keys():
							attr_type = attr['PrimitiveItemType']
						if attr['Type'] == 'List' and 'ItemType' in attr.keys():
							# if attr['ItemType'] != 'Tag':
							attr_type = attr['ItemType']
						elif attr['Type'] != 'List':
							attr_type = attr['Type']
					elif 'PrimitiveType' in attr.keys():
						attr_type = attr['PrimitiveType']

					if attr_type != 'String' and attr_type != '':
						type_array.append(resource+'.'+attr_type)

	return type_array

def write_props_file(json_load,mode,file_name_suffix,attr_array):

	prop_dict = defaultdict(list)
	for resource in d[mode].keys():
		if service in resource and resource not in attr_array:
			properties = d[mode][resource]['Properties'].keys()
			for property in properties:
				if 'Path' in d[mode][resource]['Properties'][property].keys():
					prop_path_pattern = list(d[mode][resource]['Properties'][property]['Path'])
					prop_path_pattern.append(property)
					# prop_dict[property].append(resource + ' {code}' + str(prop_path_pattern)+'{code}')
					prop_dict[property].append(resource)

	with open(service.replace('::','_') + file_name_suffix + ".md", "w") as f:
		f.write('||Property||Resources\n')
		for key, value in prop_dict.items():
			if key == 'Tags' or key == 'Description':
				continue
			if len(value) > 1:
				line = '|' + key + '|'
				for res_type in value:
					line += res_type + " \\\\ "
				f.write(line+'|\n')


if __name__ == '__main__':

	json_load = run(d)

	attr_array = get_resource_attribute_types(json_load)
	write_props_file(json_load,'ResourceTypes','_common_props',attr_array)
	write_props_file(json_load,'PropertyTypes','_common_subprops',attr_array)

	pass

