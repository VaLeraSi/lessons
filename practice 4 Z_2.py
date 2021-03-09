from requests import get, utils

response = get("http://www.cbr.ru/scripts/XML_daily.asp")
encodings = utils.get_unicode_from_response(response)


def currency_rates(currency):
    content = encodings.split("<Valute ID=")
    for i in content:
        if currency in i:
            return float(i.replace("/", "").split("<Value>")[1].replace(",", "."))


print(currency_rates("USD"))
print(currency_rates("EUR"))
