<h1>YouTube Downloader #P005</h1>

<h2>Description</h2>
Downloads YouTube videos or playlists and saves to any path directory given by the user.
<br />


<h2>Languages and Utilities Used</h2>

- <b>Python</b> 
- <b>yt-dlp library</b>

<h2>Environments Used </h2>

- <b>Windows 11 Pro</b> (24H2)
- <b>Visual Studio Code</b>

## How to Run

Follow these steps to set up and run the YouTube downloader:

• **Install Python**: Make sure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://python.org).

• **Clone the repository**: Download this project to your local machine by running `git clone https://github.com/AyaanJK/youtube-downloader.git` in your terminal or command prompt.

• **Navigate to the project directory**: Change into the downloaded folder using `cd youtube-downloader`.

• **Install required dependencies**: Install the necessary Python package by running `pip install yt-dlp` in your terminal or command prompt.

• **Run the script**: Execute the program by typing `python youtube-downloader.py` (or whatever you've named your Python file) in your terminal.

• **Enter the save location**: When prompted, type the full path where you want to save your downloaded files (e.g., `C:/Music` on Windows or `/Users/yourusername/Music` on macOS/Linux).

• **Enter the YouTube URL**: Paste the URL of the YouTube video or playlist you want to download when prompted.

• **Wait for download**: The script will show download progress and automatically save the audio file to your specified location.

• **Find your downloaded file**: Once complete, check the save location you specified to find your downloaded audio file.

### Requirements
- Python 3.8 or later
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) installed

### Quick Start
-  Install the required package:
-  pip install yt-dlp
-  Type 'python yt_downloader.py' into terminal to run
-  For Windows, simply double-click the .bat file

<h2>Program walk-through:</h2>

<p align="center">
Importing yt-dlp library to handle YouTube downloads: <br/>
<img src="https://i.imgur.com/jcVFSxv.png" height="80%" width="80%" alt="Bulk File Renamer Steps"/>
<br />
<br />
Asks where to save files and for the YouTube link:  <br/>
<img src="https://i.imgur.com/4x3CWuO.png" height="80%" width="80%" alt="Bulk File Renamer Steps"/>
<br />
<br />
Shows real-time download progress and speed: <br/>
<img src="https://i.imgur.com/Fpl0WOV.png" height="80%" width="80%" alt="Bulk File Renamer Steps"/>
<br />
<br />
Configures audio quality, output path, and enables playlist downloads: <br/>
<img src="https://i.imgur.com/X1e1Nyf.png" height="80%" width="80%" alt="Bulk File Renamer Steps"/>
<br />
<br />
Downloads the video/playlist and handles errors gracefully: <br/>
<img src="https://i.imgur.com/KGRMDtO.png" height="80%" width="80%" alt="Bulk File Renamer Steps"/>
<br />
</p>
