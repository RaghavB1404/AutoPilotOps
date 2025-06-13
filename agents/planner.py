"""PlannerAgent lambda function."""

from __future__ import annotations

import json
from typing import Any, Dict, List


def _parse_steps(steps: str) -> List[Dict[str, Any]]:
    plan = []
    for step in steps.split(','):
        action = step.strip()
        if not action:
            continue
        plan.append({"action": action})
    return plan


def handler(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """Generate a remediation plan based on the diagnosis."""
    steps = event.get("next_steps", "")
    plan = _parse_steps(steps)
    result = {"plan": plan, "instance_id": event.get("instance_id")}
    print(json.dumps(result))
    return result
