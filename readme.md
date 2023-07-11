# Web Scraping with Python and Beautiful Soup

This Python script uses the Beautiful Soup library to scrape data from the Beautylish website and store it in a SQLite database. The script also saves the HTML of the scraped page to a file.

We will scrape the new arrivals on beautylish.com.

## Installation

This script requires Python 3 and the following libraries:

- BeautifulSoup4
- undetected-chromedriver
- sqlite3

It is recommended that you use a virtual environment to install these libraries. To create a virtual environment:

```
python3 -m venv myenv
source myenv/bin/activate
```

To install the required libraries:

```
pip install beautifulsoup4 undetected-chromedriver sqlite3
```

## Usage

To run the script:

```
python web_scraping.py
```

The script will create a SQLite database called 'products.db' and a file called 'beautylish.html' containing the HTML of the scraped page.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.


# Web scraping techniques

## BeautifulSoup (bs4)

BeautifulSoup is a Python package for parsing HTML and XML documents. It provides a simple way to navigate and search the parse tree. BeautifulSoup is widely used for web scraping in Python due to its simplicity and ease of use.

## Selenium

Selenium is a powerful tool for automating web browsers. It can be used to simulate user interactions with a web page, such as clicking buttons, filling out forms, and navigating between pages. Selenium is often used for web scraping when the target website is heavily reliant on JavaScript, as it allows for dynamic web page interactions.

## Python-Playwright

Python-Playwright is a relatively new web scraping library that allows for automated web page interactions in a similar fashion to Selenium. It supports multiple browsers, including Chromium, Firefox, and WebKit.

## Scrapy

Scrapy is a popular web crawling framework in Python. It provides a powerful set of tools for scraping data from websites, including built-in support for handling requests, managing cookies, and handling form submissions. Scrapy is often used for large-scale web scraping projects.

## Test frameworks for scraping

There are several test frameworks available for web scraping in Python. Some of the most popular ones include:

### pytest

Pytest is a popular testing framework for Python that allows for testing of web scraping scripts. It provides support for fixtures, which allow for easy setup and teardown of testing environments.

### unittest

Unittest is a built-in testing framework in Python that provides support for test automation. It is often used for unit testing and integration testing of web scraping scripts.

### nose

Nose is an extension of the unittest framework that provides additional testing capabilities. It supports test discovery, which allows for automatic discovery of test cases within a project.

## Avoiding bot detection algorithms

Web scraping can sometimes trigger bot detection algorithms, which can result in IP blocks or CAPTCHAs. There are several techniques that can be used to avoid detection, including:

### Using proxies

Proxies can be used to route web scraping requests through different IP addresses, making it more difficult to track scraping activity. There are several free and paid proxy services available.

### Using request headers

Request headers can be modified to mimic human-like browsing behavior, such as using different user agents and referrers.

### Limiting request frequency

Slowing down web scraping requests can make it appear more like human browsing activity. It is important to not overload websites with requests, as this can result in IP blocks or CAPTCHAs.

## Usage of proxy, request-header, user-agent in scraping

Proxies, request headers, and user agents can be used to avoid bot detection algorithms in web scraping. Proxies can be used to route requests through different IP addresses, while request headers and user agents can be modified to mimic human browsing behavior. It is important to use these techniques responsibly and not overload websites with requests, as this can result in IP blocks or CAPTCHAs.


# My Experience

I worked as a scraper developer for eight years.
Most sites are relatively straightforward to scrape, even using beautiful-soup and the Python scrapy framework, but some are really difficult.
As I scraped increasingly difficult-to-scrape chores, my technique improved significantly.
Websites typically safeguard their data and access. There are numerous steps that a defensive system could perform.
Using Python Requests and Playwright, there are numerous ways to avoid bot detection.

## IP Rate Limit
The most basic kind of security is to block or throttle requests from the same IP address. Because a normal user would not request a hundred pages in a matter of seconds, they designate that connection as hazardous.
When making queries to the server, we must frequently modify our IP address, which we can accomplish by utilizing a proxy.

## Rotating Proxies
There are some free proxies available, however I do not advocate them. They may be useful for testing, but they are not trustworthy.
I usually buy proxy IP addresses and cycle them at random.

## User-Agent Header
The next step would be to examine our request headers. The most well-known is User-Agent, however there are numerous others.
Many websites do not check User-Agent, but those that do are a significant red signal. We'll have to swindle it. Fortunately, most libraries support custom headers. Following the Requests example:

```
import requests 
import random 
 
user_agents = [ 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36', 
	'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36', 
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36', 
	'Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148', 
	'Mozilla/5.0 (Linux; Android 11; SM-G960U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.72 Mobile Safari/537.36' 
] 
user_agent = random.choice(user_agents) 
headers = {'User-Agent': user_agent} 
response = requests.get('https://httpbin.org/headers', headers=headers) 
print(response.json()['headers']['User-Agent']) 
```

## Full Set of Headers
Each browser, and even each version, delivers a unique set of headers. Take a look at Chrome and Firefox in action:
It means just what you think it means. The prior array of five User Agents is inadequate. We need an array with all of the headers for each User-Agent. For the sake of brevity, we will give a list with only one item. It's already been far too long.
Simply copying the result from httpbin is insufficient in this scenario. It would be preferable if it could be copied directly from the source. The most straightforward method is to utilize the Firefox or Chrome DevTools - or the equivalent in your browser. Go to the Network tab, go to the target website, right-click on the request, and copy as cURL. The curl syntax is then converted in Python.


## Cookies
For basic circumstances, not transmitting cookies may be the best option. There is no need to keep a session open.

Session cookies may be the only means to reach and scrape the final material in more complex scenarios and with antibot software. We must keep in mind that the session requests and the IP address must match.

The same is true if we want content generated in the browser as a result of XHR calls. A headless browser will be required. Following the initial load, the Javascript will attempt to obtain some material via an XHR call. We can't make the call without cookies on a secure site.
