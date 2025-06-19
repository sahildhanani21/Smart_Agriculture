<?php
header('Content-Type: application/json');
include('db_config.php');

 $response = array();
 
 $checkQuery = "SELECT `rain_id`, `rain_value`, `device_id`, `reading_time` FROM `rain`"; // change here.
 $result = mysqli_query($conn,$checkQuery);
 $numrow = mysqli_num_rows($result);
 
 if($result->num_rows == 0)
 {
$response["error"] = TRUE;
$response["message"] = "Sorry no rain data found.";
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

$details['rain_id'] = $val['rain_id'];
$details['device_id'] = $val['device_id'];
$details['rain_value'] = $val['rain_value'];
$details['reading_time'] = $val['reading_time'];
array_push($data,$details);

}
}
$response["rain"] = $data; // change in response name.
$response["error"] = FALSE;
$response["message"] = "Successfully rain Sensor data Found.";
echo json_encode($response);
exit;
 }
 
?>

