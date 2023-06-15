# poc_steam_proxy

## Usage

### Setup

Create `api_keys.json` with a list of api keys for authentication against the proxy. For development you can use:

`api_keys.json`

```
{
  "dev1": "DEV1_API_KEY",
  "dev2": "DEV2_API_KEY"
}
```

Then ask team members for the steam 2FA secrets file `steam_secrets.json` and put it into project root.

Finally run `poetry install`.

### Start

To start the proxy server run `poetry run psp`.

Then you can make calls to the proxy e.g. for endpoint `/game/news/getNews` call:

<http://127.0.0.1:5000/relic/game/news/getNews>

You need to supply a header with the api key e.g. `api_key=DEV_API_KEY`

All query params or post data that you add to the request will be forwarded to the relic api.

`Insomnia_LibreMatchExamples.json` contains an Insomnia collection with some example requests. You can set your
api_key and the base url for accessing the proxy in the Insomnia environment.
