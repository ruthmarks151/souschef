from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return 'works'

url_for('public_html', filename='index.html')

if __name__ == "__main__":
    app.run(host='104.236.40.40', port=80, debug=true)                                     