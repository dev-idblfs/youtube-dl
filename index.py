import youtube_dl
from flask import Flask, escape, url_for,request,json

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login', methods=['GET'])
def login():
    url = request.args.get('url').strip('"')    
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    with ydl:
        result = ydl.extract_info(
            'https://www.youtube.com/watch?v=HhXvUMf4P_U',
            download=False # We just want to extract the info
        )
        
    if 'entries' in result:
        # Can be a playlist or a list of videos
        video = result['entries'][0]
    else:
        # Just a video
        video = result
    
    list=video['formats']
    for i in range(len(list)):
        print(list[i]['format_note'],sep ='\n')
        
    return json.dumps(list)

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))