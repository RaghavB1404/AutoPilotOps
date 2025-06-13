"""DiagnoserAgent lambda function."""

from __future__ import annotations

import json
import pathlib
from typing import Any, Dict


# Fake metrics fetcher for local demo
_DEF_METRICS = [{"Timestamp": "2025-06-13T00:00:00Z", "Average": 92.5}]


def _load_prompt() -> str:
    prompt_path = pathlib.Path("prompts/diagnosis_prompt.txt")
    return prompt_path.read_text()


def _call_llm(prompt: str) -> Dict[str, Any]:
    """Simulate an LLM call with a deterministic response."""
    # In a real implementation this would invoke an API like OpenAI or Groq.
    return {
        "cause": "Application load test running",
        "confidence": 0.85,
        "next_steps": "restart_instance"
    }


def handler(event: Dict[str, Any], context: Any = None) -> Dict[str, Any]:
    """Diagnose the cause of the alarm."""
    instance_id = event.get("instance_id", "unknown")
    metrics = _DEF_METRICS
    prompt = _load_prompt()
    llm_input = f"{prompt}\n{json.dumps(metrics)}"
    diagnosis = _call_llm(llm_input)
    diagnosis["instance_id"] = instance_id


def handler(event: dict, context=None) -> dict:
    """Diagnose the cause of the alarm.

    This placeholder implementation simply returns a fixed diagnosis.
    """
    diagnosis = {"reason": "High CPU utilization detected"}

    print(json.dumps(diagnosis))
    return diagnosis
