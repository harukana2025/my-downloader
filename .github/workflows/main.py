import yt_dlp
import os

# 【ここを好きな動画URLに書き換える！】
video_url = "https://youtube.com"

def download_video():
    print(f"ダウンロードを開始します: {video_url}")
    
    # 保存の設定（最高画質、ファイル名はタイトルにする）
    ydl_opts = {
        'format': 'best',
        'outtmpl': '%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("保存が完了しました！")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    download_video()
