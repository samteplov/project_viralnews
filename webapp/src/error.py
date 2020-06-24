
error_list = {
    "AUTH_ERROR":["AUTH_ERROR", "Unable to authenticate the twitter account."],
    "LMT_RCHD_ERROR":["LMT_RCHD_ERROR", "API rate limit has been reached. Please query later."],
    "FTCH_ERR" : ["FTCH_ERR", "An error occured while fetching the tweet object"],
    "MAL_TWT_URL" : ["MAL_TWT_URL", "The twitter url given to the application does not contain tweet id"],
    "MAL_URL" : ["MAL_URL", "Invalid Request URL."],
    "UNSUP_SRC" : ["UNSUP_SRC", "The provided url is not supported."],
    "UNBL_FTCH_NEWS" : ["UNBL_FTCH_NEWS", "Unable to fetch news article."],
    "NO_EMBD_URL" : ["NO_EMBD_URL","The tweet does not have an embeded URL."],
    "FILE_NT_FND" : ["FILE_NT_FND", "File not found in the request."],
    "URL_NT_FND" : ["URL_NT_FND" , "URL not found"]
    }


class ApplicationError(Exception):
    def __init__(self, code, message):
        self._code = code
        self._message = message
    
    def __str__(self):
        return "Application Error {} : {}".format(self._code, self._message)
    
    def to_dict(self):
        return {"error_code": self._code, "error_msg" : self._message}