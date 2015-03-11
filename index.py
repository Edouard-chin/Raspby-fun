#!/usr/bin/python
# coding=UTF-8

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

from flask import Flask, abort
from flask import request
from subprocess import call
import json
import random
import os

app = Flask(__name__)
users = {'Edouard-chin': 'édouard', 'rlustin': 'Rapha elle', 'aldeck': 'Alexandre', 'cthoret': 'Clément', 'alexandra-ekra': 'Alexandra', 'jvasseur': 'Jérome', 'FlorianLepot': 'Florian', 'amorin274': 'Adrien'}


@app.route("/payload/pullrequest", methods=['POST'])
def pullrequest():
    data = json.loads(request.data)
    state = data['action']
    wasMerged = {True: 'successfully merged', False: 'not merged'}
    isMergeable = {True: 'can', False: "can not", None: ""}
    pullrequest = data['pull_request']
    if state == 'opened' or state == 'reopened':
        speech = 'New pull request on: ' + pullrequest['base']['repo']['name'] + '. ' + users[pullrequest['user']['login']] + ' wants to merge his branch: ' \
        + pullrequest['head']['ref'] + ', in the ' + pullrequest['base']['ref'] + ' branch, containing ' + str(pullrequest['commits']) + ' commit. This pull request ' \
        + isMergeable[pullrequest['mergeable']] + ' be automatically merged.'
        forkMe(speech, 'en-US')

    elif state == 'closed':
        speech = 'The pull request of: ' + users[pullrequest['user']['login']] + ' is now closed and was ' + wasMerged[pullrequest['merged']]
        forkMe(speech, 'en-US')

    elif state == 'assigned':
        speech = users[pullrequest['assignee']['login']] + ', you have been assigned to review the pull request of: ' + users[pullrequest['user']['login']]
        forkMe(speech, 'en-US')

    return "All good!"

@app.route("/payload/pullrequest-review", methods=['POST'])
def pull_review():
    data = json.loads(request.data)
    pullrequest = data['pull_request']
    comment = data['comment']
    speech = users[pullrequest['user']['login']] + ', ' + users[comment['user']['login']] + ' commented on your pull request. Go check it.'
    forkMe(speech, 'en-US')

    return 'All good!'

@app.route("/cron/good-morning", methods=['GET'])
def cron_goodMorning():
    if not check_ip():
        abort(401)
    return forkMe('Bonjour tout le monde. Il est 9 heures 45, passez une bonne journée.', 'fr-FR')

@app.route("/cron/time-to-eat", methods=['GET'])
def cron_timeToEat():
    store = ['Sumita', 'Luigi', 'Picard', 'Kebab', 'Subway', 'Repas a L\'anjou', 'Repas au café L\'express']
    if not check_ip():
        abort(401)
    return forkMe("Il va bientot être l'heure de manger. Je vous propose aujourd'hui d'aller se faire un: " + random.choice(store), 'fr-FR')


@app.route("/cron/random", methods=['GET'])
def cron_random():
    if not check_ip():
        abort(401)
    json_data=open('randomSentences.json')
    data = json.load(json_data)
    speech = random.choice(data['sentences'])
    json_data.close()
    return forkMe(speech, 'fr-FR')

def speak(sentence, lang):
    call(["./speech.sh", sentence, lang])
    os._exit(0)

def forkMe(sentence, lang):
    newpid = os.fork()
    if newpid == 0:
         speak(sentence, lang)
    else:
        return "All good marmoud!"

def check_ip():
    allowedIps = ['142.4.201.54', '198.27.81.134', '127.0.0.1', '89.156.7.131']
    ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
    return ip in allowedIps

if __name__ == "__main__":
    app.run()
