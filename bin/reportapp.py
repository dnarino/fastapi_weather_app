import requests
from typing import Dict, Any, Optional

# Base configuration for client application
BASE_URL = "http://127.0.0.1:8000"


def api_request(method: str, endpoint: str, **kwargs: Any) -> Optional[Any]:
    """
    Sends an HTTP request to the API, handles network/http errors gracefully,
    and returns the parsed JSON response or None if an error occurs.
    """
    url = f"{BASE_URL}/{endpoint.lstrip('/')}"
    kwargs.setdefault("timeout", 5)

    try:
        response = requests.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.ConnectionError:
        print("\n❌ Error: Could not connect to the weather service. Is the API server running?")
    except requests.exceptions.Timeout:
        print("\n❌ Error: The request timed out. Please try again later.")
    except requests.exceptions.HTTPError as err:
        try:
            detail = err.response.json().get("detail", err.response.text)
        except ValueError:
            detail = err.response.text
        print(f"\n❌ Server Error ({err.response.status_code}): {detail}")
    except Exception as err:
        print(f"\n❌ An unexpected error occurred: {err}")

    return None


def main() -> None:
    choice: str = input("[R]eport weather or [s]ee reports: ")
    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        elif choice.lower().strip() == 's':
            see_events()
        else:
            print(f"Don't know what to do with {choice}")
        choice = input("[R]eport weather or [s]ee reports: ")


def report_event() -> None:
    desc: str = input('How is the climate today? ')
    city: str = input('What city? ')

    data: Dict[str, Any] = {
        'description': desc,
        'location': {
            'city': city
        }
    }

    result = api_request("POST", "api/reports", json=data)
    if result:
        print(f"Reported new event: {result.get('id')}")


def see_events() -> None:
    data = api_request("GET", "api/reports")
    if data:
        for r in data:
            location = r.get('location') or {}
            city = location.get('city', 'Unknown')
            print(f"{city} has {r.get('description')}")


if __name__ == '__main__':
    main()