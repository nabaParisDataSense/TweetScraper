import json,falcon
from scrapy import cmdline

class ObjRequestClass:
	def on_get(self, req, resp):
		resp.status = falcon.HTTP_200

		validate_params = True

		if 'search' not in req.params:
			validate_params = False

		if(validate_params is True):
			output = {
				'search' : req.params['search']
			}
		else:
			output = {
				'error' : 'parameter missing'
			}

		resp.body = json.dumps(output)

#		if(validate_params is True):
#			cmdline.execute("scrapy crawl TweetScraper -a query=",req.params['query'].split())

api=falcon.API()
api.add_route('/params',ObjRequestClass())
