# AutoPilotOps

This repository contains a minimal reference implementation of the
**Sentinel** remediation workflow.  A CloudWatch alarm triggers an
EventBridge rule which starts a Step Functions state machine. The state
machine orchestrates a series of Lambda-based agents:

1. **DiagnoserAgent** – inspects metrics and logs to determine the cause
   of the alarm.
2. **PlannerAgent** – maps the diagnosis to one or more remediation
   actions.
3. **ExecutorAgent** – invokes AWS APIs to perform the remediation.
4. **TesterAgent** – verifies that the remediation succeeded.
5. **ReflectorAgent** – performs a brief post-mortem and records the
   outcome.

The Step Functions definition is stored in
`state_machine/sentinel_state_machine.asl.json` and the AWS SAM template
`template.yaml` links the pieces together. The Lambda handlers are found
under the `agents/` directory.

These components are only stubs intended to illustrate the flow between
services. They can be deployed with the AWS SAM CLI:

```bash
sam build && sam deploy --guided
```
