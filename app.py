import os
import shutil
from flask import Flask, request, send_file, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/download', methods=['POST'])
def download():
    url = request.json.get('url')
    format_choice = request.json.get('format', 'mp3')
    
    if format_choice not in ['mp3', 'wav']:
        return jsonify({'error': 'Invalid format. Choose mp3 or wav.'}), 400
    
    if not url:
        return jsonify({'error': 'No URL provided.'}), 400
    
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': '%(title)s.%(ext)s',
            'postprocessors': [
                {
                    'key': 'FFmpegExtractAudio',
                    'preferredformat': format_choice,
                },
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
        
        return send_file(filename, as_attachment=True)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
