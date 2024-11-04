# DEPENDENCIES 
from flask import Flask, render_template, redirect, session, request
import webbrowser
# FLASK APP SET UP
app = Flask(__name__)
app.secret_key = "DSA MINI PROJECT"

# HOME ROUTE WHERE USER INPUTS WILL BE TAKEN
@app.route("/", methods=['POST', 'GET'])
def home():
    # MAP DECLARATION FOR URL INPUTS
    userurls = dict(session.items())
    
    if request.method == "POST":
        flag = request.form['flag']
        
        if flag == 'To Shorten':
            destination = request.form["inputurl"]
            shorturl = request.form["shorturl"]
            
            # VALIDATING DESTINATION WRT TO "https://"
            if "https://" not in destination:
                destination = f"https://{destination}"
            
            # CHECKING WRT TO SHORT FORM [SHORT FORM HAS TO BE UNIQUE]
            if session.get(shorturl):
                errormsg = f'{shorturl} is already used try something else'
                return render_template('error.html',errormsg=errormsg)
            else:
                session[shorturl] = destination 
            
            return redirect("/")
        elif flag == 'To Delete':
            todelete = request.form['delete_url']
            session.pop(todelete, None)
            return redirect('/')
    
    return render_template('index.html', userurls=userurls)


# ROUTE TO HANDLE SHORT URL REDIRECTION
@app.route("/<url>")
def redirectfunc(url):
    redirecturl = session.get(url)
    print(redirecturl)
    webbrowser.open(redirecturl)
    return redirect("/")


# RUN FLASK APP
if __name__ == '__main__':
    app.run(debug=True)
