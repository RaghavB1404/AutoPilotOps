"""ReflectorAgent lambda function."""

from __future__ import annotations

import json


def handler(event: dict, context=None) -> dict:
    """Summarize the outcome of the remediation."""
    test_passed = event.get("test_passed", False)
    summary = "Remediation succeeded" if test_passed else "Remediation failed"
    result = {"summary": summary}
    print(json.dumps(result))
    return result
