"""ExecutorAgent lambda function."""

from __future__ import annotations

import json
from typing import Any, Dict, List


def _execute(action: str, instance_id: str) -> Dict[str, str]:
    """Simulate executing an action."""
    # Real implementation would call AWS APIs here
    return {"action": action, "status": f"executed on {instance_id}"}


def handler(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """Execute the remediation actions."""
    plan: List[Dict[str, Any]] = event.get("plan", [])
    instance_id = event.get("instance_id", "unknown")
    results = [_execute(item.get("action", ""), instance_id) for item in plan]
    result = {"results": results, "instance_id": instance_id}
    print(json.dumps(result))
    return result
