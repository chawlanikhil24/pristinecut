from flask import Flask,render_template,Response,session,request,redirect,url_for
import web,requests
from facepy import GraphAPI
from urlparse import parse_qs


app = Flask(__name__)
app.secret_key = 'Fuckedupworld'

fb_app_id="209704059386926"
fb_app_secret_key="93895f35938943ab0fd709530b9e3a97"
post_login_url="http://localhost:5000/"
#Just Some Ping Tests
@app.route('/ping')
def ping():

	return "Hello World"

#-----------------------------Here Goes All The Routing API's--------------------------------------------------#
@app.route('/',methods=['GET','POST'])
def main():
    if "code" not in request.values.keys():
        dialog_url=("http://www.facebook.com/dialog/oauth?"+"client_id="+fb_app_id+"&redirect_uri="+post_login_url+"&scope=publish_actions")
        return redirect(dialog_url)
    else:
        code=request.values.get("code")
        graph=GraphAPI()
        response=graph.get(
            path='oauth/access_token',
            client_id=fb_app_id,
            client_secret=fb_app_secret_key,
            redirect_uri=post_login_url,
            code=code
        )
        data=parse_qs(response)
        graph=GraphAPI(data['access_token'][0])
        graph.post(path='me/feed',message='test post')
        return data['access_token'][0]



if __name__ == "__main__":
	app.run(debug=True)
