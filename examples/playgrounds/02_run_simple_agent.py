import os
from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM, SimpleAgent
from hello_agents.tools.builtin.search_tool import SearchTool

load_dotenv()

llm = HelloAgentsLLM(temperature=1)

agent = SimpleAgent(name="AI助手", system_prompt="你是一个有用的AI助手", llm=llm)

serpapi_key = os.getenv("SERPAPI_API_KEY")
search_tool = SearchTool(backend="serpapi", serpapi_key=serpapi_key)

agent.add_tool(search_tool)

response = agent.run("请联网搜索, 曼城最近一场英超比赛的比分")
print(response)