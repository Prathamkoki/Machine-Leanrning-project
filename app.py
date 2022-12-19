from flask import Flask
from housing.logging import logging

app=Flask(__name__)#flask object

@app.route("/",methods=['GET','POST'])
def index():
    logging.info("we are testing logging module")
    return "This is first ML project"

if __name__=="__main__":
    app.run(debug=True)
#module name of this app is app