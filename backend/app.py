from flask import Flask,render_template,Response,session,request,redirect,url_for,g
import web,requests
from facepy import GRaphAPI
from urlparse import parse_qs

app=Flask(__name__)
app.secret_key="Naachore"

if __name__ == "__main__":
    app.run(debug=True)
    
#code for photo upload

photos = UploadSet('photos',IMAGES)

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        rec = Photo(filename=filename. user=g.user.id)
        rec.store()
        flash("Photo Saved")
        return redirect(url_for('show', id=rec.id))
    return render_template('upload.html')
    
@app.route('/photo/<id>')
def show(id):
    photo = Photo.load(id)
    if photo is None:
        abort(404)
    url = photos.url(photo.filename)
    return render_template('show.html', url=url, photo=photo)
        
