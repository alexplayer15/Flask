import flask
import numpy

def test_flask_version():
    assert flask.__version__ == '2.3.3'

def test_numpy_version():
    assert numpy.__version__ == '1.26.3'

# def check_health_status(website_url):

#     try:
#         response = requests.get(website_url)
    
#     except requests.ConnectionError: 
#         print('Could not connect to website. It might be down.')

#     else:
#         if response.status_code == 200:
#             print(f'The website is healthy, it has returned a status code of {response.status_code}')

#         else:
#             print(f'The website might be down, it has returned a status code of {response.status_code}')

# check_health_status('http://localhost:5000')
