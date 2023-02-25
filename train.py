import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from yellowbrick.classifier import ConfusionMatrix

# "ID", **
# "FULLNAME",
# "EMAIL",
# "BIRTHDATE_DAY", **
# "BIRTHDATE_MONTH", **
# "BIRTHDATE_YEAR",
# "COUNTRY_NAME", **
# "COUNTRY_ABBREVIATION",
# "DDD",
# "MOBILE_DEVICE_OS",
# "CURRENCY_ID",
# "CURRENCY_NAME", **
# "AMOUNT",
# "AVG_AMOUNT_MONTH",
# "USE_ECOMMERCE",
# "LAST_STOCK_BOUGHT_TAG",
# "LAST_STOCK_BOUGHT_NAME", **
# "LAST_STOCK_BOUGHT_CATEGORY"

# "FULLNAME",
# "EMAIL",
# "BIRTHDATE_YEAR",
# "COUNTRY_ABBREVIATION",
# "DDD",
# "MOBILE_DEVICE_OS",
# "CURRENCY_ID",
# "AMOUNT",
# "AVG_AMOUNT_MONTH",
# "USE_ECOMMERCE",
# "LAST_STOCK_BOUGHT_TAG",
# "LAST_STOCK_BOUGHT_CATEGORY"


def trainModel():
    base = pd.read_csv("mock_data.csv")
    base = base.drop(columns=[
        'ID',
        'BIRTHDATE_DAY',
        'BIRTHDATE_MONTH',
        'CURRENCY_NAME',
        'COUNTRY_NAME',
        'LAST_STOCK_BOUGHT_NAME',
    ])
    base.LAST_STOCK_BOUGHT_TAG.unique()

    x = base.iloc[:,[0,1,2,3,4,5,6,7,8,9,11]].values
    y = base.iloc[:,10].values

    encoder = LabelEncoder()
    x[:,0] = encoder.fit_transform(x[:,0])
    x[:,1] = encoder.fit_transform(x[:,1])
    x[:,2] = encoder.fit_transform(x[:,2])
    x[:,3] = encoder.fit_transform(x[:,3])
    x[:,4] = encoder.fit_transform(x[:,4])
    x[:,5] = encoder.fit_transform(x[:,5])
    x[:,6] = encoder.fit_transform(x[:,6])
    x[:,7] = encoder.fit_transform(x[:,7])
    x[:,8] = encoder.fit_transform(x[:,8])
    x[:,9] = encoder.fit_transform(x[:,9])
    x[:,10] = encoder.fit_transform(x[:,10])

    xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.5,random_state=1)
    model = GaussianNB()
    model.fit(xtrain, ytrain)
    predicts = model.predict(xtest)
    accuracyPercentage = accuracy_score(ytest, predicts)

    print("Predicts:")
    print(predicts)
    print("")
    print("YTest")
    print(ytest)
    print("")
    print("Acertos:{:10.2f}%".format(accuracyPercentage * 100))

    confusao = ConfusionMatrix(model, classes=['APPL','BBAS3.SA','DIS','NKE','ADSG-U.TI','ADDYY','ADDDF','ADS.F',"SBUX"])
    confusao.fit(xtrain, ytrain)
    confusao.score(xtest, ytest)
    confusao.poof()