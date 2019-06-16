from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/TestGet',Methods = ['GET'])
def TestGet():
      #print("Inside Get")
       #username = request.args.get('username')
      #password = request.args.get('password')
      #print("username is " + username)
      #print("password is " + password)
      return render_template("Test_Get(1).html")
      #return "YES THERE"
      #return redirect(url_for('success',name = user))


''''@app.route('/TestPOST',methods = ['POST'])
def T_POST():
      print("Inside Get")
      user = request.form('nm')
      print("value is " + user)
      return "Test POST"
      #return render_template("Test_Post.html")
      #return redirect(url_for('success',name = user))
'''



if __name__ == '__main__':
   app.run(debug = True)