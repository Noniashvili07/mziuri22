from flask import Flask,render_template,url_for,redirect,request,session
app = Flask("__name__")
app.secret_key = 'kafka'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login',methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        user = request.form['user']
        session['user'] = user
        return redirect(url_for('user'))
    else:
        if 'user' in session:
            return redirect(url_for('user'))
    return render_template('login.html')


@app.route('/user')
def user():
    if 'user' in session:
        user = session['user']
        return render_template('profile.html', username=user)
    else:
        return redirect(url_for('login'))

@app.route('/log_out')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if '__name__' == "__main__":
    app.run(debug=True)
