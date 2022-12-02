from flask import request, Response, Flask, render_template
from re import compile
from datetime import datetime
from hashlib import md5
from time import time
from json import loads, dumps

app = Flask(__name__)

@app.route(rule = "/")
def __init__():
	if "Token" in request.cookies.keys():
		cookies = open("any.cookies", "rb")
		example = Response(render_template("__init__.html", title = "Test", content = "Hi, World!"))
		print(loads(cookies.read().decode("UTF-8")))
		cookies.close()
	else:
		example = Response(render_template("__init__.html", title = "Test", content = "Hello, World"))
		token = md5(str(datetime.now()).encode("UTF-8")).hexdigest()
		Response.set_cookie(self = example, key = "Token", value = token, max_age = 60)
		cookies = open("any.cookies", "rb")
		save_cookies = loads(cookies.read().decode("UTF-8"))
		cookies.close()
		cookies = open("any.cookies", "wb")
		data = dict(request.args)
		data["max_age"] = int(time()) + 60
		save_cookies[token] = data
		print(save_cookies)
		cookies.write(
			bytes(
				dumps(
					save_cookies
				)
				+ "\n", encoding = "UTF-8"
			)
		)
		cookies.close()
	return example

if __name__ == "__main__":
	app.run(host = "0.0.0.0", port = 20880, debug = True)