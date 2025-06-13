"""DiagnoserAgent lambda function."""

from __future__ import annotations

import json


def handler(event: dict, context=None) -> dict:
    """Diagnose the cause of the alarm.

    This placeholder implementation simply returns a fixed diagnosis.
    """
    diagnosis = {"reason": "High CPU utilization detected"}
    print(json.dumps(diagnosis))
    return diagnosis
