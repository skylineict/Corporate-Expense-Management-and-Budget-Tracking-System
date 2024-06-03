import facebook

class Facebook():
    @staticmethod
    def validate(access_token):
        try:
            graph =facebook.GraphAPI(access_token=access_token)
            profile = graph.request('/me?fields=name,email')
            return profile
        except Exception as e:
            raise Exception("token is not active")



