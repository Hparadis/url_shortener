import random
import string
from services.db import db
from services.database import URL
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def create_short_url(long_url):
    short_code = generate_short_code()
    # long_url = "https://www.google.com" we used this to find a bug 

    print("Generated code:", short_code)

    new_url = URL(
        long_url=long_url,
        short_code=short_code
    )

    db.session.add(new_url)
    db.session.commit()
    print("LONG URL:", long_url)

    return short_code
def get_long_url(short_code):
    print("SEARCHING FOR:", short_code)

    url = URL.query.filter_by(short_code=short_code).first()

    print("QUERY RESULT:", url)

    return url.long_url if url else None