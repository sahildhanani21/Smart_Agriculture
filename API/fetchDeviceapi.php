<?php
header('Content-Type: application/json');
include('db_config.php');

 $response = array();
 
 $checkQuery = "SELECT `device_id`, `login_id`, `issue_date` FROM `device`"; // change here.
 $result = mysqli_query($conn,$checkQuery);
 $numrow = mysqli_num_rows($result);
 
 if($result->num_rows == 0)
 {
$response["error"] = TRUE;
$response["message"] = "Sorry no Device data found.";
echo json_encode($response);
exit;
 }
 else
 {
 

$data = array();

for($i=1;$i<=$numrow;$i++)
{
while($val = mysqli_fetch_assoc($result))
{

$details['device_id'] = $val['device_id'];
$details['login_id'] = $val['login_id'];
$details['issue_date'] = $val['issue_date'];

array_push($data,$details);

}
}
$response["device"] = $data; // change in response name.
$response["error"] = FALSE;
$response["message"] = "Successfully device data Found.";
echo json_encode($response);
exit;
 }
 
?>

