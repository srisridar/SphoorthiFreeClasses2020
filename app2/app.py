from flask import Flask
from flask import render_template
import requests
import json


app = Flask(__name__)



@app.route('/')
def home():
	resp=requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q=nagpur&cnt=10&mode=json&units=metric&APPID=2d80cf7142a085e6c34f383205d35118#").text
	weatherdata=json.loads(resp)
	mx_temp=weatherdata.get('list')[0].get('temp').get('max')
	mn_temp=weatherdata.get('list')[0].get('temp').get('min')
	name="Sreedhar"
	return render_template("home.html", mx=mx_temp,mn=mn_temp,nme=name)


@app.route('/weather/<placename>')
def dmp(placename):
	resp=requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q=%s&cnt=10&mode=json&units=metric&APPID=2d80cf7142a085e6c34f383205d35118#"%(placename))
	data=resp.text
	weatherdata=json.loads(data)
	table=""
	for eachday in weatherdata.get('list'):
		table=table+"""<tr><td>%s</td><td>%s</td><td>%s</td></tr>"""%(eachday.get('temp').get('max'),eachday.get('temp').get('min'),eachday.get('weather')[0].get('description'))
	return render_template("weather.html",tabledata=table,placename=placename.title())


@app.route('/guruji')
def guruji():
    return """
    """
    
@app.route('/contactus/<name>')
def address(name):
	nme=name
	return render_template("contactus.html",somevalue=nme)



# main app run
if __name__ == '__main__':
	app.run(debug=True)        