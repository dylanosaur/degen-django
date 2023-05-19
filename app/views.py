from django.shortcuts import render

# Create your views here.

import requests
from bs4 import BeautifulSoup
import random

def home(request):
    search_url = 'https://www.google.com/search'
    query = 'catgirl'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36'
    }

    # Perform a Google search for the query
    params = {
        'q': query,
        'tbm': 'isch'
    }
    response = requests.get(search_url, headers=headers, params=params)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract image URLs from the search results
    image_results = soup.find_all('img')
    image_urls = [img['data-src'] for img in image_results if 'data-src' in img.attrs and 'catgirl' in img['alt'].lower()]

    # Select a random image URL
    random_image_url = random.choice(image_urls)

    return render(request, 'home.html', {'catgirl_url': random_image_url})
