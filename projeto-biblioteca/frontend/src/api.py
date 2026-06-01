import httpx

API_URL = "http://127.0.0.1:5000/api"

def get_books():
    try:
        response = httpx.get(f"{API_URL}/books/")
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Erro na API: {e}")
        return []

def add_book(title, author, year):
    try:
        response = httpx.post(f"{API_URL}/books/", json={
            "title": title,
            "author": author,
            "year": year
        })
        response.raise_for_status()
        return response.json(), None
    except httpx.HTTPStatusError as e:
        return None, e.response.json()
    except Exception as e:
        return None, {"errors": str(e)}