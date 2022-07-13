from flask import Flask

app = Flask(__name__)

@app.route('/hello/FUCK')
def hello():
    return 'Hello World'



print("poop!")
print("poop but again!")



if __name__ == '__main__':
   app.run()