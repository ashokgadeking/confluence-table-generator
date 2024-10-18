import sys
import json
from collections import defaultdict

# resource = sys.argv[1]
# prop_or_subprop = sys.argv[2]

skip_properties = ["Description", "Tags"]

def detect_gr_type(property):
	same_app_keywords = ["Arn","Role"]
	if any(keyword in property for keyword in same_app_keywords):
	    gr_type = "same app ARN"
	else:
		gr_type = "[INSERT GR TYPE]"
	return gr_type

def write_description(f, service, property, resources, spec_file, mode):
	f.write('-----------------------------------\n')
	f.write('Story Title\n')
	gr_type = detect_gr_type(property)
	if mode == 'ResourceTypes':
		prop_type = 'property'
	else:
		prop_type = 'sub-property'
	prefix=""
	if len(resources) > 1:
		f.write('[AWS::'+service+' common '+prop_type+'] Control: Ensure common '+prop_type+' '+property+' is '+gr_type+'\n\n')
		f.write('Description\n\n')
		f.write('This story addresses a common '+prop_type+' among multiple resources/properties (listed below) in AWS '+
			service+'. Please note that the context might vary across resources/properties for the same property.\n\n')
	else:
		f.write('['+resources[0]+'] Control: Ensure '+prop_type+' '+property+' is '+gr_type+'\n\n')
		f.write('Description\n\n')

	for resource in resources:
		f.write(resource+'\n')
		prop_url = spec_file[mode][resource]['Properties'][property]['Documentation']
		f.write(prop_url+'\n\n')

	f.write('\nh2. Proposed OPA Control Definition\n')

	for resource in resources:
		if mode == 'PropertyTypes':
			resource_name = resource.split(".",1)[0]
			property_name = resource.split(".",1)[1]
			f.write('The '+resource+' property exposes the following '+prop_type+':\n')
		else:
			resource_name = resource
			f.write('The '+resource+' resource exposes the following '+prop_type+':\n')
		
		f.write('{code:javascript}\n')
		f.write('{\n')
		f.write('\t"Type": "'+resource_name+'",\n')
		f.write('\t"Properties" : {\n')

		if 'PrimitiveType' in spec_file[mode][resource]['Properties'][property]:
			data_type = spec_file[mode][resource]['Properties'][property]['PrimitiveType']
		elif 'Type' in spec_file[mode][resource]['Properties'][property]:
			data_type = spec_file[mode][resource]['Properties'][property]['Type']
		
		if mode == 'PropertyTypes':
			f.write('\t\t"'+property_name+'" : {\n')
			f.write('\t\t\t"'+property+'" : '+data_type+'\n')
			f.write('\t\t}\n')
		else:
			f.write('\t\t"'+property+'" : '+data_type+'\n')

		f.write('\t}\n')
		f.write('}\n')
		f.write('{code}\n\n')

	if mode == 'PropertyTypes':
		f.write('{*}ID{*}: *'+service.lower()+'.'+property.lower()+'_subprop_'+'is'+'_'+gr_type.replace(' ','_')+'*\n')
	else:
		f.write('{*}ID{*}: *'+service.lower()+'.'+property.lower()+'_'+'is'+'_'+gr_type.replace(' ','_')+'*\n')

	f.write('{*}Implementation{*}:\n')
	f.write('\t * If '+property+' is '+gr_type+', allow.\n')
	f.write('\t * Otherwise deny\n')

def detect_common_props_and_subprops(d, mode, resource, service):

	prop_dict = defaultdict(list)
	for resource in d[mode].keys():
		if service in resource:
			properties = d[mode][resource]['Properties'].keys()
			for property in properties:
				prop_dict[property].append(resource)

	return prop_dict


with open('cfn-resource-spec.json') as f:
		d = json.load(f)

if sys.argv[1] == 'help':
	print('For common props, specify any resource. Eg. $python generate_stories.py AWS::DMS::Endpoint KmsKeyId')
	print('For common sub-props, specify any resource.property. Eg. $python generate_stories.py AWS::DMS::Endpoint.RedisSettings ServerName')

if '.' in sys.argv[1]:
	resource = sys.argv[1].split(".",1)[0]
	service = resource.split("::",3)[1]
	sub_prop = sys.argv[2]
	prop_dict = detect_common_props_and_subprops(d, 'PropertyTypes', resource, service)

	for key, values in prop_dict.items():
		if key not in skip_properties:
			if key == sub_prop:
				with open(sub_prop+"_jira_story.txt", "w") as f:
					print(key + ' ' + str(values))
					write_description(f, service, sub_prop, values, d, 'PropertyTypes')

else:
	resource = sys.argv[1]
	service = resource.split("::",3)[1]
	property = sys.argv[2]

	prop_dict = detect_common_props_and_subprops(d, 'ResourceTypes', resource, service)

	for key, resources in prop_dict.items():
		if key not in skip_properties:
			if key == property:
				with open(property+"_jira_story.txt", "w") as f:
					gr_type=""
					print(key + ' ' + str(resources))
					write_description(f, service, property, resources, d, 'ResourceTypes')



