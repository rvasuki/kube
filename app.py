# flask_web/app.py

from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/hit_backend', methods=['POST'])
def hit_backend():
    content = request.get_json()
    if (content["target"] == "backend-1" and content["username"] == "user one"):
    	return jsonify(
        	service_name="backend-1",
		    username="user one")
    else if (content["target"] == "backend-2" and content["username"] == "user one"):
        return jsonify(
            service_name="backend-2",
            username="user one")
    else if (content["target"] == "backend-3" and content["username"] == "user one"):
        return jsonify(
            service_name="backend-3",
            username="user one")
    else
	return jsonify(
		service_name="Sorry Mate!",
		username="Anonymous")


if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0',port=8080)

