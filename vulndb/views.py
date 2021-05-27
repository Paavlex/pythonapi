from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Vulnerability
from .serializers import VulnerabilitySerializer




#Seznam moznych URLs
@api_view(['GET'])
def vulnerabiltyOverview(request):
    api_urls = {
        'List': 'vulnerability-list/',
        'Search': 'vulnerability-search/<str:whatToSearch>',
        'Save': 'vulnerability-save/',
    }
    return Response(api_urls
    #zakomentovano aby bylo mozne prohlednou api v prohliozeci, jinak se posila souboru .json, ktery se v prohlizeci jen stahne
    #, headers={'Content-Disposition': 'attachment; filename="api.json"'}
    )
  

#Ziskani vsech polozek v databazi
@api_view(['GET'])
def vulnerabilityList(request):
    #ziskani vsech objektu
    vulnerabilities = Vulnerability.objects.all()
    #serializace
    serializer = VulnerabilitySerializer(vulnerabilities, many = True)
    #vlozeni dat do odpovedi
    return Response(serializer.data, 
    #headers={'Content-Disposition': 'attachment; filename="api.json"'}
    )


#Ziskani vyhledavanych polozek
@api_view(['GET'])
def vulnerabilitySearch(request, whatToSearch):
    vulnerabilities = Vulnerability.objects.all()

    #Fltrovani pomoci hledaneho retezce
    vulnerabilities = vulnerabilities.filter(name__icontains=whatToSearch)
    serializer = VulnerabilitySerializer(vulnerabilities, many = True)
    return Response(serializer.data, 
    #headers={'Content-Disposition': 'attachment; filename="api.json"'}
    )

#Ulozeni do databaze
@api_view(['POST'])
def vulnerablitySave(request):
    #serilalizace dat z zadosti
    serializer = VulnerabilitySerializer(data=request.data)

    #kontrola validity a ulozeni v kladnem pripade
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data, 
    #headers={'Content-Disposition': 'attachment; filename="api.json"'}
    )