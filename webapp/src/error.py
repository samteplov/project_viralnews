
error_list = {
    "AUTH_ERROR":["AUTH_ERROR", "Unable to authenticate the twitter account."],
    "LMT_RCHD_ERROR":["LMT_RCHD_ERROR", "API rate limit has been reached. Please query later."],
    "FTCH_ERR" : ["FTCH_ERR", "An error occured while fetching the tweet object"],
    "MAL_TWT_URL" : ["MAL_TWT_URL", "The twitter url given to the application does not contain tweet id"],
    "MAL_URL" : ["MAL_URL", "Invalid Request URL"]
    }



class ApplicationError(Exception):
    def __init__(self, code, message):
        self._code = code
        self._message = message
    
    def __str__(self):
        return "Application Error {} : {}".format(self._code, self._message)