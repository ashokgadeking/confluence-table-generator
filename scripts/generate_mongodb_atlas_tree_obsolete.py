import sys
import json
from collections import defaultdict
import os

# This script was built before the cfn spec conversion script was written. This is obsolete but still functional.
# This script directly reads the schema files of 3rd part AWS resources and builds a property tree
# continaing common props and subprops for an AWS service.

# USAGE $python generate_mongodb_atlas_tree_obsolete.py MongoDB::Atlas

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
			if node.parent.data_type == "array":
				path.append("*")
			path.append(node.parent.data)
			return node.parent.get_ancestors(path)
		return reversed(path[:-1])
	def print_tree(self):
		print('|--'*self.get_level(), end = '')
		if len(list(self.get_ancestors([]))) > 0:
			print(self.data + ' [' + ', '.join(self.get_ancestors([])) + ', ' + self.data + ']')
		else:
			if '::' in self.data:
				print('\n' + self.data)
			else:
				print(self.data + ' [' + self.data + ']')
		if self.children:
			for each in self.children:
				each.print_tree()

def run(json_load):

	properties = json_load['properties'].keys()

	root = TreeNode(json_load["typeName"],"root")

	for prop in properties:
		if prop not in ["Tags", "LastUpdatedTime", "CreatedTime", "Created"]:
			analyze_property(prop, 'properties', json_load, root)

	root.print_tree()

	return json_load


def analyze_property(prop, mode, json_load, parent_node):

	if prop not in json_load[mode]:
		return

	prop_keys = json_load[mode][prop]

	if 'type' in prop_keys:
		if prop_keys['type'] == 'object' and 'properties' in prop_keys:

			for sub_prop in prop_keys['properties']:
				if 'type' in prop_keys['properties'][sub_prop]:

					if prop_keys['properties'][sub_prop]['type'] == 'array':
						sub_prop_node = TreeNode(sub_prop, 'array')
						parent_node.add_child(sub_prop_node)
						if '$ref' in prop_keys['properties'][sub_prop]['items']:
							next_prop = prop_keys['properties'][sub_prop]['items']['$ref'].rsplit('/', 1)[-1]
							analyze_property(next_prop, 'definitions', json_load, sub_prop_node)

					elif prop_keys['properties'][sub_prop]['type'] in ["number", "integer", "boolean", "string"]:

						sub_prop_node = TreeNode(sub_prop, prop_keys['properties'][sub_prop]['type'])
						parent_node.add_child(sub_prop_node)

				elif '$ref' in prop_keys['properties'][sub_prop]:
					sub_prop_node = TreeNode(sub_prop, 'array')
					parent_node.add_child(sub_prop_node)
					next_prop = prop_keys['properties'][sub_prop]['$ref'].rsplit('/', 1)[-1]
					analyze_property(next_prop, 'definitions', json_load, sub_prop_node)

		if 'patternProperties' in prop_keys:

			patternKeys = prop_keys['patternProperties'].keys()
			for key in patternKeys:
				sub_prop = prop_keys['patternProperties'][key]['$ref'].rsplit('/', 1)[-1]
				analyze_property(sub_prop, 'definitions', json_load, parent_node)


		elif prop_keys['type'] == 'array':

			prop_node = TreeNode(prop, 'array')
			parent_node.add_child(prop_node)
			
			if '$ref' in prop_keys['items']:
				next_prop = prop_keys['items']['$ref'].rsplit('/', 1)[-1]
				analyze_property(next_prop, 'definitions', json_load, prop_node)

		elif prop_keys['type'] in ["number", "integer", "boolean", "string"]:

			prop_node = TreeNode(prop, prop_keys['type'])
			parent_node.add_child(prop_node)
			
	elif '$ref' in prop_keys:

		prop_node = TreeNode(prop, 'object')
		parent_node.add_child(prop_node)

		next_prop = prop_keys['$ref'].rsplit('/', 1)[-1]
		analyze_property(next_prop, 'definitions', json_load, prop_node)

	elif 'patternProperties' in prop_keys:

		patternKeys = prop_keys['patternProperties'].keys()
		for key in patternKeys:
			sub_prop = prop_keys['patternProperties'][key]['$ref'].rsplit('/', 1)[-1]
			analyze_property(sub_prop, 'definitions', json_load, parent_node)


def open_all_files(directory):
	"""Opens all files in a given directory."""

	for filename in os.listdir(directory):
		filepath = os.path.join(directory, filename)

		# Check if it's a file (not a directory)
		if os.path.isfile(filepath):
			try:
				with open(filepath, 'r') as file:
					d = json.load(file)
					if d['typeName'] not in ["MongoDB::Atlas::Cluster",
											"MongoDB::Atlas::Project",
											"MongoDB::Atlas::DatabaseUser",
											"MongoDB::Atlas::EncryptionAtRest",
											"MongoDB::Atlas::PrivateEndpointService",
											"MongoDB::Atlas::Trigger",
											"MongoDB::Atlas::ThirdPartyIntegration",
											"MongoDB::Atlas::CustomDBRole",
											"MongoDB::Atlas::ProjectIpAccessList"]:
						continue
						
					run(d)

			except Exception as e:
				print(f"Error opening {filename}: {e}")

if __name__ == '__main__':

	open_all_files("../mongodb_atlas_schemas")

	pass

