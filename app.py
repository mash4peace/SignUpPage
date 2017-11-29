from flask import Flask, render_template,request, flash, session
import model as db
app = Flask(__name__)
app.config["SECRET_KEY"] = "Here is my secret key"
@app.route("/", methods=['GET', 'POST'])
def index():
    message = None
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if db.userEixts(email)== True:
            if db.getPassword(email) == password:
                session['email'] = email
                return "Hello " + email

    return render_template('index.html', message = message)

@app.route('/registration', methods=['GET', 'POST'])
def registration():
    messages = []
    if request.method == 'POST':
        firname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        if(db.userEixts(email)) == True:
            messages.append("User with that email "+ email+" already exists")
            messages.append("Please login with your email")
            return render_template("registration.html", messages = messages)

        #print(email)
        else:
            db.insertUser(firname, lastname, email, password)
            return 'Hello '  + firname +" " + lastname + " thanks for registering with us"
    return render_template("registration.html")

if __name__ == '__main__':
    app.run(debug=True)
