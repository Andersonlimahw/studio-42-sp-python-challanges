import sys
import requests
from bs4 import BeautifulSoup


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
    print(f"{bcolors.WARNING}[Warning]: {message} {bcolors.ENDC}")

def log_error(message):
    print(f"{bcolors.FAIL}[Fail]: {message} {bcolors.ENDC}")


def log_success(message):
    print(f"{bcolors.OKGREEN}[Success]: {message} {bcolors.ENDC}")    

# Function to fetch the first valid link from a Wikipedia article
def get_first_valid_link(url):
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', {'id': 'mw-content-text'})
    
    # Find the first link that leads to another Wikipedia article
    for paragraph in content.find_all('p'):
        for tag in paragraph.find_all(['a', 'i']):
            link = tag.get('href', '')
            if link.startswith('/wiki/') and not link.startswith('/wiki/Help:'):
                return link

    return None

# Function to find the path to Philosophy
def find_roads_to_philosophy(start_url):
    visited = set()
    current_url = start_url
    roads = [current_url]

    while current_url != '/wiki/Philosophy':
        if current_url in visited:
            log_error("It leads to an infinite loop !")
            return

        visited.add(current_url)

        current_url = get_first_valid_link(f"https://en.wikipedia.org{current_url}")
        
        if current_url is None:
            log_error("It's a dead end !")
            return
        
        roads.append(current_url)

    total_roads = len(roads)
    log_success(f"{total_roads} roads from {start_url} to philosophy !")
    
    for road in roads:
        log_info(road.lstrip('/wiki/').replace('_', ' '))
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        log_warning("Usage: python roads_to_philosophy.py <search_query>")
    else:
        search_query = sys.argv[1]
        response = requests.get(f"https://en.wikipedia.org/wiki/{search_query}")

        if response.status_code != 200:
            log_error("Error: Unable to connect to Wikipedia.")
        else:
            find_roads_to_philosophy(f"/wiki/{search_query}")
