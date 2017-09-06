# -*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect, flash, url_for, session
# from flaskext.mysql import MySQL
import csv, math, io, pandas

import json
#from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'secret'


@app.route("/")
def showMainPage():
	return render_template("main.html")


# 메인 화면
#@app.route("/main")


if __name__=="__main__":
	app.run(debug=True, host = '127.0.0.1', port= 5000)
	#app.run(host='163.152.184.176', port= 5000, debug=True)

