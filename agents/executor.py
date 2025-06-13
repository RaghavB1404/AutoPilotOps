"""ExecutorAgent lambda function."""

from __future__ import annotations

import json


def handler(event: dict, context=None) -> dict:
    """Execute the remediation actions."""
    plan = event.get("plan", [])
    results = []
    for item in plan:
        results.append({"action": item.get("action"), "status": "success"})
    result = {"results": results}
    print(json.dumps(result))
    return result
