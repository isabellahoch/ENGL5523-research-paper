# ENGL 55.23/FILM 48.07 Research Paper - Winter 2023

## Description
This repository contains Python scripts for scraping, parsing, and analyzing textual data from both Twitter and Fizz posts discussing Dartmouth. The scripts utilize the `gensim` and `nltk` packages for text analysis and also utilize MALLET's Java-based comprehensive text analysis capabilities.

The repository is organized into the following directories:

- `scripts/`: Contains all the python scripts used for data scraping, parsing, and analysis.
- `data/`: Contains all the data files, subdivided into separate folders containing Fizz and Twitter results, respectively.
- `MALLET/`: Contains the output of the topic modeling done with the MALLET tool.
- `TOPICS/`: Contains the output of the topic modeling done with the TOPICS tool.

## Requirements

The following packages are required to run the scripts:

- gensim
- nltk
- dotenv
- pandas

Additionally, [MALLET's Java-based comprehensive text analysis tool](https://mallet.cs.umass.edu/download.php) is required to run the topic modeling scripts.


## Usage
To use the scripts, follow these steps:

- Clone the repository to your local machine.
- Create a Twitter Developer Account to gain access to their API through a Bearer Token and create a `.env` file to securely save said Bearer Token in the format `BEARER_TOKEN=xxxxxx`
- Install the required packages.
- Run the scripts in the `scripts/` directory to scrape, parse, and analyze the data.
- The output of the analysis will be stored in the `MALLET/` and `TOPICS/` directories.

## License
This project is licensed under the MIT License, 2023.