import sys
import json
from collections import defaultdict

service = sys.argv[1]

with open('cfn-resource-spec.json') as f:
	d = json.load(f)
	prop_dict = defaultdict(list)
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			properties = d['ResourceTypes'][resource]['Properties'].keys()
			for property in properties:
				prop_dict[property].append(resource)

	for key, value in prop_dict.items():
		if len(value) > 1:
			print("\n"+key)
			for res_type in value:
				print(res_type)

