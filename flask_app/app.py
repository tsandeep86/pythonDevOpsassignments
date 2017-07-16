from flask import Flask, request, render_template,flash,jsonify
from audioop import add

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

@app.route('/')
@app.route('/default/<var1>,<var2>', methods=['GET','POST'])
def default_name(var1,var2):
    return render_template('app_temp.html', name=var1, name2=var2)

@app.route('/default/boot')
def boot():
    return render_template('boot.html')

@app.route('/logonpage')
def logon():
    return render_template('app_login.html')

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


if __name__=='__main__':
    app.run(debug=True)   
    

