#!/usr/bin/env python
import sys
import os
from piazza_api import Piazza
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from pprint import pprint

def piazza_parse(pi_url):
    temp = ""
    p = Piazza()
    p.user_login(email=os.environ['EMAIL'], password=os.environ['PASSWORD'])
    classes = p.get_user_classes()

    #piazza_url = urlparse(sys.argv[1])
    piazza_url = urlparse(pi_url)

    class_id = piazza_url.path.split('/')[2]
    post_num = piazza_url.query.split('=')[1]
    
    # Returns a class network
    class_net = p.network(class_id)

    post = class_net.get_post(post_num)

    class_name = "None"
    for i in classes:
        if i['nid'] == class_id:
            class_name = i['num']
    question = post["history"][0]["content"]
    subject = post["history"][0]["subject"]

    # print("QUESTION JSON")
    # print('-----------------')
    # print(post["history"][0])
    # print()

    temp += "__**CLASS NAME**__\n"
    temp += class_name + '\n\n'
    temp += "__**SUBJECT**__\n"
    temp += subject + '\n\n'


    # Content of post that includes html tags
    #
    # print("CONTENT")
    # print('-----------------')
    # print(question)
    # print()

    temp += "__**CONTENT**__\n"
    question_text = BeautifulSoup(question, features='lxml').text
    temp += question_text + '\n\n'

    answers = post["children"]
    print()

    temp += "__**ANSWERS**__\n"
    #TODO concatenate all answers? or just one
    #temp += answers

    return temp

piazza_parse('https://piazza.com/class/k84o7ugzfyn2l7?cid=681')

    