import requests


def fetch_census_population_data(api_key, state_code=None):
    base_url = "https://api.census.gov/data/2020/dec"
    endpoint = "p1"

    params = {
        "get": "NAME,POP",
        "for": "state" if not state_code else f"state:{state_code}",
        "key": api_key
    }

    response = requests.get(f"{base_url}/{endpoint}", params=params)
    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    from config import API_KEY

    # Fetch data for all states (no specific state code provided)
    data = fetch_census_population_data(API_KEY)

    # Print the data in a readable format
    header = data[0]
    for row in data[1:]:
        print(f"{row[0]}: {row[1]} population")

    # If you want data for a specific state, you can use its code. For example, for California:
    # ca_data = fetch_census_population_data(API_KEY, state_code="06")
    # print(f"{ca_data[1][0]}: {ca_data[1][1]} population")
