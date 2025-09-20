import requests
import os
from urllib.parse import urlparse
import uuid

def main():
    print("Welcome to the Ubuntu Image Fetcher")
    print("A tool for mindfully collecting images from the web\n")

    # Prompting user for image URL
    url = input("Please enter the image URL: ").strip()

    # directory for fetched images
    folder_name = "Fetched_Images"
    os.makedirs(folder_name, exist_ok=True)

    try:
        # Fetch the image
        response = requests.get(url, timeout=10)
        response.raise_for_status() 
        # Raise HTTPError for bad responses

        # Extracting filename from URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If no valid filename, generate one
        if not filename or "." not in filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Save image in binary mode
        file_path = os.path.join(folder_name, filename)
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"Successfully fetched: {filename}")
        print(f"Image saved to {file_path}\n")
        print("Connection strengthened. Community enriched.")

    except requests.exceptions.MissingSchema:
        print("Invalid URL. Please include http:// or https://")
    except requests.exceptions.ConnectionError:
        print("Failed to connect. Please check your internet connection.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
    
