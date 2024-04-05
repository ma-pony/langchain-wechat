from langchain.agents import Tool
from langchain_community.utilities.python import PythonREPL

python_repl = PythonREPL()

python_repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute python commands. Input should be a valid python command. If you want to see the output of a value, you should print it out with `print(...)`.",  # noqa: E501
    func=python_repl.run,
)
