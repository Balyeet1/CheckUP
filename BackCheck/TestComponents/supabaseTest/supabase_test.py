from supabase import create_client, Client

supabase: Client = create_client("https://plccucouimuhvrhrhdmr.supabase.co",
                                 "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InBsY2N1Y291aW11aHZyaHJoZG1yIiwicm9sZSI6ImFub24iLCJpYXQiOjE2OTc4MDMxMTUsImV4cCI6MjAxMzM3OTExNX0.mb6oiQRacpYxMKJ8hJlHdq2tieeJcazyL_AiiZ6w5OQ")


def sign_up_user(user_email, password):
    data = supabase.auth.sign_up({
        "email": user_email,
        "password": password,
    })

    return data


#sign_up_user("ricardoldias123@gmail.com", "Teste12345")


def sign_in_user(user_email, password):
    try:
        data = supabase.auth.sign_in_with_password({
            "email": user_email,
            "password": password,
        })
    except Exception as e:
        print(e.args, e)
        return "Something went wrong"

    return data


print(sign_in_user("ricardoldias123@gmail.com", "Teste12345"))
