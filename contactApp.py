#!/usr/bin/env python3
# contactApp.py - Program to manage contacts
# James Skon, 2022
import json

from contactDB import contactDB
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross domain requests

ctdb = contactDB()


def toJSON(data):
    results = "{\"results\":["
    for e in data:
        results += '{"first":"'+e[0]+'",'
        results += '"last":"'+e[1]+'",'
        results += '"phone":"'+e[2]+'",'
        results += '"type":"'+e[3]+'",'
        results += '"ID":"'+str(e[4])+'"},'
    if results[-1] == ',':
        results = results[:-1]
    results += ']}'
    return results


@app.route("/")
def about():
    return render_template("contactApp.html")


@app.route("/contact/find/<search>")
def find(search):
    results = ctdb.find(search)
    return toJSON(results)


@app.route("/contact/find")
def findall():
    results = ctdb.find("")
    return toJSON(results)


@app.route("/contact/last/<search>")
def findlast(search):
    results = ctdb.findByLast(search)
    return toJSON(results)


@app.route("/contact/first/<search>")
def findfirst(search):
    results = ctdb.findByFirst(search)
    return toJSON(results)


@app.route("/contact/type/<search>")
def findtype(search):
    results = ctdb.findByType(search)
    return toJSON(results)


@app.route("/contact/add/<first>/<last>/<phone>/<ctype>")
def add(first, last, phone, ctype):
    results = ctdb.add(first, last, phone, ctype)
    return results


@app.route("/contact/update/<idnum>/<first>/<last>/<phone>/<ctype>")
def update(idnum, first, last, phone, ctype):
    results = ctdb.update(idnum, first, last, phone, ctype)
    return results


@app.route("/contact/delete/<idnum>")
def delete(idnum):
    results = ctdb.delete(idnum)
    return results
