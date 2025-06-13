"""TesterAgent lambda function."""

from __future__ import annotations

import json


def handler(event: dict, context=None) -> dict:
    """Verify that the remediation actions had the desired effect."""
    results = event.get("results", [])
    success = all(item.get("status") == "success" for item in results)
    result = {"test_passed": success}
    print(json.dumps(result))
    return result
