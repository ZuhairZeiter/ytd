---

# YouTube Thumbnail Downloader  

![Tool Banner](https://i.ibb.co/G7ynVtJ/YTD-Logo-White-with-Black-Background-5000x5000.png)  

A professional, reliable, and easy-to-use tool for downloading high-quality YouTube thumbnails. With an intuitive CLI interface, error handling, and logging, this tool is perfect for developers and content creators alike.

---

## ✨ Features  
- Fetches video details (title, description, duration) directly from the YouTube Data API.  
- Downloads the highest available resolution of thumbnails.  
- Automatically saves thumbnails with unique filenames in a dedicated folder.  
- Comprehensive logging for errors and successful operations.  
- Fully supports multiple URLs in one go.  
- User-friendly interface with clear prompts and ASCII art branding.  
- Option to download more thumbnails or exit after each session.  
- Cross-platform terminal support (Windows, macOS, Linux).  

---

## 🛠️ Prerequisites  
Ensure you have the following installed on your system:  
- Python 3.8+  
- Pip (Python Package Installer)  
- A valid YouTube Data API Key ([Get yours here](https://console.cloud.google.com/))  

---

## 📦 Installation  

1. Clone this repository:  
   ```bash
   git clone https://github.com/zuhairzeiter/ytd.git
   cd youtube-thumbnail-downloader
   ```  

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

3. Replace the placeholder API key in `main()` with your YouTube Data API key:  
   ```python
   api_key = "YOUR_API_KEY_HERE"
   ```  

---

## 🚀 Usage  

Run the script:  
```bash
python ytd.py
```  

Follow the on-screen prompts to:  
1. Enter one or more YouTube video URLs (comma-separated).  
2. View video details, including title, description, and duration.  
3. Download the highest quality thumbnail available.  
4. Choose to download more thumbnails or exit.  

### Example Session  
```plaintext
===== YouTube Thumbnail Downloader =====
Enter YouTube video URLs (comma-separated): https://youtu.be/dQw4w9WgXcQ

Fetching details for video URL: https://youtu.be/dQw4w9WgXcQ

Video Details:
Title: Never Gonna Give You Up
Description: Official Rick Astley video!
Duration: 3m 33s

Thumbnail URL: https://img.youtube.com/vi/dQw4w9WgXcQ/maxresdefault.jpg

Thumbnail successfully saved to thumbnails/abc123xyz.jpg.

Do you want to download more thumbnails? (yes/no): no
Exiting. Thank you for using the YouTube Thumbnail Downloader!
```  

---

## 🧩 Directory Structure  
```plaintext
youtube-thumbnail-downloader/
├── thumbnails/          # Saved thumbnails
├── requirements.txt     # Python dependencies
├── ytd.py              # Main script
├── README.md            # Documentation
├── log.txt              # Logs for errors and events
```

---

## 🛡️ Error Handling  
- **Invalid YouTube URL**: Detects invalid or unsupported formats and prompts the user to try again.  
- **Network Issues**: Handles network-related errors gracefully with informative messages.  
- **Fallback Mechanisms**: Uses a fallback thumbnail URL if the highest resolution is unavailable.  
- **Logging**: All events, errors, and warnings are logged to `log.txt` for easy debugging.  

---

## 🌟 Contribution  

We welcome contributions! If you have ideas for improvements, feel free to:  
1. Fork this repository.  
2. Make your changes in a new branch.  
3. Submit a pull request with a clear explanation of your enhancements.  

---

## 📝 License  

This project is licensed under the [MIT License](LICENSE).  

---

## 📫 Contact  

Feel free to reach out for feedback or support:  
- **GitHub Issues**: [Open an issue](https://github.com/zuhairzeiter/ytd/issues)  
- **Email**: zuhairzeiter@outlook.com  

---

### 🚧 TODO  
- Add multi-threaded downloads for faster processing.  
- Implement a GUI for a more user-friendly experience.  
- Add support for playlists.  

---

> **Disclaimer**: This tool uses the YouTube Data API and respects their terms of service. Ensure you follow all guidelines when using the API key.  

---  
