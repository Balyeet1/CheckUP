from supabase import create_client, Client


def connect_database(url, key):
    """Creates a connection to the database."""
    try:
        connection: Client = create_client(url, key)
        return connection
    except Exception as e:
        print("-------------Warning-----------\n",
              e,
              "\nPlease check you got the right url and key to connect to the database\n"
              "-------------Warning-----------")

        raise e
