import json
import os

from dotenv import load_dotenv
from steam.guard import SteamAuthenticator, MobileWebAuth

load_dotenv()

# Environment
ACCOUNT_NAME = os.getenv("STEAM_ACCOUNT_NAME")


def main():
    wa = MobileWebAuth(ACCOUNT_NAME)
    wa.cli_login()

    sa = SteamAuthenticator(backend=wa)
    sa.add()  # SMS code will be send to the account's phone number
    # sa.secrets  # dict with authenticator secrets (SAVE THEM!!)

    # save the secrets, for example to a file
    json.dump(sa.secrets, open("steam_secrets.json", "w"))

    print("Secrets:")
    print(sa.secrets)

    # HINT: You can stop here and add authenticator on your phone.
    #       The secrets will be the same, and you will be able to
    #       both use your phone and SteamAuthenticator.

    print("Enter sms code:")
    smscode = input()
    sa.finalize(smscode)  # activate the authenticator

    code = sa.get_code()  # generate 2FA code for login
    print("code: " + code)

    # sa.remove()  # removes the authenticator from the account


if __name__ == "__main__":
    main()
