import os
from dotenv import load_dotenv
from hello_agents.tools.registry import ToolRegistry
from hello_agents.tools.builtin import SearchTool, CalculatorTool

load_dotenv()

tavily_key = os.getenv("TAVILY_API_KEY")
search_tool = SearchTool(backend="tavily", tavily_key=tavily_key)
calc_tool = CalculatorTool()

tool_registry = ToolRegistry()
tool_registry.register_tool(tool=search_tool)
tool_registry.register_tool(tool=calc_tool)


def web_search(query: str):
    return f"这是对于 \"{query}\" 的联网搜索结果"

tool_registry.register_function(name="custom_web_search", description="通过查询关键字, 借助Tavily进行联网搜索", func=web_search)

tools = tool_registry.list_tools()
print("🔨tools:\n", tools)

tool_descriptions = tool_registry.get_tools_description()
print("🚗 tool descriptions:\n", tool_descriptions)

search_output = tool_registry.execute_tool(name="search", input_text="曼城俱乐部最近一场英超比赛的比分")
print("👏 search output:\n", search_output)

calc_output = tool_registry.execute_tool(name="python_calculator", input_text="3*8+6")
print("👏 calc output:\n", calc_output)

custom_web_search_output = tool_registry.execute_tool(name="custom_web_search", input_text="曼城俱乐部")
print("👏 custom web search output:\n", custom_web_search_output)