# BackCheck

## Setup

1. If you don’t have Python installed, [install it from here](https://www.python.org/downloads/)

2. Clone this repository. [GitHub CheckUp](https://github.com/Balyeet1/CheckUP)

3. Enter the directory BackCheck:

   ```bash
   $ cd BackCheck
   ```

4. Install the requirements:

   ```bash
   $ pip install -r requirements.txt
   ```

5. Make a copy of the example environment variables file:

   ```bash
   $ cp env_example ..env
   ```

6. Fill the environment variables, contained in the .env file.

7. Run the backend app:

   ```bash
   $ python3 my_app.py
   ```
   
8. Enjoy in dev environment :)


9. Access the .env file and change the variable FLASK_ENV to "production"


10. Run the backend app in production:

   ```bash
   $ waitress-serve --threads=4 --listen=*:8080 my_app:app
   ```
   
11. Enjoy in prod environment :)
