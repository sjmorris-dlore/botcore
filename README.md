# botcore

Shared Python primitives used across `igbot`, `adsbot`, and `growthbot`.

## Included modules
- `botcore.aws.secrets`: Secrets Manager JSON helpers
- `botcore.aws.email`: SES text/html helpers
- `botcore.time.windows`: settled reporting week window helpers
- `botcore.metrics.maturity`: engagement maturity and projected score helpers

## Local dev
```powershell
pip install -e .\botcore
python -m unittest discover -s .\botcore\tests -p "test_*.py"
```

