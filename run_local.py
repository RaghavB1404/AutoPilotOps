from agents.diagnoser import handler as diagnoser
from agents.planner import handler as planner
from agents.executor import handler as executor
from agents.tester import handler as tester
from agents.reflector import handler as reflector

state = {}
state.update(diagnoser(state))
state.update(planner(state))
state.update(executor(state))
state.update(tester(state))
state.update(reflector(state))
print(state)
