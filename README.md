[<img alt="Youtube example" src="https://img.shields.io/badge/YouTube-FF0000?style=for-the-badge&logo=youtube&logoColor=white" />](https://www.youtube.com/watch?v=_crYfS5v4ag)

# Exif-Scraping-Tool
EST is a CLI based script that allows you to retrieve and store exif data from an image.

## How does it work?

- Exif Scraping Tool uses Piexif and PIL to retrieve device and geolocation information from image files.

1. Clone the repository. 
```
$ git clone https://github.com/Freeloot/Exif-Scraping-Tool
$ cd Exif-Scraping-Tool-main/
```

2. Install (windows).

```
$ cd /setup/
$ install.bat
$ cd ..
$ cd src
```

2. Install (Linux).

```
$ cd /setup/
$ pip3 install -r requirements.txt
$ cd ..
$ cd src
```

3. Run the script.

- Scrape a file within the current directory 
```
$ python3 est.py image.jpg
```

- Scrape a file within a seperate folder 
```
$ python3 est.py images_folder/image.jpg
```
