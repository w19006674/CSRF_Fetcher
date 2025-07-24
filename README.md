# CSRF_Fetcher

# Moodle CSRF Token Fetcher & Login Request Generator

This Python script automates the login process for a Moodle instance by:

- Fetching the login page to extract the CSRF token (`logintoken`)
- Capturing the necessary session cookies
- Constructing a raw HTTP POST login request
- Saving the request to a `login_data.txt` file for debugging or reuse

---

## 🔧 Use Case

This script is useful for:

- Simulating and testing login requests
- Understanding web application authentication flows
- Practicing HTTP request crafting and CSRF token handling
- Automation or SRE training scenarios

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install requests beautifulsoup4
