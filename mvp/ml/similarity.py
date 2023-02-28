from fuzzywuzzy import fuzz
import csv

def findDuplicatedUsers(csvfilename : str):
    file = open(f"{csvfilename}.csv")
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)

    for row in rows:
        k = row[0]
        full_name = row[1]
        email = row[2]
        birth_day = row[3]
        birth_month = row[4]
        birth_year = row[5]
        country_name = row[6]
        country_tag = row[7]
        ddd = row[8]
        mobile_os = row[9]
        currency_tag = row[10]
        currency_name = row[11]
        amount = row[12]
        amount_per_month = row[13]
        use_ecommerce = row[14]
        last_stock_tag = row[15]
        last_stock_name = row[16]
        last_stock_category = row[17]

        print(row)

    return

findDuplicatedUsers("mock_data")

# for instagramUser in instagramUsers:
#         nameSimilarPercentage = fuzz.partial_token_sort_ratio(facebookUser.name, instagramUser.name)
#         emailSimilarPercentage = fuzz.partial_token_sort_ratio(facebookUser.email, instagramUser.email)

#         if nameSimilarPercentage >= 70 and facebookUser.age == instagramUser.age and emailSimilarPercentage >= 40:
#             userFound = [facebookUser, instagramUser]
#             break

#     if userFound == "":
#         print("User not found")
#     else:
#         print("User found!")
#         print(f"Name({nameSimilarPercentage}): {userFound[0].name} - {userFound[1].name}")
#         print(f"Email({emailSimilarPercentage}): {userFound[0].email} - {userFound[1].email}")
#         print(f"Age: {userFound[0].age} - {userFound[1].age}")