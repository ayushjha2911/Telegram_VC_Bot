HEROKU = True  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku & Docker.
if HEROKU:
    from os import environ

    from dotenv import load_dotenv

    load_dotenv()  # take environment variables from .env.
    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SESSION_STRING = environ[
        "SESSION_STRING"
    ]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]
    CHAT_ID = int(environ["CHAT_ID"])
    DEFAULT_SERVICE = environ.get("DEFAULT_SERVICE") or "youtube"

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 7402428
    API_HASH = "7486f6b7f5560472bdef864c05bf7c3e"
    ARQ_API_KEY = "GEAPFD-KPKLGA-AGZIPA-WDTFMP-ARQ"
    CHAT_ID = -1001528320407
    DEFAULT_SERVICE = (
        "saavn"  # Must be one of "youtube"/"saavn"
    )

# don't make changes below this line
ARQ_API = "https://thearq.tech"
