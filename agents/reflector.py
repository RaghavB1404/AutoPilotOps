"""ReflectorAgent lambda function."""

from __future__ import annotations

import json
from typing import Any, Dict


def _post_mortem(passed: bool) -> str:
    if passed:
        return "Remediation succeeded. Consider monitoring thresholds."
    return "Remediation failed. Additional investigation required."


def handler(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """Summarize the outcome of the remediation."""
    test_passed = event.get("test_passed", False)
    summary = _post_mortem(test_passed)
    result = {"summary": summary, "instance_id": event.get("instance_id")}



def handler(event: dict, context=None) -> dict:
    """Summarize the outcome of the remediation."""
    test_passed = event.get("test_passed", False)
    summary = "Remediation succeeded" if test_passed else "Remediation failed"
    result = {"summary": summary}
    print(json.dumps(result))
    return result
