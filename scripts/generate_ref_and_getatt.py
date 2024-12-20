import sys
import json
import requests
from bs4 import BeautifulSoup

# This script generates ref and get-att values for an AWS resource. This script only support AWS Cloudformation
# resources. 3rd party resources are not supported.

# Usage python ./generate_ref_and_getatt.py AWS::QuickSight::DataSet

service = sys.argv[1]

def get_ref_and_getatt(resource):

	resource_url = d['ResourceTypes'][resource]['Documentation']

	response = requests.get(resource_url)
	soup = BeautifulSoup(response.content, "html.parser")

	service = resource.split("::",3)[1]
	resource_name = resource.split("::",3)[2]

	tag = soup.find(id="aws-resource-"+service.lower()+"-"+resource_name.lower()+"-return-values-ref")

	if tag is not None:
		ref_desc=""
		if tag.next_sibling.name == 'p':
			print('\n\n'+resource+'\n')
			ref_desc = tag.next_sibling.get_text(strip=True).replace('\n','')
			if ref_desc.endswith('For example:'):
				ref_desc += ' '+tag.next_sibling.next_sibling.get_text(strip=True).replace('\n','')
			print(' '.join(ref_desc.split()))

with open('../input_json_spec_files/cfn-resource-spec.json') as f:
	d = json.load(f)
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			get_ref_and_getatt(resource)