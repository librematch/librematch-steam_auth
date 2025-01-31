# ⚔️ Libre:Match Steam-Auth Proxy

## Usage

Rename the `.env.sample` to `.env` and set your Steam account credentials.
For security reasons, it's strongly recommended to:

1. Create a separate Steam account dedicated to API access
2. Gift the required game to this account
3. Use a strong password
4. Set the password in an environment variable rather than in `.env` to avoid accidental commits

Now follow the instructions under development.

## Development

### Install uv

Follow the installation instructions of the [official repository](https://github.com/astral-sh/uv/?tab=readme-ov-file#installation)

### Install dependencies

Run `uv sync` to install all dependencies within a virtual environment for this project.

### Setup

Create `api_keys.json` with a list of api keys for authentication against the proxy. For development you can use:

`api_keys.json`

```json
{
  "dev1": "DEV1_API_KEY",
  "dev2": "DEV2_API_KEY"
}
```

> ⚠️ **Note**: Two-factor authentication (2FA) is currently not supported.
> The project uses basic username/password authentication.
> The `enable-2fa.py` script and related 2FA functionality are deprecated.

### Start

To start the proxy server run `uv run psp`.

Then you can make calls to the proxy e.g. for endpoint `/game/news/getNews` call:

<http://127.0.0.1:5000/relic/game/news/getNews>

You need to supply a header with the api key e.g. `api_key=DEV_API_KEY`

All query params or post data that you add to the request will be forwarded to the relic api.

`Insomnia_LibreMatchExamples.json` contains an Insomnia collection with some example requests. You can set your
api_key and the base url for accessing the proxy in the Insomnia environment.

## License

"AGPL-3.0-or-later", see [License](./LICENSE.md)
