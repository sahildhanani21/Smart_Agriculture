<?php
header('Content-Type: application/json');
include('db_config.php');

$response = array();



if(isset($_GET["name"]) && isset($_GET["email_id"]) && isset($_GET["ph_no"]) && isset($_GET["password"]) && isset($_GET["role"]) && isset($_GET["status"]))
{
	  

	  $name = $_GET["name"];
	  $email_id = $_GET["email_id"];
	  $ph_no = $_GET["ph_no"];
	  $password = $_GET["password"];
	  $role = $_GET["role"];
	  $status = $_GET["status"];

	  $query = "INSERT INTO `login_table`(name, email_id, ph_no, password, role, status) VALUES('$name','$email_id','$ph_no','$password','$role','$status')";
	  $result = mysqli_query($conn,$query);
	  
	
	
	  
	  if($result)
	  {
	
		  
			  $response["error"] = FALSE;
			  $response["message"] = "Successfully added.";
			  echo json_encode($response);
			  exit;
	  }
	  else
	  {
		  
	  	  $response["error"] = TRUE;
		  $response["message"] = "Sorry not able to insert";
		  $response["errr"] = mysqli_error($conn);
		  echo json_encode($response);
			  
		  
	  }
}
  else
  {
	  //Invalid parameters
	  $response["error"] = TRUE;
	  $response["message"] = "Invalid Parameters";
	 
	  echo json_encode($response);
	  exit;
  }
?>