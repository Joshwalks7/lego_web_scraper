# LEGO My Wallet

A simple Python web scraper that compares LEGO set prices across three mock storefronts:

- Balmart
- Camazon
- Marget

The program fetches product data from each storefront, lets the user enter a LEGO set number, and then shows the available prices sorted from cheapest to most expensive.

## What it does

- Scrapes set names and prices from HTML pages using `requests` and `BeautifulSoup`
- Checks whether a set is available in any of the three stores
- Displays the cheapest and most expensive price options for a given set
- Repeats until the user decides to stop

## Requirements

- Python 3
- `requests`
- `beautifulsoup4`

Install the dependencies with:

```bash
python -m pip install requests beautifulsoup4
```

## Run the program

```bash
python lego_my_wallet.py
```

When the script runs, it will ask for a set number such as:

- 10316
- 75313
- 42146
- 60442

Then it will compare the price across the available stores.

## Run the tests

```bash
python -m pytest
```

This project includes a basic test file that checks the set-price comparison logic.
