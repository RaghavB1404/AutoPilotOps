"""SentinelAgent lambda function."""

from __future__ import annotations

import json
from typing import Any, Dict


def handler(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """Parse an alarm event and start the Sentinel workflow.

    In a real deployment this would call Step Functions. Here we just return
    the extracted instance ID so the local demo can proceed.
    """
    detail = event.get("detail", {})
    metrics = (
        detail.get("configuration", {})
        .get("metrics", [{}])
    )
    instance_id = (
        metrics[0]
        .get("metricStat", {})
        .get("metric", {})
        .get("dimensions", {})
        .get("InstanceId", "unknown")
    )
    print(json.dumps({"starting_execution_for": instance_id}))
    # Here we would call Step Functions' StartExecution API
    return {"instance_id": instance_id}
