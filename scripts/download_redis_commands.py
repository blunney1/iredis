#!/bin/python3

"""
Download all Reids commands from https://redis.io/commands.
Output to csv format.
"""
import sys
import csv

import lxml
from lxml import etree
import requests

stdout_writer = csv.writer(sys.stdout)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


eprint("Download https://redis.io/commands page...")
page = requests.get("https://redis.io/commands").text
eprint("Download finished!")

eprint("Start prase page...")
html = etree.HTML(page)
commands = html.xpath("//div[@class='container']/ul/li")
for command in commands:
    group = command.attrib['data-group']
    command_name = command.xpath("./a/span[@class='command']/text()")[0].strip()
    command_args = command.xpath("./a/span[@class='command']/span[@class='args']/text()")[0].strip()
    command_summary = command.xpath("./a/span[@class='summary']/text()")[0].strip()
    command_link = command.xpath("./a/@href")[0].strip()
    stdout_writer.writerow([
        group,
        command_name,
        " ".join(command_args.split()),
        command_summary,
        command_link,
    ])
eprint("Down.")