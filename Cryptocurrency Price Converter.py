import requests

def get_price(crypto, currency):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies={currency}'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        if crypto in data and currency in data[crypto]:
            return data[crypto][currency]
        else:
            raise KeyError(f"Data not found for {crypto}/{currency}")
    except requests.exceptions.RequestException as e:
        raise SystemExit(f"Error fetching data: {e}")
    except KeyError as e:
        raise ValueError(f"Error: {e}. Please enter valid cryptocurrency and currency codes.")

def main():
    print("Welcome to the Cryptocurrency Converter!")

    # List of example cryptocurrencies and fiat currencies that can be used
    print("\nExample cryptocurrencies: bitcoin, ethereum, litecoin, ripple, cardano")
    print("Example world currencies: usd, eur, inr, gbp, jpy, aud\n")

    while True:
        try:
            crypto = input("Enter the cryptocurrency (e.g., bitcoin): ").strip().lower()
            if not crypto:
                raise ValueError("Cryptocurrency cannot be empty.")
            currency = input("Enter the currency (e.g., usd): ").strip().lower()
            if not currency:
                raise ValueError("Currency cannot be empty.")
            
            price = get_price(crypto, currency)
            print(f"1 {crypto.upper()} = {price} {currency.upper()}")
            break  # Exit the loop if conversion successful
        except ValueError as ve:
            print(ve)
        except Exception as e:
            print(f"Error: {e}")
            retry = input("Do you want to retry? (yes/no): ").strip().lower()
            if retry != 'yes':
                break  # Exit the loop if user doesn't want to retry

if __name__ == "__main__":
    main()
