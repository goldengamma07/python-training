from flask import Flask, render_template, request

app = Flask(__name__)

sam = "<html><body><div><a href='/profile'>profile</a></div>\
        <div><a href='/'>home</a></div><div><a href='/blog'>my blog</a></div><div>"
sam_end = "</div></body></html>"
@app.route('/', methods=["GET"])
def home():
  
    return render_template("index.html")
    
@app.route('/login', methods=["GET", "POST"])
def profile():
    if request.form['email'] == 'ganisdon@gmail.com':
        if request.form['pass'] == '1212':            
            return render_template("login.html", u_name=request.form["Username"])
        return "User password is incorrect.. please enter correct password"
    return "User email is incorrect.. please enter correct email"

@app.route('/blog', methods=["GET"])
def blog():
    return sam+" xaxaxaxaxaxaxaxaxaaxjajajajajajajajajajajwkwkwkwkwkwkwkwkwkwkwk"+sam_end



if __name__ == '__main__':
    app.secret_key="jajajajajaja"
    app.run(debug=True)