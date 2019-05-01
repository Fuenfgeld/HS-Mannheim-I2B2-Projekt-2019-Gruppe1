# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd

# Create your views here.

def index(request):
    return render( #wenn html-Template benutzt werden soll
        request,
        "tbdApp/index.html"
    )

def age(request):
    df = pd.read_csv("beispieldaten_header.csv", sep = ";")
    count = df.groupby('Age').size()
    under33 = count[:23]
    under66 = count[23:50]
    under99 = count[50:]
    list33 = under33.tolist()
    list66 = under66.tolist()
    list99 = under99.tolist()
    finList = [len(list33), len(list66), len(list99)]
    labels = ["0-33 Jahre", "34-66 Jahre", "67-99 Jahre"]
    colors = ['#2E64FE', '#2E64FE', '#2E64FE']

    return render(
        request,
        "tbdApp/barchart.html",
        {
            'title': "Altersverteilung",
            'labels': labels,
            'data': finList,
            'colors': colors
        }
    )
def race(request):
    df = pd.read_csv("beispieldaten_header.csv", sep = ";")
    count = df.groupby("Race").size()
    data = count.tolist()
    labels = ['Asiatisch', 'Afrikanisch', 'Spanisch', 'Indisch', 'Europaeisch']
    colors = ['#FFFF00', '#190707', '#FF0000', '#8A4B08', '#F7F8E0']

    return render(
        request,
        "tbdApp/piechart.html",
        {
            'title': "Ethnische Verteilung",
            'labels': labels,
            'data': data,
            'colors': colors
        }
    )

def sex(request):
    dataframe = pd.read_csv("beispieldaten_header.csv", sep = ";") #Dataframe
    count = dataframe.groupby('Sex').size() #Series
    data = count.tolist() #Series in Liste umwandeln / Reihenfolge wichtig!
    labels = ['Weiblich', 'Maennlich']
    colors = ['#FF0000', '#0040FF']

    return render(
        request,
        "tbdApp/piechart.html",
        {
            'title': "Geschlechterverteilung",
            'labels': labels,
            'data': data,
            'colors': colors,
        }
    )