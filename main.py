import requests


def fetch_census_data(api_key, endpoint, params):
    base_url = "https://api.census.gov/data/2020/dec/pl"

    # Add the API key to the parameters
    params['key'] = api_key

    # Make the request
    response = requests.get(f"{base_url}/{endpoint}", params=params)

    # Check the response status
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
    # Adjust according to the specific data table or endpoint you're interested in
    ENDPOINT = "P1"
    PARAMS = {
        "get": "NAME",  # Columns or fields you want to retrieve
        "for": "state:*"  # Geographic filters or other conditions
    }

    data = fetch_census_data(API_KEY, ENDPOINT, PARAMS)
    for row in data:
        print(row)
