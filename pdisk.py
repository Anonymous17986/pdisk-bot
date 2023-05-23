import  requests as re
import json 
def pdisk_url(api_key:str , link:str , title :str , thumb = None ):
		if thumb :
			data = { "api_key":api_key,
	                   "content_src":link,
	                    "link_type":"link",
	                     "title": title,
	                     "cover_url":thumb
	                  } 	
			res = re.post("https://pdisk.pro/api/upload/server?key",data).content
			result = json.loads(res)
			return result
		else:
			data = { "api_key":api_key,
	                   "content_src":link,
	                    "link_type":"link",
	                     "title": title ,
	                  }
			res = re.post('https://pdisk.pro/api/upload/server?key',data).content
			result = json.loads(res)
			return result 
			
def api_check(api_key):
	data = {"api_key":api_key}
	res = re.get('https://fs9.pdisk.pro/cgi-bin/upload.cgi',data).content
	result = json.loads(res)
	return result
				                                                                                                                                                      				                                                                                                           
