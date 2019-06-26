import flask
from flask import request

from flask import json, jsonify
# from flask_restful import reqparse

app = flask.Flask(__name__)
app.config["DEBUG"] = True


# function to get the value from the json file
def getData():								
	with open('testfile.json', 'r') as j:	
		json_data = json.load(j)			
	return json_data						


# return data in carousal format.
def format_carousals(cars):								
	slides = []								
	for i in cars[:9]:							
		slides.append({						
				"title":i["car_name"],
				"subtitle":i["car_name"] + i["price"],
				"image_url":i["img"],
				})
	return jsonify({
		"entries":[
		{
		"template_type":"carousel",
		"shadow":True,
		"slides":slides	
		}
				]
	})

#create a link for video purpose and find the car in storage and return the video link to user 
#else return no video found
@app.route('/video/')
def video():
	car_data = getData()
	cars = car_data["Cardetails"]
	data = request.args.get('last_freeform_input')
	car = [c for c in cars if data.lower() in c["car_name"].lower()]
	if car:
		car = car[0]
		script = {
		"entries":[
		{
			"template_type":"video", 
			"url":car["video"],
		}
			]
		}
		return jsonify(script)
	else:
		return jsonify({
			"entries":[
				{
				"template_type":"message",
				"message": "no Videos found"
				}
			]
			})


#function for button purpose looking for car_name is storage an return image button and video button to user.
@app.route('/button/')
def button():
	car_data = getData()
	cars = car_data["Cardetails"]
	data = request.args.get('last_freeform_input')
	car = [c for c in cars if data.lower() in c["car_name"].lower()]
	if car:
		car = car[0]
		return jsonify(
		{
		"entries":[
		{
			"template_type":"message",
			"message":"click the below button to view the demo.",
			"buttons":[  
				{
				"type":"url",
				"url":car["img"],
				"webview_height":"new", 
				"title":"Preview"
				},
		{
				"type":"url",
				"url":car["video"],
				"webview_height":"full",
				"title":"Preview"
				}
			]
			}
		]

		}
		)
	else:
		return jsonify({
		"entries":[
		{
			"template_type":"message",
			"message":"No Car found",
		}
			]
		})


# it will return the car_name and the price to user in simple message.
@app.route('/sendmessage/')
def sendmessage():
	car_data = getData()
	cars = car_data["Cardetails"]
	data = request.args.get('last_freeform_input')
	car = [c for c in cars if data.lower() in c["car_name"].lower()]
	if car:
		car = car[0]
		return jsonify({
			"entries":[
			{
				"template_type":"message",
				"message":car["car_name"]+" cost " + car["price"],
			}
				]
			})
	else:
		return jsonify({
			"entries":[{
				"template_type":"message",
				"message":"Car not found",
			}]
		})


# function to set a attribute 
@app.route('/attribute/')
def attribute():
	car_data = getData()
	cars = car_data["Cardetails"]
	data = request.args.get('last_freeform_input')
	return jsonify({
		"entries":[{
		   "template_type":"set_attr",
		   "attributes":[
				{"attribute":"attr", "value": data}
			 ]
		}]
	})


#function to title, subtitle and image url to user in carousal format. 
#if user enter all it will call the all function, defined above
@app.route('/carousal/')
def carousal():
	car_data = getData()
	cars = car_data["Cardetails"]
	data = request.args.get('last_freeform_input')
	if 	(data == 'all' or data == 'All'):
			return format_carousals(cars)
	car = [c for c in cars if data.lower() in c["car_name"].lower()]
	if car:
		car = car[0]
		script = {
			"entries":[{
				"template_type":"carousel",
				"shadow":True,
				"slides":[{
					"title":car["car_name"],
					"subtitle":car["car_name"] + car["price"],
					"image_url": car["img"]
					}]
			}]
		}
		return jsonify(script)
	else:
		return jsonify({
		"entries":[{
			"template_type":"message",
			"message": "no Car found"
			  
			}]
		}) 

app.run()