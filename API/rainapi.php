<?php
header('Content-Type: application/json');
include('db_config.php');

$response = array();



if(isset($_GET["rain_value"]))
{
	  

	  $rain_value = $_GET["rain_value"];
	  

	  $query = "INSERT INTO `rain`(`rain_id`, `rain_value`, `device_id`, `reading_time`) VALUES('$rain_value',CURRENT_TIMESTAMP(),'$device_id')";
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
  
//   SMS API
