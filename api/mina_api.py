import requests
from config import MINA_EXPLORER_API_BASE_URL

def get_validator_info(validator_address):
    # Fetching information about a specific validator from the MinaExplorer API
    url = f"{MINA_EXPLORER_API_BASE_URL}/validator/{validator_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # TODO error handeling
        return None

def get_uptime_data(validator_address):
    # Fetching uptime data for a specific validator
    url = f"{MINA_EXPLORER_API_BASE_URL}/uptime/{validator_address}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        # TODO error handeling
        return None

# TODO adding additional functions for other API interactions
