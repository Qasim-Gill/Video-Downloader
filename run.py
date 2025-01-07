import yt_dlp

def download_facebook_video(url):
    # it download best video but it does not care about audio
    # ydl_opts = {
    #     'outtmpl': '%(title)s.%(ext)s',  # Save the video with the title as the filename
    #     'format': 'best',  # Download the best available quality
    # }
    # it download video with best quality and best audio bcz on fb when i download video it does not download audio so now it is
    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save with title as filename
        'format': 'bestvideo+bestaudio/best',  # Download best video + audio, then merge
        'merge_output_format': 'mp4',  # Merge video and audio into an MP4 file
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

# Example usage:
video_url = "https://www.facebook.com/..."
download_facebook_video(video_url)

# 20
