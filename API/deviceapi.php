<?php
header('Content-Type: application/json');
include('db_config.php');

$response = array();



if(isset($_GET["login_id"]) && isset($_GET["issue_date"]))
{
	  


	$login_id = $_GET["login_id"];  
	$issue_date = $_GET["issue_date"];
	  



	  $query = "INSERT INTO `device`(login_id,issue_date) VALUES('$login_id',CURRENT_TIMESTAMP())";
	  $result = mysqli_query($conn,$query);
	//   2022-10-05
	
	
	  
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