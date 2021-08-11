from flask import Flask
import requests
import sys

app = Flask(__name__)

@app.route('/home')
def get():
  sys.stderr.write("\n----------calling pyserver----------\n")
  sys.stdout.flush()
  r = requests.get('http://pyserver/index')
  return r.text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', threaded = True)

