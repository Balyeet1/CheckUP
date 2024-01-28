from supabase import create_client, Client
from gotrue.errors import AuthApiError

try:
    supabase: Client = create_client("https://plccucouimuhvrhrhdmr.supabase.co",
                                     "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsY2N1Y291aW11aHZyaHJoZG1yIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc4MDMxMTUsImV4cCI6MjAxMzM3OTExNX0.mb6oiQRacpYxMKJ8hJlHdq2tieeJcazyL_AiiZ6w5OQ")
except Exception as e:
    print(e)
    print("Please check you got the right url and key to connect to the database")
    pass


def sign_up_user(user_email, password):
    try:
        return supabase.auth.sign_up({
            "email": user_email,
            "password": password,
        })

    except AuthApiError as ex:
        print(ex)


# sign_up_user("ricardoldias123@gmail.com", "Vir22222123")


def sign_in_user(user_email, password):
    try:
        return supabase.auth.sign_in_with_password({
            "email": user_email,
            "password": password,
        })
    except AuthApiError as ex:
        print(ex)


# print(sign_in_user("ricardoldias123@gmail.com", "ViraMilho_123"))

print(sign_in_user("ricardoldi@gmail.com", "ViraMilho_123"))
