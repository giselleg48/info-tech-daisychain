# Local Development
## Set up Google Cloud credentials
There are a [few ways to do this](https://googleapis.dev/python/google-api-core/latest/auth.html), but the most straightforward might be through the Google Cloud CLI:
```
sudo snap install google-cloud-cli --classic (or brew install --cask google-cloud-sdk)
```
then
```
gcloud auth application-default login
```
and follow the prompts provided.
## Set up python
Requirements: python3.10+, pipenv

1. If needed, install pipenv
```
pip3 install pipenv
```

2. Start pipenv shell to create virtual env and instal dependencies
```
pipenv shell
```
3. Run
```
python3 test.py

```
