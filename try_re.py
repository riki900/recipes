import re

task_content = '"[Spicy Lime Avocado Soup Recipe - Allrecipes.com](https://www.allrecipes.com/recipe/246841/spicy-lime-avocado-soup/?internalSource=hub%20recipe\u0026referringContentType=Search)",'

#url_re = r'(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/?[a-z0-9])+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)'
#url_re = r'(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/?[a-z0-9])+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)'

content_pattern = r'(?P<label>\[.+\])\((?P<url>.+)\)'
host_pattern = r'\/\/(.+?)\/'

content_re = re.compile(content_pattern)
host_re = re.compile(host_pattern)

label, url = content_re.findall(task_content)[0]

print(host_re.findall(url))

