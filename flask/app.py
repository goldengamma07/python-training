from flask import Flask

app = Flask(__name__)
@app.route('/', methods=["GET"])
def home():
    return"<html><body><div><a href='/profile'>profile</a></div>\
        <div><a href='/'>home</a></div><div><a href='/blog'>my blog</a></div></body></html>"

@app.route('/profile', methods=["GET"])
def profile():
    return"<html><body><div><a href='/profile'>profile</a></div>\
        <div><a href='/'>home</a></div><div><a href='/blog'>my blog</a></div>\
            <div>Name: Ganesh shyam M</div><div>DOB: 11.05.1996</div>\
                <div>mail:<a href='https://mail.google.com/mail/u/2/#inbox?compose=CllgCJZZxwkTBQQtHvJhqqkZBplbVHrpLWsSKjrnDkXKHvfKXTmMvCkFWSKwPLNShTdWXdrlGRg'>ganeshshyamm@gmail.com</a></div>\
                    <div>facebook profile:<a href='https://www.facebook.com/ganesh.shyam/'>Ganesh Shyam</a></div></body></html>"


@app.route('/blog', methods=["GET"])
def blog():
    return"<html><body><div><a href='/profile'>profile</a></div>\
        <div><a href='/'>home</a></div><div><a href='/blog'>my blog</a></div>\
            <div>xaxaxaxaxaxaxaxaxaaxjajajajajajajajajajajwkwkwkwkwkwkwkwkwkwkwk</div></body></html>"

if __name__ == '__main__':
    app.secret_key="jajajajajaja"
    app.run(debug=True)