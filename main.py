from flask import Flask,render_template,redirect,session,request
import webbrowser
app = Flask(__name__)
app.secret_key = "DSA MINI PROJECT"
@app.route("/",methods=["POST","GET"])
def home():
    userurls ={}
    userurls = dict(session.items())
    if request.method == "POST":
        userurls = dict(session.items())
        destination = request.form["inputurl"]
        shorturl = request.form["shorturl"]
        if not session.get(shorturl):
            if "https://www." not in destination:
                destination = "https://www." + destination
            session[shorturl] = destination
    return render_template("index.html",userurls=userurls)

@app.route("/<url>")
def redirectfunc(url):
    redirecturl = session.get(url)
    print(redirecturl)
    webbrowser.open(redirecturl)
    return redirect("/")













if __name__ == "__main__":
    app.run(debug=True)