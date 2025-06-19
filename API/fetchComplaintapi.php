<?php
header('Content-Type: application/json');
include('db_config.php');

 $response = array();
 
 $checkQuery = "SELECT `complaint_id`, `login_id`, `description`, `complaint_type`, `complaint_time` FROM `complaint_table`"; // change here.
 $result = mysqli_query($conn,$checkQuery);
 $numrow = mysqli_num_rows($result);
 
 if($result->num_rows == 0)
 {
$response["error"] = TRUE;
$response["message"] = "Sorry no Complaint data found.";
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

$details['complaint_id'] = $val['complaint_id'];
$details['login_id'] = $val['login_id'];
$details['description'] = $val['description'];
$details['complaint_type'] = $val['complaint_type'];
$details['complaint_time'] = $val['complaint_time'];

array_push($data,$details);

}
}
$response["Complaint"] = $data; // change in response name.
$response["error"] = FALSE;
$response["message"] = "Successfully Complaint data Found.";
echo json_encode($response);
exit;
 }
 
?>

