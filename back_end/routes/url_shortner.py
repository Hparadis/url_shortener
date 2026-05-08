from flask import Blueprint,request,jsonify,redirect
from services.logic import create_short_url

url_shortner_bp = Blueprint('url_shortner',__name__)
route_bp = Blueprint('route',__name__)

@url_shortner_bp.route('/',methods=['POST'])
def shorten_url():
     data = request.get_json()
     long_url = data.get('url')

     short_code = create_short_url(long_url)
     print("DATA RECEIVED:", data)

     return jsonify({
        "message":"URL shortened successfully!",
        "short_code":short_code
        })
@route_bp.route('/<short_code>',methods=['GET'])
def get_long_urls(short_code):
    from services.logic import get_long_url
    long_url = get_long_url(short_code)
    if long_url:
      return redirect(long_url)
    else:
        return jsonify({
            "message":"Short code not found!"
        }),404
