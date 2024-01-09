class CloudShellClient:
    """Client class for Cloud Shell API."""
    
    def operations(self):
        """Returns the operations Resource."""
        pass
    
    def users(self):
        """Returns the users Resource."""
        pass
    
    def close(self):
        """Close httplib2 connections."""
        pass
    
    def new_batch_http_request(self, callback):
        """Create a BatchHttpRequest object based on the discovery document."""
        pass
