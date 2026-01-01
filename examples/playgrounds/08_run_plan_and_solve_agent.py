from dotenv import load_dotenv
from hello_agents import PlanAndSolveAgent
from hello_agents.core.llm import HelloAgentsLLM

load_dotenv()

llm = HelloAgentsLLM()

plan_agent = PlanAndSolveAgent(name="问题解决专家", llm=llm)

problem = """
一家公司第一年营收100万，第二年增长20%，第三年增长15%。
如果每年的成本是营收的70%，请计算三年的总利润。
"""

answer = plan_agent.run(problem)