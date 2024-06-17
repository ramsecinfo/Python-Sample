from flask import *
 
app = Flask(__name__)
 
@app.route('/')
def home():
    return ("<body style='background-color: #9dffff; height=100%; display:flex;'>"
            "<div style='font-family: Poppins; display:flex; flex-direction: column; align-self: center; width: 100%'>"
            "<h1 style='text-align:center'>Welcome to Jenkins CI/CD Pipeline for Python Application</h1>"
            "<h2 style='text-align:center'>Also with SAST Security Scan</h2>"
            "</div>"
            "</body>")
 
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
