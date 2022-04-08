# Exif-Scraping-Tool
EST is a tool that allows you to retrieve and store exif data from an image.

## How does it work?

- Exif Scraping Tool uses Piexif and PIL to retrieve device and geolocation information from image files.

1. Clone the repository using `git clone https://github.com/Freeloot/Exif-Scraping-Tool/`
2. Locate and run the /setup/install.bat file (windows only), on linux install packages manually.
3. Locate and run the /src/est.py using the following syntax

### Windows
Scrape a file within the current directory `python est.py image.jpg`

Scrape a file within a seperate folder `python est.py imagesFolder/image.jpg`
<br>
### Linux
Scrape a file within the current directory `python3 est.py image.jpg`

Scrape a file within a seperate folder `python3 est.py imagesFolder/image.jpg`
