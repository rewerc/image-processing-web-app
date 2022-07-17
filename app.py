from flask import Flask, render_template, send_file, request
from io import BytesIO
import cv2 as cv
import numpy as np
import json
from dip import *

def allowed(string):
    return "." in string and string.rsplit(".", 1)[1].lower() in ["jpg", "png"]

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/image", methods=["POST"])
def image():
    if "image" not in request.files:
        return "0"
    file = request.files["image"]
    if file.filename == "":
        return "0"
    if file and allowed(file.filename):
        file = file.read()
        img = cv.imdecode( np.frombuffer(file, np.uint8), cv.IMREAD_GRAYSCALE )

        # process here
        if "settings" in request.form:
            settings = json.loads( request.form["settings"] )
            if "negative" in settings and settings["negative"]:
                img = Negative(img)
            if "contrastSets" in settings and settings["contrastSets"]["scale"] != 0:
                img = CS(img, settings["contrastSets"]["scale"])
            if "brightSets" in settings and settings["brightSets"]["const"] != 0:
                img = IB(img, settings["brightSets"]["const"])
            if "scaleSets" in settings and (settings["scaleSets"]["xscale"] != 0 or settings["scaleSets"]["yscale"] != 0):
                img = Scaling(img, settings["scaleSets"]["xscale"], settings["scaleSets"]["yscale"])
            if "rotateSets" in settings and settings["rotateSets"]["angle"] != 0:
                img = Rotate(img, settings["rotateSets"]["angle"])
            if "transSets" in settings and (settings["transSets"]["xtrans"] != 0 or settings["transSets"]["ytrans"] != 0):
                img = Trans(img, settings["transSets"]["xtrans"], settings["transSets"]["ytrans"])
            if "smoshaSets" in settings and settings["smoshaSets"]["level"] != 0:
                img = SS(img, settings["smoshaSets"]["level"])
            if "pp1Sets" in settings and settings["pp1Sets"]["angle"] != 0:
                img = PP(img, settings["pp1Sets"]["angle"])
            if "pp2Sets" in settings and (settings["pp2Sets"]["top"] != 0 or settings["pp2Sets"]["left"] != 0):
                img = PP2(img, settings["pp2Sets"]["top"], settings["pp2Sets"]["left"])

        img = BytesIO( cv.imencode(".png", img)[1].tobytes() )
        return send_file(
            img,
            as_attachment=True,
            download_name="editted.png",
            mimetype="image/png"
        )

if __name__ == '__main__':
   app.run(debug=True)