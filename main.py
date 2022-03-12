from flask import Flask, flash, request
from flask_restful import Api, Resource
from sqlalchemy import true
ALLOWED_EXTENSIONS = {"png","jpg","jpeg"}
app = Flask(__name__)
api = Api(app)

videos = {}

class UploadPicture(Resource):
    #check if file ends with .png or .jpg
    def checkValidFile(self, filename):
        return "." and filename.rsplit(".",1)[1].lower() in ALLOWED_EXTENSIONS

    #upon receiving post request,execute this
    def post(self,video_id):
        if "file" not in request.files:
            flash("no file found")
            return redirect(request.url)
        
        file = request.files["file"]#the key is currently "file" but it will be whatever the name of file was set in html in react. TODO: update this
        if file and checkValidFile(file.filename):
            filename = secure_filename(file.filename)
            
api.add_resource(UploadPicture, "/uploadphoto")
if __name__ == "__main__":
    app.run(debug=True)

