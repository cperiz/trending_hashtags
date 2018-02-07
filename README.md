# Trending Hashtags

This is a simple code to scrape real time public domain tweets, and maintain a cumulative histogram of the unique hashtags. Tweepy is used to scrape the tweets and feed the separated hashtags into a counter. An asynchronous messaging (via RabbitMQ) has been utilized to message the hashtags with a highest counts to a download script every X seconds, which in turn google searches and downloads urls for these hashtags. Another instance of use for asynchronous messaging is to maintain a plot of the top trending hashtags for easy viewing.

## Getting Started


### Prerequisites

You need to have python 2.7 or have an anaconda virtual environment with python 2.7 in order to run.

### Installing

The following outlines the instructions for setting up this code using an anaconda virtual environment.

Install RabbitMQ. The easiest way to install rabbitmq is possibly with homebrew

```
brew install rabbitmq
```

For more information on RabbitMQ installation see brew install https://www.rabbitmq.com/install-standalone-mac.html.

Create virtual environment using anaconda. Activate anaconda environment.

```
conda update conda
conda create -n yourenvname python=2.7 anaconda
source activate yourenvname
```

The python twitter API tweepy is used to scrape twitter. pika is required for asynchronous messaging from python. google-search (https://pypi.python.org/pypi/google-search/1.0.2) is used to download urls for top ranking hashtags. Install these on the anaconda environment:

```
pip install tweepy
pip install pika
pip install google-search
```

Deactivate anaconda environment after use.

```
source deactivate
```

Once you clone the repository open two terminals. Run the plotter (or url downloader) first. This will wait for asynchronous messages from the scraper and plot a histogram of the hashtag counts.

```
python receiver_plotter.py
```
or
```
python receiver_plotter.py
```

In the second terminal, run the scraper.

```
python tweepy_plotter.py
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
