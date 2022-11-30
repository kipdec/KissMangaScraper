# KissMangaScraper

## What is it?

This is a cli script that pulls down images from Kiss manga created to quickly demonstrate webscraping.

## How do I use it?

```
usage: python3 scraper.py [-h] [-n NAME] [-o OUTPUT_DIR] url

positional arguments:
  url                   The KissManga url you want to pull the images from.
                        Required.

options:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  The name you want the output files to be. E.g. for
                        bleach_1.jpg, you would supply `--name=bleach`.
                        Defaults to `page`
  -o OUTPUT_DIR, --output_dir OUTPUT_DIR
                        The directory you want the files to be created in. If
                        the directory does not exist, it will create it.
                        Defaults to current directory
```

## How could it be better?

Some ideas:

- [ ] Asynchronous calls to download the images
- [ ] Scrape the Manga name and chapter number from the html

## Contributing

If you'd like to contribute, feel free to open a PR.