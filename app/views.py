from app import app
from flask import Flask, flash, request, redirect, url_for, session, jsonify, render_template, make_response
import requests
import jwt
from os import environ 

SECRET = environ.get('SECRET')

def index(): 
    # if request.method == "POST":
    #     req = request.get_json(force=True)
    #     if req['type'] == "parse_data_yandex":
    #         res = parse_data_yandex(req)
    #         return make_response(res)
        
    #     elif req['type'] == "get_image_list":
    #         print('req = ', req)
    #         res = jsonify({ "status": 200, "image_ids": arr })
    #         return make_response()

    return ''

####
@app.route('/auth/login', methods=["POST", "GET", "OPTIONS"])
def login():
    #req = request.get_json(force=True)
    #login = req['login']
    #passw = req['password']
    status = ""
    res = {"status": status}
    if status == "error":
        error = ""
        res["error"] = error
    
    else:
        access_token = ""
        refresh_token = ""
        res["access_token"] = access_token
        res["refresh_token"] = refresh_token
    response = jsonify(res)
    return make_response(response)

####
@app.route('/auth/refresh_token', methods=["POST", "GET", "OPTIONS"])
def refresh_token():
    #req = request.get_json(force=True)
    #refresh_token = req['refresh_token']
    status = ""
    res = {"status": status}
    if status == "error":
        error = ""
        res["error"] = error
    
    else:
        access_token = ""
        refresh_token = ""
        res["access_token"] = access_token
        res["refresh_token"] = refresh_token
    response = jsonify(res)
    return make_response(response)


###
@app.route('/auth/logout', methods=["POST", "GET", "OPTIONS"])
def logout():
    #req = request.get_json(force=True)
    #access_token = req['access_token']
    status = ""
    res = {"status": status}
    if status == "error":
        error = ""
        res["error"] = error


@app.route('/')
def mew():
    return 'Mew'
