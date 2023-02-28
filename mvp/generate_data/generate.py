import random
import csv

def generateRandomName() -> str:
    with open("names.txt") as f:
        lines = f.readlines()
        randomFirstName = lines[random.randint(0, len(lines) - 1)].upper().split()

    return randomFirstName[0].upper()


def generateRandomCountry() -> list[str]:
    file = open('country.csv')
    csvReader = csv.reader(file)
    rows = []
    for row in csvReader:
        rows.append(row)
    
    return rows[random.randint(1, len(rows) - 1)]


def generateRandomEmailExtension() -> str:
    file = open('email_extensions.csv')
    csvReader = csv.reader(file)
    rows = []
    for row in csvReader:
        rows.append(row)

    return rows[random.randint(1, len(rows) - 1)][0]


def generateRandomEmail(name : str, country : list[str], extension : str) -> str:
    name = name.lower()
    name = name.replace(" ", "-").lower()
    return f"{name}{generateRandomName().lower()}@{extension}.com.{country[0]}"


def generateRandomBirthdate() -> list[int]:
    return [random.randint(1, 30), random.randint(1, 12), random.randint(1970, 2004)]


def generateRandomMobileOS() -> str:
    file = open('mobile_os.csv')
    csvReader = csv.reader(file)
    rows = []
    for row in csvReader:
        rows.append(row)
    
    return rows[random.randint(1, len(rows) - 1)]


def generateRandomCurrency() -> list[str]:
    file = open('currency.csv')
    csvReader = csv.reader(file)
    rows = []
    for row in csvReader:
        rows.append(row)
    
    return rows[random.randint(1, len(rows) - 1)]


def generateRandomAmount() -> int:
    return random.randint(100, 1_000_000)


def generateRandomStock() -> list[str]:
    file = open('stocks.csv')
    csvReader = csv.reader(file)
    rows = []
    for row in csvReader:
        rows.append(row)
    
    return rows[random.randint(1, len(rows) - 1)]


def generateFullRow(id : int) -> str:
    name = f"{generateRandomName()} {generateRandomName()}"
    countryObject = generateRandomCountry()
    country_abbreviation = countryObject[0]
    country_name = countryObject[1]
    country_ddd = countryObject[2]
    extension = generateRandomEmailExtension().upper()
    email = generateRandomEmail(name, country_abbreviation, extension).lower()
    birthdate = generateRandomBirthdate()
    mobile_os = generateRandomMobileOS()
    currency = generateRandomCurrency()
    currency_id = currency[0]
    currency_name = currency[1]
    amount = generateRandomAmount()
    avg_amount_month = generateRandomAmount() / 12
    use_ecommerce = random.randint(0, 1) % 2 == 0
    stock = generateRandomStock()
    stock_id = stock[0]
    stock_name = stock[1]
    stock_category = stock[2]

    row = f'"{id}","{name}","{email}","{birthdate[0]}","{birthdate[1]}","{birthdate[2]}","{country_name}","{country_abbreviation}","{country_ddd}","{mobile_os[0]}","{currency_id}","{currency_name}","{amount}","{avg_amount_month}","{use_ecommerce}","{stock_id}","{stock_name}","{stock_category}"'
    return row


i = 6_001
while i <= 10_000:
    row = generateFullRow(i)
    print(row)
    i += 1