import requests

def get_supported_currencies():
    """Returns a list of currencies supported by Frankfurter API."""
    url = "https://api.frankfurter.app/currencies"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return list(data.keys())
        else:
            print(f"Failed to get currencies. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching supported currencies: {e}")

    # Fallback currency list (common ones)
    return [
        "USD", "EUR", "GBP", "INR", "AUD", "CAD", "CHF", "CNY", "JPY",
        "HKD", "SGD", "SEK", "NOK", "ZAR", "BRL", "MXN", "KRW", "THB"
    ]

def get_exchange_rate(from_currency, to_currency):
    """Get exchange rate between two currencies using Frankfurter API."""
    if from_currency == to_currency:
        return 1.0  # No conversion needed
    url = f"https://api.frankfurter.app/latest?from={from_currency}&to={to_currency}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return data["rates"].get(to_currency)
        else:
            print(f"Error fetching rate. Status code: {response.status_code}")
    except Exception as e:
        print(f"Exception during API call: {e}")
    return None

def convert_currency(amount, from_currency, to_currency):
    rate = get_exchange_rate(from_currency, to_currency)
    if rate:
        return amount * rate
    return None

def main():
    print("💱 Currency Converter (Frankfurter API, No Key Required)")

    supported = get_supported_currencies()
    print("\nSupported currencies:", ", ".join(sorted(supported)))

    from_currency = input("\nEnter the currency you are converting from (e.g., USD): ").upper()
    to_currency = input("Enter the currency you are converting to (e.g., EUR): ").upper()

    if from_currency not in supported:
        print(f"'{from_currency}' is not supported.")
        return
    if to_currency not in supported:
        print(f"'{to_currency}' is not supported.")
        return

    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount.")
        return

    converted = convert_currency(amount, from_currency, to_currency)

    if converted is not None:
        print(f"\n✅ {amount:.2f} {from_currency} = {converted:.2f} {to_currency}")
    else:
        print("\n❌ Conversion failed. Try again later or with different currencies.")

if __name__ == "__main__":
    main()
