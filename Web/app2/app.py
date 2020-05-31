from flask import Flask
from flask import render_template


app = Flask(__name__)



@app.route('/')
def home():
    mx_temp=45.54
    mn_temp=24.25
    return render_template("home.html", mx=mx_temp,mn=mn_temp)

@app.route('/weather')
def dmp():
    return render_template("weather.html")


@app.route('/guruji')
def guruji():
    return """
    """
    
@app.route('/contactus')
def address():
    return render_template("contactus.html")



# main app run
if __name__ == '__main__':
	app.run(debug=True)        