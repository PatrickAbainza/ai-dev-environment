from langgraph.graph import StateGraph, END
from langgraph.pregel import Pregel
from langchain_core.runnables import RunnableLambda

def hello_world(input_):
    return "Hello, World!"

workflow = StateGraph(str)
workflow.add_node("hello_world", RunnableLambda(hello_world))
workflow.set_entry_point("hello_world")
workflow.add_edge("hello_world", END)

graph = workflow.compile()

for output in graph.stream("test"):
    print(output)