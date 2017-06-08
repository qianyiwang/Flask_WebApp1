from flask import Flask, render_template, request, json, jsonify

app = Flask(__name__)
global data
data = 0

@app.route('/')
def index():
	global data
	if data == 0:
		return "No Data"
	else:
		d = data
		data = 0
		return "<h1>Data: %s<h1>" % d

@app.route('/receiveData/', methods = ['POST', 'GET'])
def receiveData():
    jsondata = request.get_json()
    global data
    data = json.loads(jsondata)['Data']
    print data
    # #stuff happens here that involves data to obtain a result

    result = {'escalate': True}
    return json.dumps(result)


if __name__ == '__main__':
	app.run(debug=True)