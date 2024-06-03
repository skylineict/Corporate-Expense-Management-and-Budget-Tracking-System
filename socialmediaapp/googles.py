from google.oauth2 import id_token
from  google.auth.transport import requests

class Google:
    @staticmethod
    def validate(access_token):
        try:
            id_info = id_token.verify_oauth2_token(access_token, requests.Request())
            myid =  {

                "myid": id_info

            }

            # print(myid)
            
            # Verify the issuer of the token
            if id_info['iss'] not in ['accounts.google.com', 'https://accounts.google.com']:
                raise ValueError('Wrong issuer.')
            
            return id_info
        except ValueError as e:
            raise Exception(f"Token validation error: {e}")
        except Exception as e:
            raise Exception(f"An error occurred during token validation: {e}")

                                                                                                                                                                        
