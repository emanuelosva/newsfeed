"""Firebase connection and db methods"""

# Required imports
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firestore DB
key = {
    "type": "service_account",
    "project_id": "newsfeed-master-afd51",
    "private_key_id": "970bae9b910ea3df198ea72872d3f41199f6f33d",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQC/wK/sgTMs++wX\nEXMGKtmxAYdwUDw0gWEVdG7dk4xvEGV9qYoLvoPhyff5QhrfNR2INMUxvKDRoBYW\nYe4SNgCGfRyP1/rEn/o/1ulHEp0obigQ2Vkq/7yJdlAu9LhdrO1UCP9M9xzztAD7\nsbD6SK4r4ATnFXh2S1E50kYjNh+dl4Uj9WspBoohVWnpBho3cwDZAQJFQAL7RY4n\nU8Rmh4YAiuNbe9aRoygSJk3In8mULGUhtg4d30q6c3fbg0xOwCSYh7laBZ0LAMt7\n4zyumixDdEt202VJkKH4rNTxZUEDzcybLwgA5f21bqXofqIfbOV0l1LcaxYwVJQp\nWR3IcoKjAgMBAAECggEAWp95RUAGbKMfAAP6JZcIzRPY66av3Wyr8lTVtJhwDWll\nXc9Lc6N1drdaH44zXvweWen+rDPmmUucRLXBqw+kjesBHaZIWLb2sUcjdriAV8Q/\n4T6nWqAEfb7RxG9Z1sPMYiPibIB5SV/v+wQOjSreTdQQ3RmTleyglcAf77I7nOFW\nYbJy+bFZRMWeJOK0cGr1KjmSYu3dIP7G7dEYVb1S3vuQJ3/iBv1qwybWMFCvt0Dq\n77EnN2I0dF6upxdmhBj8m/APLJkg3c77RyZ8kjuhQeffBwL6BEKTlhV0tWAatcd5\n+FicAD6lSWbMo++3enOcdIUhxX44K9Jn1J7EvPUgeQKBgQDs5eP53aLu2gGGR89V\nvhsWY6wRUA7MRDgxQKhCEwuBP1jbU7Ygzibugpf1zBNJK2rtQ9bzrfaUQYgUHGYv\nJSKljwEghX0Cs5Ma8EHjaRT/X0ffpClEDUgBz543k12WHbH837rDAYOAW40jdNCa\n+s3qymMlyQp8Cf2CK2JHZ4ksZQKBgQDPNuUxa1tALYp/m42wyP4TbX+eNciAKU2/\n+ulQwrzawZ8j1Y1gvWo1aCrHC6zgWlX8NH2fnoFOsnxlLaUH+X2emlX/Ds0cHWyS\ntwqXta2c/RecHAslsl90nyz1TYaYtT4sFvqaGzEmYBZftPbTLY4V8olbACcFVVcD\n6oT0pfGuZwKBgQDkId8RWKb3bWnabnz0DUb4oLOrWHVnsKqMg7+FIeIKbX6ceFkD\n7oL/XTQJuKU56V3nb1UpBXZX/2OUOmUNMa3T0Ys8TlC8sUIQxx4saZ2W76K/c89p\ngYC+fbnXu0p8rcwhwTKRaHvCuGeKpYveM3jpik1ArgIywUwodq8GJGatIQKBgQC1\nRzsfDuKXtL+zf2xnuo68hFDfIgI0TO4eA+5VnugFINqOSOcUOOFPs7+ovsgQxjbv\nGyTDnbFWHcPB6Dq2TUfelvqg1lwOOpefis6ThndKHgino8kEw5XKuu5j89zKf9TS\nUZAPfbZz8h/gvrooaXQiMzqDCBEbE1u6q1KBjSNwBQKBgQCzE5i4T147Sp85j3Mb\n3mvCDUUBOGNBkT3vEirljZVgZOOu06lBYF1QcCI6rc+6X5U9IOSORBglCuOhXWN6\nt6nd+9PWFPV0dpm+EXgBGM02LPExQACCR/ULydevro5Njh4pmy+gbvDFxwXCHGI6\ntyrBahxGpooE8p8IUk9nf8c9bw==\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-r6f2z@newsfeed-master-afd51.iam.gserviceaccount.com",
    "client_id": "108668210412025186178",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-r6f2z%40newsfeed-master-afd51.iam.gserviceaccount.com"
}
cred = credentials.Certificate(key)
default_app = initialize_app(cred)
db = firestore.client()


# ------------------------- Db methods ---------------------------#

def user_add(user_data):
    """Add new user to database"""
    user = db.collection('users').document(user_data["email"])
    user.set({
        'username': user_data["username"],
        'password': user_data["password"],
        'news_sites': []
    })


def get_user_by_email(user_email):
    """get user by UID from database"""
    return db.collection('users').document(user_email).get()


def add_news_site(user_id, news_name):
    news_sites = db.collection('users').document(user_id).news_sites
    news_sites.add(news_site_name)


def delete_news_site(user_id, news_name):
    news_sites = db.collection('users').document(user_id).news_sites
    for news_site in news_sites:
        if news_site == news_name:
            news_site.delete()
