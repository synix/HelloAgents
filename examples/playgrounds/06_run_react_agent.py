from dotenv import load_dotenv
from hello_agents import ReActAgent, ToolRegistry, search, calculate
from hello_agents.core.llm import HelloAgentsLLM

load_dotenv()

tool_registry = ToolRegistry()
tool_registry.register_function("search", "网页搜索工具", search)
tool_registry.register_function("calculate", "数学计算工具", calculate)

llm = HelloAgentsLLM()

react_agent = ReActAgent(
    name="研究助手",
    llm=llm,
    tool_registry=tool_registry,
    max_steps=5
)

result = react_agent.run("搜索最新的GPT-4发展情况, 并计算其参数量相比GPT-3的增长倍数")

print("🚀 result:\n", result)
print("📝 loops:\n", "\n\n".join(react_agent.current_history))