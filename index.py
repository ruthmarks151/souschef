from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    content = get_file('/public_html/index.html')
    return Response(content, mimetype="text/html")
if __name__ == "__main__":
    app.run(host='104.236.40.40', port=80)                                     