import requests
import bs4

def search_images(text):
    # Make a request to the Google Images API
    url = 'https://www.google.com/search?q=' + text + '&tbm=isch'
    response = requests.get(url)

    # Parse the HTML response
    soup = bs4.BeautifulSoup(response.content, 'html.parser')

    # Find all the image results
    image_results = soup.find_all('img', class_='rg_i')

    # Return the URLs of the image results
    return [image['src'] for image in image_results]

if __name__ == '__main__':
    # Search for images of cats
    image_urls = search_images('cats')

    # Print the URLs of the first 5 image results
    for image_url in image_urls[:5]:
        print(image_url)
