# ⚔️ Libre:Match Steam-Auth Proxy

## Usage

Rename the `.env.sample` to `.env` and set your Steam account to log into.
Set your password in an environment variable as well, please don't use `.env` for it
as it might happen that you push this password to this repository.

Now follow the instructions under development.

## Development

### Install poetry

Follow the installation instructions on the [official website](https://python-poetry.org/docs/#installation)

### Install dependencies

Run `poetry install` to install all dependencies within a virtual environment for this project.

### Setup

Create `api_keys.json` with a list of api keys for authentication against the proxy. For development you can use:

`api_keys.json`

```json
{
  "dev1": "DEV1_API_KEY",
  "dev2": "DEV2_API_KEY"
}
```

If you are a member of LibreMatch team, ask members for the steam 2FA secrets file `steam_secrets.json` and put it into project root.

Otherwise use the `enable-2fa.py` script to generate your own `steam_secrets.json` file.

Finally run `poetry install`.

### Start

To start the proxy server run `poetry run psp`.

Then you can make calls to the proxy e.g. for endpoint `/game/news/getNews` call:

<http://127.0.0.1:5000/relic/game/news/getNews>

You need to supply a header with the api key e.g. `api_key=DEV_API_KEY`

All query params or post data that you add to the request will be forwarded to the relic api.

`Insomnia_LibreMatchExamples.json` contains an Insomnia collection with some example requests. You can set your
api_key and the base url for accessing the proxy in the Insomnia environment.

## License

"AGPL-3.0-or-later", see [License](./LICENSE.md)
