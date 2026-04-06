from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Descargador de TikTok 🎵</h1>
    <form action="/download" method="post">
        <input type="text" name="url" placeholder="Pega URL de TikTok" required>
        <button type="submit">Descargar</button>
    </form>
    '''

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    
    ydl_opts = {
        'outtmpl': 'video.%(ext)s',
        'format': 'mp4'
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return send_file("video.mp4", as_attachment=True)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
