from dotenv import load_dotenv
from hello_agents import ReflectionAgent
from hello_agents.core.llm import HelloAgentsLLM

load_dotenv()

llm = HelloAgentsLLM()

reflection_agent = ReflectionAgent(
    name="代码专家",
    llm=llm,
    max_iterations=3
)

code = reflection_agent.run("编写一个高效的素数筛选算法，要求时间复杂度尽可能低")
print(f"🚀 最终代码:\n{code}")

print(f"📝 MEMORY:\n{reflection_agent.memory.get_trajectory()}")