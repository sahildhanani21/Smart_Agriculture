<?php
header('Content-Type: application/json');
include('db_config.php');

 $response = array();
 
 $checkQuery = "SELECT `login_id`, `name`, `email_id`, `ph_no`, `password`, `role`, `status` FROM `login_table`"; // change here.
 $result = mysqli_query($conn,$checkQuery);
 $numrow = mysqli_num_rows($result);
 
 if($result->num_rows == 0)
 {
$response["error"] = TRUE;
$response["message"] = "Sorry no Login data found.";
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

$details['login_id'] = $val['login_id'];
$details['name'] = $val['name'];
$details['email_id'] = $val['email_id'];
$details['ph_no'] = $val['ph_no'];
$details['password'] = $val['password'];
$details['role'] = $val['role'];
$details['status'] = $val['status'];
array_push($data,$details);

}
}
$response["login"] = $data; // change in response name.
$response["error"] = FALSE;
$response["message"] = "Successfully login data Found.";
echo json_encode($response);
exit;
 }
 
?>

