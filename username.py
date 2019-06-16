from flask import Flask,redirect,url_for,request,render_template
app=Flask(__name__)

@app.route("/")
def index():
   return render_template("test.html")


@app.route("/GetInput" , methods = ['POST'])
def GetInput():
    uname = request.form['username']
    password = request.form['password']
    print(uname)
    print(password)
    if((uname=='pasu')&(password=='12345')):
     return render_template('welcome.html')
    else:
     return render_template('wrong.html')

if __name__ == '__main__':
   app.run(debug = True)
