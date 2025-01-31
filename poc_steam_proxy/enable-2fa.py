# SPDX-License-Identifier: AGPL-3.0-or-later

"""
DEPRECATED: This script is no longer functional as Steam Guard and 2FA authentication
are not working with the current steam library version. Please use basic username/password
authentication instead.

For security, it's recommended to:
1. Create a separate Steam account dedicated to API access
2. Gift the required game to this account
3. Use a strong password
4. Store credentials securely
"""

import json
import os
import sys
import warnings
from dotenv import load_dotenv
from steam.guard import SteamAuthenticator, MobileWebAuth

# Emit deprecation warning
warnings.warn(
    "This script is deprecated as Steam Guard and 2FA authentication are no longer "
    "supported. Please use basic username/password authentication instead.",
    DeprecationWarning,
    stacklevel=2,
)

load_dotenv()

# Environment
ACCOUNT_NAME = os.getenv("STEAM_ACCOUNT_NAME")


def main():
    print("WARNING: This script is deprecated and will not work as expected.")
    print("Please use basic username/password authentication instead.\n")

    # wait for user input
    input("Press Enter to continue...")
    sys.exit(0)

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
