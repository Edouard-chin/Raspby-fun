#!/usr/bin/python
# coding=UTF-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask
from flask import request
from subprocess import call
import json

app = Flask(__name__)
users = {'Edouard-chin': 'édouard', 'rlustin': 'Rafhael', 'aldeck': 'Alexandre', 'cthoret': 'Clément', 'alexandra-ekra': 'Alexandra', 'jvasseur': 'Jérome', 'FlorianLepot': 'Florian'}

@app.route("/payload/pullrequest", methods=['POST'])
def pullrequest():
    data = json.loads(request.data)
    state = data['action']
    wasMerged = {True: 'successfully merged', False: 'not merged'}
    isMergeable = {True: 'can', False: "can not", None: 'I am not sure if it can'}
    pullrequest = data['pull_request']
    if state == 'opened' or state == 'reopened':
        speech = 'New pull request on: ' + pullrequest['base']['repo']['name'] + '. ' + users[pullrequest['user']['login']] + ' want to merge his branch: ' \
        + pullrequest['head']['ref'] + ', in the ' + pullrequest['base']['ref'] + ' branch, containing ' + str(pullrequest['commits']) + ' commit. This pull request ' \
        + isMergeable[pullrequest['mergeable']] + ' be automatically merged.'
        call(["./speech.sh", speech])

    elif state == 'closed':
        speech = 'The pull request of: ' + users[pullrequest['user']['login']] + ' is now closed and was ' + wasMerged[pullrequest['merged']]
        call(["./speech.sh", speech])

    elif state == 'assigned':
        speech = users[pullrequest['assignee']['login']] + ', you have been assigned to check the pull request of: ' + users[pullrequest['user']['login']]
        call(["./speech.sh", speech])

    return "All good!"

@app.route("/payload/pullrequest-review", methods=['POST'])
def pull_review():
    data = json.loads(request.data)
    pullrequest = data['pull_request']
    comment = data['comment']
    speech = users[pullrequest['user']['login']] + ', ' + users[comment['user']['login']] + ' commented on your pull request. Go check it.'
    call(["./speech.sh", speech])
    return 'All good!'

if __name__ == "__main__":
    app.run(debug=True)
