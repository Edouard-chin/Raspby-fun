<?php

require_once 'vendor/autoload.php';
require_once 'token.php';

$client = new \Github\Client();
$client->authenticate($accessToken, null, Github\Client::AUTH_HTTP_TOKEN);
$openedPullRequests = $client->api('pull_request')->all('upro', 'digitalevent');
$pullRequestsDetails = array();
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
	);
}

$mergeable = ($infos[0]['mergeable']) ? 'mergeable': 'non mergeable';
$text = urlencode($infos[0]['user'] . ' a ouvert une poule request ' . $mergeable . ' contenant ' . $infos[0]['commits'] . ' commits');

$output = shell_exec("./speech.sh {$text} {$ttsLang[array_rand($ttsLang)]}");
var_dump($output);exit();