### app setup ###
# pip install flask
# then, run app using 'python flask_app_carousel.py'
# open your browser with url http://localhost:5000/


import flask
from flask import request

from flask import jsonify
app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/',methods=['GET','POST'])
def showCarousal():
    mobile = request.form.get('mobile_number')
    return jsonify(getCarouselRes())



def getCarouselRes():
    return {
    "entries": [
        {
            "template_type": "carousel",
            "shadow": True,
            "slides": [
                {
                    "title": "Royal Sundaram General Insurance",
                    "subtitle": "24369",
                    "image_url": "http://steffen-s.com/wp-content/uploads/2016/04/NZ-Landscape-3-600x400.jpg",
                    "buttons": [
                        {
                            "type": "url",
                            "url": "https://b2capistaging.insurancedekho.com/car-insurance/quotes?request=5d35e1c125b99f3f296ff5c2&quoteReferenceNumber=BA503146VPC0051297",
                            "webview_height": "new",
                            "title": "Buy Now"
                        }
                    ]
                },
                {
                    "title": "DHFL General Insurance",
                    "subtitle": "54965",
                    "image_url": "http://steffen-s.com/wp-content/uploads/2016/04/NZ-Landscape-3-600x400.jpg",
                    "buttons": [
                        {
                            "type": "url",
                            "url": "https://b2capistaging.insurancedekho.com/car-insurance/quotes?request=5d35e1c125b99f3f296ff5c2&quoteReferenceNumber=EEuo2QTBe",
                            "webview_height": "new",
                            "title": "Buy Now"
                        }
                    ]
                }
            ]
        }
    ]
}


if __name__ == "__main__":
	app.run()
