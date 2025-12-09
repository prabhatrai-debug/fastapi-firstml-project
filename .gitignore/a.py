from flask import Flask, redirect,url_for,render_template
app=Flask(__name__)

@app.route('/success/<int:score>')
def success(score):
    return "the person has passed and marks is"+str(score)

@app.route('/home')
def hello():
    return 'Hello Prabhat'



@app.route('/')
def welcome():
    return render_template('index.html')


# @app.route('/submit',method=['POST','GET'])
# def submit():
    



if __name__=="__main__":
    app.run(debug=True)

