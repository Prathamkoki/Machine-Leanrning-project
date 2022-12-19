from flask import Flask

app=Flask(__name__)#flask object

@app.route("/",methods=['GET','POST'])
def index():
    return "This is first ML project"

if __name__=="__main__":
    app.run(debug=True)
#module name of this app is app