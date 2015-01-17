from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')

<<<<<<< HEAD
if __name__ == "__main__":
    app.run(host='104.236.40.40', port=80, debug=true)                                    
=======
import os
@app.route('/static/<path:path>')
def static_proxy(path):
    # send_static_file will guess the correct MIME type
    return app.send_static_file(os.path.join('static', path))

if __name__ == '__main__':  # pragma: no cover
    app.run(host='0.0.0.0', port=5000)
>>>>>>> 404a5832de766d8c9ff4a72d9f6adbf7a2a2f3d3
