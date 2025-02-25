from flask import jsonify,Flask,request
 
app=Flask(__name__)
 
 #GET
@app.route('/api/v1/feeds',methods=['GET'])
def show_all_feeds():
    data={'result':'success','data':{'feed1':'data1','feed2':'data2'}}
    return data
@app.route('/api/v1/feeds/<int:feed_id>',methods=['GET'])
def show_one_feed(feed_id):
    data={'result':'success','data':{'feed1':'data1'}}
    return data
datas=[{'result':'success','data':{'feed1':'data1'}}]

@app.get('/data')
def get_data():
    return {"datas":datas}

#POST
@app.route('/api/v1/feeds',methods=['POST'])
def create_one_feed():
    name=request.form['name']
    age=request.form['age']
    return jsonify({'result':'success'})

@app.post('/data')
def post_data():
    request_data=request.get_json()
    datas.append(request_data)
    return jsonify(datas),201

if __name__=='__main__':
    app.run(debug=True)
