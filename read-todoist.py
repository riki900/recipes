#
# read todoist projects and tasks json files
#

import json
import pprint
import re
from   collections import Counter

projects_file_path = "json/projects.json"
tasks_file_path = "json/tasks.json"

with open (projects_file_path, "r") as proj_export:
    projs = json.load(proj_export)

with open (tasks_file_path, "r") as task_export:
    tasks = json.load(task_export)

pp = pprint.PrettyPrinter(indent=4)
#pp.pprint(tasks)

#for proj in projs['projects']:
#    print(f"{proj['id']} : {proj['name']}")

recipe_projs = [2213378915,2214514337]   

print(type(tasks))
print('scanning tasks')
# for task in tasks:
#     if task['project_id'] in recipe_projs and \
#        '//www.allrecipes.com' in task['content']:
#             print(task['content'])

tasks_list = {
    task['content']
    for task in tasks
    if task['project_id'] in recipe_projs and 'www.allrecipes.com' in task['content']
}

content_pattern = r'(?P<label>\[.+\])\((?P<url>.+)\)'
host_pattern = r'\/\/(.+?)\/'

content_re = re.compile(content_pattern)
host_re = re.compile(host_pattern)

hosts = []
urls = []
for task_content in tasks_list:
    try:
        label, url = content_re.findall(task_content)[0]
        hosts.append(host_re.findall(url)[0])
        urls.append(url)
    except IndexError as e:
        print(task_content)

with open('urls.txt', 'w') as f:
    for url in urls:
        f.write(f'{url}\n')
print('terminado')       





