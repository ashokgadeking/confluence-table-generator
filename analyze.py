import sys
import json
from collections import defaultdict

service = sys.argv[1]

with open('cfn-resource-spec.json') as f:
	d = json.load(f)
	prop_dict = defaultdict(list)
	for resource in d['PropertyTypes'].keys():
		if service in resource:
			properties = d['PropertyTypes'][resource]['Properties'].keys()
			for property in properties:
				prop_dict[property].append(resource)

with open(service + '_common_props' + ".md", "w") as f:
	f.write('||Property||Resources\n')
	for key, value in prop_dict.items():
		if len(value) > 1:
			line = '|' + key + '|'
			for res_type in value:
				line += res_type + " \\\\ "
			f.write(line+'|\n')
