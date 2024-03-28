
from django.shortcuts import render,redirect
from django.conf import settings
from django.http import HttpResponse 
from django.core.files.storage import FileSystemStorage
import urllib.parse
from PIL import Image

import json
import numpy as np








#Aas8QN2mLYFLeo11M9pV4Q==ojNlGuRVdNmbaAMX
# Create your views here.
def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query , headers = {'X-Api-Key':'Aas8QN2mLYFLeo11M9pV4Q==ojNlGuRVdNmbaAMX'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "oops! There was an error"
            print(e)
        return render(request, 'home.html',{'api':api})
    else:
         return render(request, 'home.html',{'query':'Enter a valid query'})


    return render(request , 'home.html')
def streamlit_app(request):
    # Redirect to the Streamlit app URL
    return redirect('http://localhost:8501')
    
def update_search_bar(request):
    if request.method == 'POST':
        prediction_result = request.POST.get('prediction', '')
        # Update your search bar with the prediction result
        # Example: You can pass the prediction result to the template context
        return render(request, 'home.html', {'prediction_result': prediction_result})
    else:
        return HttpResponse("Method not allowed", status=405)

