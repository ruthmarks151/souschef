from flask import Flask, Response
app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='104.236.40.40', port=80, debug=true)                                     