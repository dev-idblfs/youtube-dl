import youtube_dl
from flask import Flask, escape, url_for,request,json,jsonify

app = Flask(__name__)
app.config['PYTHONATH']='bypass_app'

@app.route('/')
def index():
    return 'index'


@app.route('/youtube')
def youtube():
    if request.args:
        url = request.args.get('url')
        ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
        result = ydl.extract_info(
            url,
            download=False # We just want to extract the info
        )
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result
        
        list=video['formats']
        return jsonify(list)
    else:
        return "login"