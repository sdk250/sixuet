from flask import request, Response, Flask
from re import compile
from datetime import datetime
from hashlib import md5
from json import loads, dumps

app = Flask(__name__)

@app.route(rule = "/")
def __init__():
	cookies = open("any.cookies", "ab+")
	if "Token" in request.cookies.keys():
		example = Response("Hi, World!")
		print(compile("^([a-z0-9]+[^= ]) ?= ?(.+)$").findall(cookies.readline().decode("UTF-8")))
		
		# example.response = value
	else:
		example = Response("Hello, World!")
		token = md5(str(datetime.now()).encode("UTF-8")).hexdigest()
		Response.set_cookie(self = example, key = "Token", value = token, max_age = 60)
		data = 
		cookies.write(
			bytes(
				dumps(
					[
						{
							token: dict(request.args)
						}
					]
				) + "\n", encoding = "UTF-8"
			)
		)
	# for i in request.args.keys():
	# 	print(i, request.args[i])
	# 	print(dict(request.args))
	cookies.close()
	return example

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 20800, debug = True)