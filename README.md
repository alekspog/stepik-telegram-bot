# Script to push reviews from the Stepik course to the Telegram channel

## Run script

Create .env file and your credentials to the file.
```bash
# Telegram bot
export API_ID="YOUR_VALUE"
export API_HASH="YOUR_VALUE"
export BOT_TOKEN="YOUR_VALUE"
export CHANNEL_ID="YOUR_VALUE"

# Stepik
export COURSE_ID="YOUR_VALUE"
export CLIENT_ID="YOUR_VALUE"
export CLIENT_SECRET="YOUR_VALUE"
```

Export your credentials as environment variables.
```bash
source .env
```

Run script:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python send_reviews.py
```
