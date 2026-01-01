import os
from dotenv import load_dotenv
from hello_agents.core.llm import HelloAgentsLLM
from hello_agents.core.message import Message

# 运行: uv run examples/playgrounds/01_run_azure_provider.py
# 成功运行的前置条件
# uv pip install ".[evaluation]"

load_dotenv()

print('🔧 环境变量检查:')
print(f'LLM_MODEL_ID: {os.getenv("LLM_MODEL_ID", "未设置")}')
print(f'LLM_API_KEY: { "已设置" if os.getenv("LLM_API_KEY") else "未设置"}')
print(f'LLM_BASE_URL: {os.getenv("LLM_BASE_URL", "未设置")}')

llm = HelloAgentsLLM(max_tokens=8000, temperature=1)

message = Message(content="介绍一下巴塞罗那俱乐部", role="user").to_dict()
response = llm.invoke(messages=[message])

print(f"🚀 大语言模型 {os.getenv("LLM_MODEL_ID")} 的调用结果:\n{response}")

