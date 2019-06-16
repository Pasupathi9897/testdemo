'''from flask import Flask, redirect, url_for, request,render_template
app = Flask(__name__)

@app.route('/TestGet',methods = ['GET'])
def T_GET():
      print("Inside Get")
      return render_template("Test_Get.html")

"""

@app.route('/TestPOST',methods = ['POST'])
def T_POST():
      print("Inside Get")
      user = request.form('nm')
      print("value is " + user)
      return "Test POST"
      #return render_template("Test_Post.html")
      #return redirect(url_for('success',name = user))


"""

if __name__ == '__main__':
   app.run(debug = True)'''


print(__name__)