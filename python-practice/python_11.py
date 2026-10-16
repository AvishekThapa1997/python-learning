def get_service_metrics():
    return {
       "total_requests": 120, 
       "successful": 105, 
       "failed": 10, 
       "retries": 3, 
       "timeouts": 2  
    }


print(type(get_service_metrics()))
