"""Secrets Manager JSON helpers."""

from __future__ import annotations

import json
from typing import Any

import boto3


def get_secret_json(
    secret_name: str,
    region: str = "us-east-1",
    client: Any | None = None,
) -> dict:
    """Fetch a JSON secret and return it as a dict."""
    sm = client or boto3.client("secretsmanager", region_name=region)
    resp = sm.get_secret_value(SecretId=secret_name)
    return json.loads(resp["SecretString"])


def put_secret_json(
    secret_name: str,
    payload: dict,
    region: str = "us-east-1",
    client: Any | None = None,
) -> None:
    """Write a full JSON payload to an existing secret."""
    sm = client or boto3.client("secretsmanager", region_name=region)
    sm.put_secret_value(SecretId=secret_name, SecretString=json.dumps(payload))


def upsert_secret_json(
    secret_name: str,
    payload: dict,
    description: str = "",
    region: str = "us-east-1",
    client: Any | None = None,
) -> str:
    """Create a secret if missing; otherwise update its current version."""
    sm = client or boto3.client("secretsmanager", region_name=region)
    try:
        sm.create_secret(
            Name=secret_name,
            Description=description,
            SecretString=json.dumps(payload),
        )
        return "created"
    except sm.exceptions.ResourceExistsException:
        sm.put_secret_value(SecretId=secret_name, SecretString=json.dumps(payload))
        return "updated"


def update_secret_key(
    secret_name: str,
    key: str,
    value: Any,
    region: str = "us-east-1",
    client: Any | None = None,
) -> dict:
    """Update one key inside a JSON secret and write it back."""
    secret = get_secret_json(secret_name=secret_name, region=region, client=client)
    secret[key] = value
    put_secret_json(secret_name=secret_name, payload=secret, region=region, client=client)
    return secret


# Backward-compatible alias matching existing naming in adsbot.
def load_secrets(secret_name: str, region: str = "us-east-1") -> dict:
    return get_secret_json(secret_name=secret_name, region=region)

