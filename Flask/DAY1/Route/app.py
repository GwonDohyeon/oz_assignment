from flask import Flask,request,Response
import requests
app=Flask(__name__)

@app.route('/')
def home():
    return "hello, this is main page."

@app.route('/about')
def about():
    return "this is about page"

@app.route('/user/<username>')
def user_profile(username):
    return f'User:{username}'

@app.route('/number/<int:number>')
def number(number):
    return f'User:{number}'

@app.route('/test')
def test():
    response=requests.post(url="localhost:5000/submit",data='test data')
    return response

@app.route('/submit',methods=['GET','PUT','POST','DELETE'])
def submit():
    print(request.method)
    
    if request.method=='GET':
        print("GET method")
    
    if request.method=='POST':
        print("POST method")
    return Response("success",status=200)

if __name__=="__main__":
    app.run(debug=True)