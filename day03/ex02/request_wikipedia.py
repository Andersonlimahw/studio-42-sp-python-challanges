import requests
import sys
import re
import os


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Function to log messages
def log_info(message):
    print(f"{bcolors.OKBLUE}[Info]: {message} {bcolors.ENDC}")

def log_warning(message):
    print(f"{bcolors.WARNING}[Info]: {message} {bcolors.ENDC}")

def log_error(message):
    print(f"{bcolors.WARNING}[Info]: {message} {bcolors.ENDC}")

# Function to clean the search query to create a valid file name
def clean_query(query):
    return re.sub(r'\s+', '_', query)

# Function to request data from Wikipedia and write it to a file
def request_wikipedia(query, language="en"):
    # Define the URL of the Wikipedia API
    base_url = f"https://{language}.wikipedia.org/w/api.php"
    
    # Define the parameters for the API request
    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "exintro": True,
        "explaintext": False,
        "meta": "siteinfo",
        "titles": query,
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    log_info(f"Api response code: {response.status_code}, base_url {base_url}")

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))

        log_info(f"Api response data: {data}")
        log_info(f"Api response data: page {page}")
        if "missing" not in page:
            # Extract the page content
            content = page["extract"]
            # Create a valid file name
            file_name = f"{clean_query(query)}.wiki"
            # Write the content to the file
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(content)           
            log_info(f"Data written to {file_name}")
        else:
            log_warning("No information found for the given query.")
    else:
        log_error("Error: Unable to connect to Wikipedia API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        log_info("Usage: python request_wikipedia.py <search_query>")
    else:
        try:
          search_query = sys.argv[1]
          request_wikipedia(search_query)
        except Exception as e:
          log_error(f"An error occurred: {str(e)}")
