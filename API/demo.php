<?php
$api_url =
   "https://agriitech.000webhostapp.com/API/fetchSecurityapi.php?"
// "https://agriitech.000webhostapp.com/API/fetchSecurityapi.php?apikey=d6yErgxbF1QPuues9PWobdHFFJh2"; 
// $api_url =
// "http://cricapi.com/api/fantasySummary?apikey=<apikey>&unique_id=cunique_ id>"

// Initiate curl
$ch = curl_init();
// Disable SSL verification
// curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); 
// Will return the response, if false it print the response 
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
// Set the url
curl_setopt($ch, CURLOPT_URL, $api_url);
// Execute
$result=curl_exec($ch);
// Closing
curl_close($ch);
$demo=json_decode($result);
echo "<pre>";
print_r($demo);
?>