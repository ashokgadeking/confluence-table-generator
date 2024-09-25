import sys
import json
from collections import defaultdict
import requests
from bs4 import BeautifulSoup

service = sys.argv[1]

with open('cfn-resource-spec.json') as f:
	d = json.load(f)
	sub_prop_url = ""
	for resource in d['ResourceTypes'].keys():
		if service in resource:
			with open(resource.strip(":")+".md", "w") as f:
				f.write('||No.||Property||Description||Type||Threat Context||GR Required||Jira Story\n')
				print("\n"+resource)
				properties = d['ResourceTypes'][resource]['Properties'].keys()
				i=1
				for property in properties:
					url = d['ResourceTypes'][resource]['Properties'][property]['Documentation']
					response = requests.get(url)
					soup = BeautifulSoup(response.content, "html.parser")
					tag = soup.find(id=url.split("#",1)[1])
					desc = str(tag.next_sibling.p.get_text())
					while desc.find("  ") != -1:
						desc = desc.replace("  ", " ")
					cleaned_desc = desc.replace('\t','').replace('\n','')
					parent_tag = tag.next_sibling.find_all(string="Type")[0].parent.parent
					sub_prop_type = str(parent_tag).split(" ",1)[1][:-4]
					stripped_url = url.rsplit("/",1)[0] + "/"
					f.write('|'+ str(i) + '|' + property + '|' + cleaned_desc + '|' + sub_prop_type.replace('./', stripped_url) + '|' + '' + '|' + '' + '|' + '' + '|\n')
					i+=1