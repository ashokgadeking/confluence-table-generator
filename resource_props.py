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
			with open(resource.strip(":")+".html", "w") as f:
				f.write('<table style="border-collapse: collapse;">')
				f.write("<tr style=border: 1px solid #000;>")
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">No.</th>')
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">Property</th>')
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">Description</th>')
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">Type</th>')
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">Threat Context</th>')
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">GR Required</th>')
				f.write('<th style=border: 1px solid #000; background-color: #FFF;">JIRA Story</th>')
				f.write('</tr>')
				print("\n"+resource)
				properties = d['ResourceTypes'][resource]['Properties'].keys()
				i=1
				for property in properties:
					url = d['ResourceTypes'][resource]['Properties'][property]['Documentation']
					response = requests.get(url)
					soup = BeautifulSoup(response.content, "html.parser")
					tag = soup.find(id=url.split("#",1)[1])
					f.write("<tr style=border: 1px solid #000;>")
					f.write("<td style=border: 1px solid #000;>"+str(i)+"</td>")
					i+=1
					f.write("<td style=border: 1px solid #000;>"+property+"</td>")
					desc = str(tag.next_sibling.p.get_text())
					while desc.find("  ") != -1:
						desc = desc.replace("  ", " ")
					cleaned_desc = desc.replace('\t','').replace('\n','')
					f.write("<td style=border: 1px solid #000;>"+cleaned_desc+"</td>")
					parent_tag = tag.next_sibling.find_all(string="Type")[0].parent.parent
					sub_prop_type = str(parent_tag).split(" ",1)[1][:-4]
					stripped_url = url.rsplit("/",1)[0] + "/"
					f.write("<td style=border: 1px solid #000;>"+sub_prop_type.replace('./', stripped_url)+"</td>")
					f.write("<tr>")
				f.write('</table>')