import yt_dlp

save_path = input("Where to save? (e.g. C:/Music): ").strip()
video_url = input("Enter YouTube URL: ").strip()

def show_progress(d):
    if d['status'] == 'downloading':
        print(f"\rDownloading: {d['_percent_str']} at {d['_speed_str']}", end='')
    elif d['status'] == 'finished':
        print("\nDownload complete!")

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    'progress_hooks': [show_progress],
    'noplaylist': False,
}

try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print(f"✅ Saved to: {save_path}")
except Exception as e:
    print(f"\n❌ Error: {e}")