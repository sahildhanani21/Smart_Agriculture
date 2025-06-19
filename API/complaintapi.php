<?php
header('Content-Type: application/json');
include('db_config.php');

$response = array();



if(isset($_GET["description"]) && isset($_GET["complaint_type"]))
{
	  

	  $description = $_GET["description"];
      $complaint_type = $_GET["complaint_type"];

	  $query = "INSERT INTO `complaint_table`(description,complaint_type,complaint_time) VALUES('$description','$complaint_type',CURRENT_TIMESTAMP())";
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