from flask import Flask, jsonify,make_response,abort,request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

database = ["12345", "343dffeer33", "4rr5435v34c44", "MP1YWTLM","P1YWTLM"]

#swagger config
SWAGGER_URL='/swagger'
API_URL='/static/swagger.json'
SWAGGER_BLUEPRINT=get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name' : 'Validate Serial Number'
    }
)

app.register_blueprint(SWAGGER_BLUEPRINT,url_prefix=SWAGGER_URL)

@app.route('/', methods=['GET'])
def Validate_Serial_number():
    val = request.args.get('SN')
    val = val
    
    if val in database:
        result = {
            "Serial_number": val,
            "Serial_number present in Database? ": "YES",
            "Load the role ? ": "YES, Load the role."
        }
        return jsonify(result)
    else:
        result = {
            "Serial_number": val,
            "Serial_number present in Database? ": "NO",
            "Load the role ? ": "No, terminate the process!!"
        }
        return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)