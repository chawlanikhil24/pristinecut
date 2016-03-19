from flask import Flask,render_template,Response,session,request,redirect,url_for
import web,requests
from facepy import GRaphAPI
from urlparse import parse_qs

app=Flask(__name__)
app.secret_key="Naachore"

if __name__ == "__main__":
    app.run(debug=True)

fb_app_id="209704059386926"
fb_app_secret_key="93895f35938943ab0fd709530b9e3a97"
post_login_url="127.0.0.1:5000"
#Setup routing
@app.route("/",methods=['GET','POST'])
def main():
    user_data=web.input(code=None)
    if not user_data.code:
        dialog_url=("http://www.facebook.com/dialog/oauth?"+"client_id="+fb_app_id+"&redirect_uri="+post_login_url+"&scope=publish_stream")
        return redirect(dialog_url)
    else:
        graph=GraphAPI()
        
