# PatreonScraper
A Selenium setup for scraping Patreon subscriptions

## Important Information

- This program requires a valid Patreon account with active subscriptions.
- No data nor credentials will be shared or exposed while using this application. Everything 
happens locally while a Selenium client scrapes the specified artists on Patreon.

### Data Structure

The output is a JSON file that has the following structure:
```json
[
  {
    "id": "<integer>",
    "title": "<string>",
    "date": "<YYYY-MM-DD>",
    "content": "<string>",
    "images": [
      "<string>",
      ...
    ],
    "tags": [
      "<string>",
      ...
    ],
    "url": "<string>"
  }
]
```

| Field     | Type           | Description                                                                                                               |
|-----------|----------------|---------------------------------------------------------------------------------------------------------------------------|
| `id`      | `<string>`     | The Patreon id of this post. It's guaranteed unique.                                                                      |
| `title`   | `<string>`     | The title of the post.                                                                                                    |
| `date`    | `<YYYY-MM-DD>` | The publish date of the post. The format is always `YYYY-MM-DD`.                                                          |
| `content` | `<string>`     | The body text of the post. Can be empty.                                                                                  |
| `images`  | `<string>`     | The images of the post. It always uses the relative path to the parent folder of the output JSON file. Between 0 and `N`. |
| `tags`    | `<string>`     | The tags of the post. Can be used to group or search posts. Between 0 and `M`.                                            |
| `url`     | `<string>`     | The Patreon URL of the post.                                                                                              |


## Setup

### Requirements

To run this project, you need to have
- Python (tested with 3.12)
- pip

installed on your machine.

### Installation

1. Clone this repository using:
```
git clone https://github.com/zaw4rud0/PatreonScraper.git
cd PatreonScraper
```
2. Install the required dependencies using:
```
pip install -r requirements.txt
```

### Configurations

Make a copy of `.env.example` by running the following command:
```
cp .env.example .env
```
Replace the placeholder values in the `.env` file with the actual values.

### Running

1. Start the scraper:
```
python -m src.main
```
2. Run unit tests:
```
pytest
```

## Roadmap

- [x] Ability to scrape different artists in one run
- [x] Download images of scraped posts and place them in `/{OUTPUT_FOLDER}/{ARTIST}/{IMAGES}/{YEAR}/{MONTH}/`
- [ ] Ability to store scraped posts in a database out of the box
- [ ] More control over the scraping process, i.e. when the user wants to change the Patreon filters
- [ ] GUI window to show scraped posts, including their images. Use scraped tags to filter and search.
