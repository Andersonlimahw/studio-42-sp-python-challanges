import requests
import sys
import re
import os

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

    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        page = next(iter(data["query"]["pages"].values()))        

        print(f"Api response data: {data}")
        print(f"Api response data: page {page}")
        if "missing" not in page:
            # Extract the page content
            content = page["extract"]
            # Create a valid file name
            file_name = f"{clean_query(query)}.wiki"
            
            # Write the content to the file
            with open(file_name, "w", encoding="utf-8") as file:
                file.write(content)           
            print(f"Data written to {file_name}")
        else:
            print("No information found for the given query.")
    else:
        print("Error: Unable to connect to Wikipedia API.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python request_wikipedia.py <search_query>")
    else:
        try:
          search_query = sys.argv[1]
          request_wikipedia(search_query)
        except Exception as e:
          print(f"An error occurred: {str(e)}")
