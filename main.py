from flask import Flask, render_template, request, json, redirect, url_for
from datetime import datetime
import pygal

app = Flask(__name__)
global data, time
data = []
time = []

@app.route('/')
def Welcome():
    global data, time
    print data, time
    try:
    	graph = pygal.Line()
    	graph.title = "% Data Received"
    	graph.x_labels = time
    	graph.add('Data', data)
    
    	graph_data = graph.render_data_uri()
    	return render_template('graphing.html', graph_data=graph_data)
    except Exception, e:
    	return(str(e))

@app.route('/receiveData/', methods = ['POST', 'GET'])
def receiveData():
    global data
    jsondata = request.get_json()
    d = json.loads(jsondata)['Data']
    data.append(int(d))
    time.append(str(datetime.now()))
    print "DEBUG: ", d
    result = {'escalate': True}
    # return json.dumps(result)
    return render_template('showData.html', data=d)


@app.route('/update')
def request():
    return app.send_static_file('graphing.html')


def calculateVal(val):
	return val*2-1

if __name__ == '__main__':
	app.run(debug=True)