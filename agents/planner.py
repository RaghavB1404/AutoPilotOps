"""PlannerAgent lambda function."""

from __future__ import annotations

import json


def handler(event: dict, context=None) -> dict:
    """Generate a remediation plan based on the diagnosis."""
    diagnosis = event.get("reason", "")
    plan = []
    if "High CPU" in diagnosis:
        plan.append({"action": "RestartInstance"})
    result = {"plan": plan}
    print(json.dumps(result))
    return result
