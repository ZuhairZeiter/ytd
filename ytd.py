import os
import re
import requests
import isodate
import logging
import random
import string
from colorama import Fore, Style, init


init(autoreset=True)


logging.basicConfig(filename="log.txt", level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')


def show_ascii_art():
    print(Fore.MAGENTA + Style.BRIGHT + r"""
  __   _______ ____     _             _____     _           _      
  \ \ / /_   _|  _ \   | |__  _   _  |__  /   _| |__   __ _(_)_ __ 
   \ V /  | | | | | |  | '_ \| | | |   / / | | | '_ \ / _` | | '__|
    | |   | | | |_| |  | |_) | |_| |  / /| |_| | | | | (_| | | |   
    |_|   |_| |____(_) |_.__/ \__, | /____\__,_|_| |_|\__,_|_|_|   
                              |___/                                
    """)

def fetch_video_details(video_id, api_key):
    base_url = "https://www.googleapis.com/youtube/v3/videos"
    params = {
        "key": api_key,
        "part": "snippet,contentDetails",
        "id": video_id,
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        if "items" not in data or not data["items"]:
            print(Fore.RED + f"No data found for video ID {video_id}.")
            logging.warning(f"No data found for video ID {video_id}.")
            return None

        video = data["items"][0]
        details = {
            "title": video["snippet"]["title"],
            "description": video["snippet"]["description"],
            "thumbnail_url": video["snippet"]["thumbnails"]["high"]["url"],
            "duration": video["contentDetails"]["duration"],
        }
        return details
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error fetching details for {video_id}: {str(e)}")
        print(Fore.RED + "Network error occurred. Please check your internet connection.")
        return None
    except Exception as e:
        logging.error(f"Unexpected error fetching details for {video_id}: {str(e)}")
        print(Fore.RED + "An unexpected error occurred.")
        return None

def parse_duration(duration):
    try:
        parsed_duration = isodate.parse_duration(duration)
        total_seconds = int(parsed_duration.total_seconds())
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if hours > 0:
            return f"{hours}h {minutes}m {seconds}s"
        else:
            return f"{minutes}m {seconds}s"
    except Exception as e:
        logging.error(f"Error parsing duration: {str(e)}")
        return "Unknown duration"

def get_best_thumbnail(video_id, fallback_url):
    try:
        max_quality_url = f"https://img.youtube.com/vi/{video_id}/maxresdefault.jpg"
        response = requests.head(max_quality_url)
        if response.status_code == 200:
            return max_quality_url
        else:
            print(Fore.YELLOW + "Max resolution thumbnail not available. Using high-quality thumbnail.")
            logging.info("Max resolution thumbnail not available. Fallback used.")
            return fallback_url
    except requests.exceptions.RequestException as e:
        logging.error(f"Error checking max resolution thumbnail: {str(e)}")
        print(Fore.RED + "Network error while fetching thumbnail. Using fallback.")
        return fallback_url
    except Exception as e:
        logging.error(f"Unexpected error fetching thumbnail: {str(e)}")
        return fallback_url

def generate_random_filename(extension=".jpg"):
    try:
        random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        return random_string + extension
    except Exception as e:
        logging.error(f"Error generating random filename: {str(e)}")
        return "default_thumbnail.jpg"

def download_thumbnail(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        print(Fore.GREEN + f"Thumbnail successfully saved to {save_path}.")
        logging.info(f"Thumbnail saved to {save_path}.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Network error downloading thumbnail from {url}: {str(e)}")
        print(Fore.RED + "Network error occurred while downloading the thumbnail.")
    except Exception as e:
        logging.error(f"Unexpected error downloading thumbnail: {str(e)}")
        print(Fore.RED + "An unexpected error occurred while saving the thumbnail.")

def extract_video_id(url):
    try:
        pattern = r'(?:https?:\/\/)?(?:www\.)?youtu(?:be\.com\/(?:watch\?v=|v\/|embed\/|shorts\/)|\.be\/)([a-zA-Z0-9_-]{11})'
        match = re.search(pattern, url)
        if match:
            return match.group(1)
        else:
            print(Fore.RED + "Invalid YouTube URL format. Please enter a valid URL.")
            logging.warning(f"Invalid URL provided: {url}")
            return None
    except Exception as e:
        logging.error(f"Error extracting video ID: {str(e)}")
        print(Fore.RED + "An unexpected error occurred while processing the URL.")
        return None

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    api_key = "AIzaSyD7Mfa2ObOgl7dgov2456toRbydu1wD_Yg"

    while True:
        clear_terminal()
        show_ascii_art()
        print(Fore.CYAN + Style.BRIGHT + "===== YouTube Thumbnail Downloader =====")
        urls = input(Fore.CYAN + "Enter YouTube video URLs (comma-separated): ").split(",")

        save_dir = "thumbnails"
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
            print(Fore.CYAN + f"Created directory: {save_dir}")
            logging.info(f"Created directory: {save_dir}")
        else:
            print(Fore.CYAN + f"Directory '{save_dir}' already exists.")

        for url in urls:
            url = url.strip()
            video_id = extract_video_id(url)
            if not video_id:
                continue

            print(Fore.CYAN + f"\nFetching details for video URL: {url}")
            video_details = fetch_video_details(video_id, api_key)
            if video_details is None:
                continue

            print(Fore.YELLOW + "\nVideo Details:")
            print(Fore.YELLOW + f"Title: {Fore.WHITE + video_details['title']}")
            print(Fore.YELLOW + f"Description: {Fore.WHITE + video_details['description']}")
            print(Fore.YELLOW + f"Duration: {Fore.WHITE + parse_duration(video_details['duration'])}")

            best_thumbnail = get_best_thumbnail(video_id, video_details["thumbnail_url"])
            print(Fore.YELLOW + f"Thumbnail URL: {Fore.WHITE + best_thumbnail}")

            random_filename = generate_random_filename()
            save_path = os.path.join(save_dir, random_filename)

            download_thumbnail(best_thumbnail, save_path)

        more_downloads = input(Fore.CYAN + "\nDo you want to download more thumbnails? (yes/no): ").strip().lower()
        if more_downloads != "yes":
            print(Fore.GREEN + "Exiting. Thank you for using the YouTube Thumbnail Downloader!")
            logging.info("User exited the application.")
            break

if __name__ == "__main__":
    main()
