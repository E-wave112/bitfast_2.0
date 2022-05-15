from decouple import config

def get_url():
    if config('ENV') == 'development':
        return "http://127.0.0.1:8000"
    return "https://bitfast.herokuapp.com"
    