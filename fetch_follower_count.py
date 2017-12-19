#! /usr/local/bin/python2
from lxml import html
import requests

url = 'https://twitter.com/mikhail_advani'
follower_count_identifier = '//li[@class="ProfileNav-item ProfileNav-item--followers"]/a/span[@class="ProfileNav-value"]'
count_file_name = 'twitter_follower_count.json'

page = requests.get(url)
tree = html.fromstring(page.content)

count = tree.xpath(follower_count_identifier)[0].text
json_content = "{\"count\":%s}" % count

count_file = open(count_file_name, 'w')
count_file.write(json_content)

