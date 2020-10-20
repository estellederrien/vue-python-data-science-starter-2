# --------------------------------------------------------LOADING PYTHON MODULES ---------------------------------------------------
# LOADING THE FLASK LIBRARY
from flask import Flask, jsonify, request, render_template
from flask_cors import CORS

# MONGODB DRIVER
import pymongo

# PRETTY PRINT JSON
import pprint

# SYS
import sys



# --------------------------------------------------------IMAGES AND FILES UPLOADS MANAGEMENT ---------------------------------------------------
# Cloudinary settings using python code. Run before pycloudinary is used.
import cloudinary
cloudinary.config(
  cloud_name = 'xxxxxxxx',  
  api_key = '354237299578646',  
  api_secret = '3UWkrND91MW3jhmGecvp77uetvQ'  
)
import cloudinary.uploader

# Image uploads
import werkzeug
import os
import uuid
UPLOAD_FOLDER = './tmp/'
# --------------------------------------------------------END IMAGES AND FILES UPLOADS MANAGEMENT ---------------------------------------------------



# --------------------------------------------------------APP SETTING -------------------------------------------------------------------------------
app = Flask(__name__,
            static_folder="dist/static",  # place that webpack builds to
            template_folder="dist")# SERVING THE BUILT VUE.JS DIRECTORY

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# Setting upload FILES folder
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# --------------------------------------------------------MIDDLEWARE  ------------------------------------------------------------------------------

@app.before_request
def middleware():
    # CONTROLE DEMO ON OFF
        # private code
    # CONTROLE SESSIONS PRESENT OR NOT
        # private code
    # GETTING USER IP
    print(jsonify({'ip': request.remote_addr}), 200)

# -----------------------------------------------------  ROUTE SERVING THE BUILT VUE.JS DIRECTORY ---------------------------------------------------

@app.route('/')
def index():
    return render_template("index.html")

# ----------------------------------------------------- CLOUDINARY WEB SERVICE ---------------------------------------------------

@app.route('/api/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        
        # Getting the file comin from the vue.js front end - On récupère le fichier qui a été envoyé de l'applications vue.js
        file = request.files['file']
             
        # Filename renaming management - On r&écupère le nom du fichier pour s'en servir après
        originalFilename = os.path.splitext(file.filename)[0]
        extension = os.path.splitext(file.filename)[1]
        #f_name = str(uuid.uuid4()) + extension

        f_name = originalFilename + extension
        
        print("------------------------------------------------DEBUG------------------------------")
        print(originalFilename)
        print("------------------------------------------------DEBUG------------------------------")
       
        # Saving to the TMP folder - TMP is mandatory on heroku- On sauve le fichier sur le server PYTHON FLASK - Heroku n'accepte que le rep TMP
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], f_name))

        # Saving to CLOUDINARY
        cloudinary.uploader.upload(os.path.join(app.config['UPLOAD_FOLDER'], f_name), public_id = originalFilename)

        # Getting the CLOUDINARY generated url
        my_cloudinary_url = cloudinary.utils.cloudinary_url(f_name)
        
        # Sending the cloudinary generated filename to the vue.js front end, for later displaying the good image in the app
        return jsonify({'filename':my_cloudinary_url[0]})    

# ----------------------------------------------------- LINEAR SOLVER WEBS SERVICES ---------------------------------------------------


""" 
minimize_cost_1 web service
@params json object
@return json object 
"""

@app.route('/api/minimize_cost_1', methods=['POST'])
def minimize_cost_1():

    # Getting the front end DATA
    post_data = request.get_json()
    
    # Calling the solver     
    myResult = pulp_functions.pulp_minimize_cost_1(post_data)
    
    # Sending back the result to the front end
    return jsonify(myResult)

# ----------------------------------------------------- HELPER FUNCTIONS ---------------------------------------------------  

# Print is not working in nested functions, so we need this hacking code to make it working.
# La function print ne fonctionne pas dans les functions lp solver, du coup on rajoute ce hack.
def print_msg(*args, end='\n'):
    for item in args:
        sys.stdout.write(str(item)+' ')
    sys.stdout.write(end)
    sys.stdout.flush()

print = print_msg



 # ----------------------------------------------------- STARTING THE SERVER PARAMS ---------------------------------------------------  

# configuration
DEBUG = True

# instantiate the app
""" app = Flask(__name__)
app.config.from_object(__name__) """


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)

""" if __name__ == '__main__':
    app.run() """
