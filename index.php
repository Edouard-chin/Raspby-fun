#!/usr/bin/php
<?php

require_once 'vendor/autoload.php';
require_once 'token.php';

$client = new \Github\Client();
$client->authenticate($accessToken, null, Github\Client::AUTH_HTTP_TOKEN);
$openedPullRequests = $client->api('pull_request')->all('upro', 'digitalevent');
$pullRequestsDetails = array();
$infos = array();
$ttsLang = array(
    'en',
    'ja',
    'de',
    'tr',
);
foreach ($openedPullRequests as $value) {
    $pullRequestsDetails[] = $client->api('pull_request')->show('upro', 'digitalevent', $value['number']);
}
foreach ($pullRequestsDetails as $value) {
    $infos[] = array(
        'user' => $value['user']['login'],
        'mergeable' => $value['mergeable'],
        'commits' => $value['commits'],
        'updatedAt' => strtotime($value['updated_at']),
    );
}

var_dump($infos[0]['updatedAt']);exit();
if (empty($infos)) {
    return ;
} elseif (time() - $infos[0]['updatedAt'] > 90) {
    // return;
}
$mergeable = ($infos[0]['mergeable']) ? 'mergeable': 'non mergeable';
$text = urlencode($infos[0]['user'] . ' a ouvert une poule request ' . $mergeable . ' sur digital event, contenant ' . $infos[0]['commits'] . ' commits');

putenv("SHELL=xterm");
$output = shell_exec("/home/echin/exos/Raspby-fun/speech.sh {$text} {$ttsLang[array_rand($ttsLang)]}");
