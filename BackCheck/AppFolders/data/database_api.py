from database import supabase


def sign_in_user(user_email):
    data = supabase.auth.sign_in_with_otp({
        "email": 'example@email.com'
    })

    return data
