<?php
header('Content-Type: application/json');
include('db_config.php');

 $response = array();
 
 $checkQuery = "SELECT `sec_id`, `sec_value`, `device_id`, `reading_time` FROM `security`"; // change here.
 $result = mysqli_query($conn,$checkQuery);
 $numrow = mysqli_num_rows($result);
 
 if($result->num_rows == 0)
 {
$response["error"] = TRUE;
$response["message"] = "Sorry no Security data found.";
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

$details['sec_id'] = $val['sec_id'];
$details['sec_value'] = $val['sec_value'];
$details['device_id'] = $val['device_id'];
$details['reading_time'] = $val['reading_time'];


array_push($data,$details);

}
}
$response["security"] = $data; // change in response name.
$response["error"] = FALSE;
$response["message"] = "Successfully Security data Found.";
echo json_encode($response);
exit;
 }
 
?>

