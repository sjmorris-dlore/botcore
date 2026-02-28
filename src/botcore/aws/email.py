"""SES email helpers."""

from __future__ import annotations

from typing import Any

import boto3


def send_ses_text(
    sender: str,
    recipient: str,
    subject: str,
    body: str,
    region: str = "us-east-1",
    client: Any | None = None,
) -> None:
    ses = client or boto3.client("ses", region_name=region)
    ses.send_email(
        Source=sender,
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {"Text": {"Data": body, "Charset": "UTF-8"}},
        },
    )


def send_ses_html(
    sender: str,
    recipient: str,
    subject: str,
    html_body: str,
    region: str = "us-east-1",
    client: Any | None = None,
) -> None:
    ses = client or boto3.client("ses", region_name=region)
    ses.send_email(
        Source=sender,
        Destination={"ToAddresses": [recipient]},
        Message={
            "Subject": {"Data": subject, "Charset": "UTF-8"},
            "Body": {"Html": {"Data": html_body, "Charset": "UTF-8"}},
        },
    )

