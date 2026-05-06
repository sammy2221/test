#!/usr/bin/env python3
"""Open-source custom Discord Rich Presence client.

Usage:
  python rich_presence.py --client-id YOUR_APP_ID --details "Coding" --state "In project"
"""

from __future__ import annotations

import argparse
import time
from datetime import datetime

from pypresence import Presence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Set a custom Discord Rich Presence status."
    )
    parser.add_argument("--client-id", required=True, help="Discord application client ID")
    parser.add_argument("--details", default="Working on something cool", help="Main activity line")
    parser.add_argument("--state", default="Open source mode", help="Secondary activity line")
    parser.add_argument("--large-image", default=None, help="Large image asset key")
    parser.add_argument("--large-text", default=None, help="Large image tooltip")
    parser.add_argument("--small-image", default=None, help="Small image asset key")
    parser.add_argument("--small-text", default=None, help="Small image tooltip")
    parser.add_argument("--button1-label", default=None, help="Button #1 label")
    parser.add_argument("--button1-url", default=None, help="Button #1 URL")
    parser.add_argument("--button2-label", default=None, help="Button #2 label")
    parser.add_argument("--button2-url", default=None, help="Button #2 URL")
    parser.add_argument(
        "--duration",
        type=int,
        default=0,
        help="How long to keep running (seconds). 0 means forever.",
    )
    return parser.parse_args()


def build_buttons(args: argparse.Namespace) -> list[dict[str, str]]:
    buttons: list[dict[str, str]] = []
    if args.button1_label and args.button1_url:
        buttons.append({"label": args.button1_label, "url": args.button1_url})
    if args.button2_label and args.button2_url:
        buttons.append({"label": args.button2_label, "url": args.button2_url})
    return buttons


def main() -> None:
    args = parse_args()

    rpc = Presence(args.client_id)
    rpc.connect()

    start_time = int(datetime.now().timestamp())
    buttons = build_buttons(args)

    payload = {
        "details": args.details,
        "state": args.state,
        "start": start_time,
        "large_image": args.large_image,
        "large_text": args.large_text,
        "small_image": args.small_image,
        "small_text": args.small_text,
    }

    if buttons:
        payload["buttons"] = buttons

    payload = {k: v for k, v in payload.items() if v is not None}

    rpc.update(**payload)
    print("Rich Presence set. Press Ctrl+C to stop.")

    end_time = time.time() + args.duration if args.duration > 0 else None

    try:
        while True:
            if end_time and time.time() > end_time:
                break
            time.sleep(15)
            rpc.update(**payload)
    except KeyboardInterrupt:
        pass
    finally:
        rpc.clear()
        rpc.close()
        print("Rich Presence cleared.")


if __name__ == "__main__":
    main()
