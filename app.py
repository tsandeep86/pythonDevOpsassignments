from flask import Flask, request, render_template,flash,jsonify,redirect,url_for
from audioop import add
import pymysql
import json

app = Flask(__name__)

"""
@app.route('/cupertino/<add>', methods=['GET','POST'])
def index(add):
    
    if request.method == 'POST':
        return "This is a post request: %s" %add
    else:
        return "This is a get request:%s" %add
def index():
    
    return ' This is my page'
"""
db=pymysql.Connect(host='localhost', port=3306, user='root', passwd='AnjuSandy2628', db='webapp')
cursor=db.cursor()
"""
@app.route('/')
@app.route('/default/<var1>,<var2>', methods=['GET','POST'])
def default_name(var1,var2):
    return render_template('app_temp.html', name=var1, name2=var2)
"""

"""
@app.route('/login', methods=['GET', 'POST'])
def logon_boot():
    error = None
    if request.method == 'POST':
        print request.form['password']
        print request.form['username']
        if request.form['password'] =='anju' and request.form['username'] =='tsandeep86@gmail.com':
            return boot()
        else:
            return render_template('login.html')
"""
@app.route('/boot/<name>', methods=['GET','POST'])
def boot(name):

    return render_template('boot.html',name=name)

@app.route('/logonpage')
def logon():
    return render_template('app_login.html')

@app.route('/get_data/',methods=['GET','POST'])
def get_data():
    print "one"
    print "++++++++",request.args.to_dict()
    data=request.args.to_dict()
    if(data['username']=='tsandeep86@gmail.com' and data['password']=='test'):
        result="True"
        print result
    else:
        result="False"
        print result
    print result    
    return jsonify({'result':result})

@app.route('/userinput')
def userinput():
    return render_template('userinput.html')

@app.route('/userinfo/',methods=['GET','POST'])
def user_info():
    data=request.args.to_dict()
    print data
    print data['username']
    cursor=db.cursor()
    q=("select username,address,phone_no,email from webapp.user_info where username='{0}'").format(data['username'])
    cursor.execute(q)
    userinfo=cursor.fetchone()
    name=json.dumps(userinfo)
    print name
    if(name != "null"):
        return jsonify({'result':url_for('boot',name=name),
                        'name':name})
    else:
        return name
    db.close()
    #return render_template('boot.html',json_userinfo=json_userinfo)
    #return redirect("http://127.0.0.1:5000/default/boot")


if __name__=='__main__':
    app.run(debug=True)   
    

