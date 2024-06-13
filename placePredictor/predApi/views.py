from django.shortcuts import redirect, render
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pandas as pd

# api that predicts placement possibility of  a student based on the data provided by her/him
# def index(request):
#     return render(request, 'predictor/firstPage.html')


def predict(request):
    return render(request, 'predictor/main.html')


def result(request):

    # reading the data
    dataframe = pd.read_csv("collegePlace.csv")

    # data preprocessing
    dataframe['Gender'].replace({'Male': 0, 'Female': 1}, inplace=True)
    dataframe['Stream'].replace({
        'Electronics And Communication': 0,
        'Computer Science': 1,
        'Information Technology': 2,
        'Mechanical': 3,
        'Electrical': 4,
        'Civil': 5
    }, inplace=True)
    # cleaning the data
    Y = dataframe["PlacedOrNot"]
    X = dataframe.drop(["PlacedOrNot"], axis=1)

    # dividing the data
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)

    # model training and fitting
    model = LogisticRegression()
    model.fit(X_train, Y_train)

    # user input
    val1 = float(request.GET['n1'])
    val2 = float(request.GET['n2'])
    val3 = float(request.GET['n3'])
    val4 = float(request.GET['n4'])
    val5 = float(request.GET['n5'])
    val6 = float(request.GET['n6'])
    val7 = float(request.GET['n7'])

    pred = model.predict([[val1, val2, val3,
                           val4, val5, val6, val7]])
    pred_proba = model.predict_proba([[val1, val2, val3, val4, val5, val6, val7]])*100
    

    # results
    result1 = ""
    if pred == [0]:
        result1 = "You are not placed, Work Hard!!."
    else:
        result1 = "You will be placed most probably."
    redirect('predict/')
    return render(request, "predictor/main.html",
                  {"result2": result1, "pred_proba": pred_proba[0][1]})
