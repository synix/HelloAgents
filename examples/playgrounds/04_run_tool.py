import os
import json
from dotenv import load_dotenv
from hello_agents.core.llm import HelloAgentsLLM
from hello_agents.tools.builtin.calculator import CalculatorTool
from hello_agents.tools.builtin.search_tool import SearchTool

# 成功运行的前置条件
# uv pip install ".[search]"

load_dotenv()

llm = HelloAgentsLLM(temperature=1)

tavily_key = os.getenv("TAVILY_API_KEY")
search_tool = SearchTool(backend="tavily", tavily_key=tavily_key)
search_result = search_tool.run({ "query": "曼城俱乐部最近一场英超比赛的比分", "return_mode": "json" })
print("👏 搜索结果:\n", json.dumps(search_result, indent=2, ensure_ascii=False))

calc_tool = CalculatorTool()
calc_result = calc_tool.run({ "input": "3*8+6" })
print("👏 计算结果:", calc_result)