from flask import Flask, render_template

app = Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    return render_template("index.html")
    
@app.route('/about', methods=["GET"])
def about():
    return render_template("about.html")

@app.route('/blog', methods=["GET"])
def blog():
    return"<html><body><div><a href='/profile'>profile</a></div>\
        <div><a href='/'>home</a></div><div><a href='/blog'>my blog</a></div>\
            <div>xaxaxaxaxaxaxaxaxaaxjajajajajajajajajajajwkwkwkwkwkwkwkwkwkwkwk</div></body></html>"



if __name__ == '__main__':
    app.secret_key="jajajajajaja"
    app.run(debug=True)