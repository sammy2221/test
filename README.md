# Discord Rich Presence Custom (Open Source)

A lightweight open-source Python script for setting custom Discord Rich Presence.

## Features

- Set `details` and `state`
- Optional large/small image assets
- Up to 2 optional buttons
- Keeps presence alive until stopped

## Requirements

- Python 3.10+
- Discord desktop app running
- A Discord application (for Client ID and assets)

## Install

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
python rich_presence.py \
  --client-id 123456789012345678 \
  --details "Building open source" \
  --state "Custom Rich Presence" \
  --large-image logo \
  --large-text "My Project" \
  --button1-label "GitHub" \
  --button1-url "https://github.com/yourname/yourrepo"
```

## Notes

- Create assets inside your Discord Developer Portal application settings.
- Use asset keys (not filenames) for image parameters.
- If Discord is not open, connection fails.

## License

MIT
