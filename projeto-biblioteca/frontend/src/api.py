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
        response = httpx.post(f"{API_URL}/books/", json={"title": title, "author": author, "year": year})
        response.raise_for_status()
        return response.json(), None
    except httpx.HTTPStatusError as e:
        return None, e.response.json()
    except Exception as e:
        return None, {"errors": str(e)}

def update_book(book_id, title, author, year):
    try:
        response = httpx.put(f"{API_URL}/books/{book_id}", json={"title": title, "author": author, "year": year})
        response.raise_for_status()
        return response.json(), None
    except httpx.HTTPStatusError as e:
        return None, e.response.json()
    except Exception as e:
        return None, {"errors": str(e)}

def delete_book(book_id):
    try:
        response = httpx.delete(f"{API_URL}/books/{book_id}")
        response.raise_for_status()
        return True, None
    except Exception as e:
        return False, str(e)