from dotenv import load_dotenv
from hello_agents import HelloAgentsLLM, SimpleAgent

load_dotenv()

llm = HelloAgentsLLM(temperature=1)

agent = SimpleAgent(name="AI助手", system_prompt="你是一个有用的AI助手", llm=llm)

collectd_content: list[str] = []
for chunk in agent.stream_run("什么是人工智能?"):
    collectd_content.append(chunk)

print(f"✅ 流式调用结果:\n {"".join(collectd_content)}")