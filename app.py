from flask import Flask, request, send_file
import yt_dlp
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <title>TikTok Downloader PRO</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', sans-serif;
                background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }

            .container {
                background: rgba(255, 255, 255, 0.05);
                backdrop-filter: blur(15px);
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                width: 400px;
                box-shadow: 0 0 30px rgba(0,0,0,0.5);
            }

            h1 {
                margin-bottom: 20px;
                font-size: 28px;
            }

            input {
                width: 90%;
                padding: 12px;
                border-radius: 10px;
                border: none;
                margin-bottom: 20px;
                outline: none;
                font-size: 14px;
            }

            button {
                background: linear-gradient(45deg, #00c6ff, #0072ff);
                border: none;
                padding: 12px 20px;
                color: white;
                font-size: 16px;
                border-radius: 10px;
                cursor: pointer;
                transition: 0.3s;
            }

            button:hover {
                transform: scale(1.05);
                box-shadow: 0 0 15px #00c6ff;
            }

            .footer {
                margin-top: 20px;
                font-size: 12px;
                opacity: 0.6;
            }

            .loader {
                display: none;
                margin-top: 15px;
            }
        </style>

        <script>
            function showLoader() {
                document.getElementById("loader").style.display = "block";
            }
        </script>
    </head>
    <body>

    <div class="container">
        <h1>🎵 TikTok Downloader</h1>

        <form action="/download" method="post" onsubmit="showLoader()">
            <input type="text" name="url" placeholder="Pega aquí el link de TikTok..." required>
            <br>
            <button type="submit">⬇ Descargar Video</button>
        </form>

        <div id="loader" class="loader">
            ⏳ Descargando video...
        </div>


    </div>

    </body>
    </html>
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
