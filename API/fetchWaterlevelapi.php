<?php
header('Content-Type: application/json');
include('db_config.php');

 $response = array();
 
 $checkQuery = "SELECT `wl_id`, `wl_value`, `device_id`, `reading_time` FROM `waterlevel`"; // change here.
 $result = mysqli_query($conn,$checkQuery);
 $numrow = mysqli_num_rows($result);
 
 if($result->num_rows == 0)
 {
$response["error"] = TRUE;
$response["message"] = "Sorry no waterlevel data found.";
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

$details['wl_id'] = $val['wl_id'];
$details['wl_value'] = $val['wl_value'];
$details['device_id'] = $val['device_id'];
$details['reading_time'] = $val['reading_time'];


array_push($data,$details);

}
}
$response["Waterlevel"] = $data; // change in response name.
$response["error"] = FALSE;
$response["message"] = "Successfully Waterlevel data Found.";
echo json_encode($response);
exit;
 }
 
?>

