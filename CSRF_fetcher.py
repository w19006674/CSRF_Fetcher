import requests
from bs4 import BeautifulSoup
import os

# Function to extract CSRF token and cookies (if needed dynamically)
def get_csrf_token_and_cookies(session, url):
    response = session.get(url)
    if response.status_code != 200:
        print(f"Failed to fetch the page, status code: {response.status_code}")
        return None, None
    soup = BeautifulSoup(response.text, 'html.parser')
    token_element = soup.find('input', {'name': 'logintoken'})
    if token_element is None:
        print("CSRF token not found on the page")
        return None, None
    token = token_element['value']
    cookies = session.cookies.get_dict()
    return token, cookies

# Main script to connect to login page
login_url = "http://192.168.200.138/moodle/login/index.php"
session = requests.Session()

token, cookies = get_csrf_token_and_cookies(session, login_url)

username = 'w19006674'
password = 'Testingpassword1234!'
print("CSRF Token:", token)

# Prepare login data
login_data = {
    'username': username,
    'password': password,
    'logintoken': token
}

# Convert login data to a URL-encoded string
login_data_str = '&'.join([f"{key}={value}" for key, value in login_data.items()])
content_length = len(login_data_str)

# Prepare cookies string if there are any

cookies_str = '; '.join([f"{key}={value}" for key, value in cookies.items()])

# Save login data to a file
with open("login_data.txt", "w") as f:
    f.write("POST /moodle/login/index.php HTTP/1.1\n")
    f.write("Host: 192.168.200.138\n")
    f.write("Content-Type: application/x-www-form-urlencoded\n")
    f.write(f"Content-Length: {content_length}\n")
    if cookies_str:
        f.write(f"Cookie: {cookies_str}\n")
    f.write("\n")
    f.write(login_data_str)

# Print message to show file has been created successfully
print("login_data.txt file created successfully")