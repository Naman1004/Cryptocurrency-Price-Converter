# Cryptocurrency Price Converter

## Overview
This is a simple cryptocurrency price converter that fetches a given cryptocurrency's current value in a specified fiat currency. It uses the CoinGecko API to retrieve real-time prices. The program supports popular cryptocurrencies like Bitcoin, Ethereum, and Litecoin, and currencies such as USD, EUR, and INR.

## Features
1. Fetches real-time prices of cryptocurrencies from the CoinGecko API.
2. Allows users to input a cryptocurrency and a fiat currency to get the conversion rate.
3. Handles errors such as invalid inputs or failed API requests.
4. Interactive prompt to retry in case of invalid input or connection issues.

## How It Works
1. The user is prompted to enter a cryptocurrency name (e.g., Bitcoin, Ethereum).
2. Then, the user enters the fiat currency code (e.g., USD, EUR) they want the cryptocurrency price in.
3. The program fetches the current price of the selected cryptocurrency in the specified currency and displays it.
4. The program will prompt the user to retry if an error occurs (e.g., invalid cryptocurrency, unavailable data, or connection issues).

## Requirements
1. Python 3.x
2. Requests library for making API calls
