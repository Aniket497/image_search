# image_search
#This program will first make a request to the Google Images API. The Google Images API is a web service that allows you to search for images on Google. The request will contain the text that you want to search for, in this case, "cats".

The response from the Google Images API will be an HTML document that contains the results of the search. The program will then parse the HTML document and find all the image results. The image results will be a list of <img> tags.

The program will then return the URLs of the image results. The URLs can be used to download the images from the web.

To run the program, you will need to have the requests and bs4 libraries installed. You can install the libraries by following the instructions on the following websites:

Requests: https://requests.readthedocs.io/en/master/
Beautiful Soup: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
Once you have installed the libraries, you can run the program by saving it as a Python file and then running it from the command line. For example, if you saved the program as search_images.py
