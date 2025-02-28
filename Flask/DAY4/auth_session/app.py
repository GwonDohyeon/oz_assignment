from flask import Flask,render_template,redirect,request,session,flash,url_for
from datetime import timedelta
app=Flask(__name__)

app.config['PERMANENT_SESSION_LIFETIME']=timedelta(minutes=5)

app.secret_key='flask-secret-key'#session함호화 키
admin_user={
    "john":'pw123',
    "leo":'pw123'
}

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login',methods=['POST'])
def login():
    username=request.form.get('username')
    password=request.form.get('password')
    """
    redirect(url_for("secret")) url_for는 route endpoint(view function)의 이름을 기반으로 url을 생성(동적 url)
    ex) url_for(blpname.function_name, param1)은 
    @blpname.route('/<int:param1>)
    def function_name(self,param1):
    로 연결
    
    redirect('/secret') 은 정적 url 사용
    ex) api endpoint가 위와같이 정의됐다면
    redirect('/blp_prefix/1)
    """
    if username in admin_user and password == admin_user[username]:
        session.get('username')==username # session["키"]=값
        session.permanent=True
        return redirect(url_for('secret')) 
    else:
        flash("Invalid username or password.")
        return redirect(url_for('index'))
    
@app.route('/secret')
def secret():
    if 'username' in session:
        return render_template('secret.html')
    else:
        return redirect(url_for('index'))
    
@app.route('/logout')
def logout():
        session.pop('username',None)
        flash("Have been logged out.")
        return redirect(url_for('index'))
    
if __name__=='__main__':
    app.run(debug=True)