from dotenv import load_dotenv
from hello_agents.agents.simple_agent import SimpleAgent
from hello_agents.core.llm import HelloAgentsLLM

load_dotenv()

def test_agent_without_memory():
    llm = HelloAgentsLLM()
    agent = SimpleAgent(name="学习助手", llm=llm)
    response1 = agent.run(input_text="我叫张三, 正在学习Python, 目前掌握了基础语法")
    print(response1)

    # SimpleAgent实现了记忆(memory), 所以这里强制将记忆删除, 以测试在没有记忆情况下agent的表现
    agent.clear_history()

    response2 = agent.run("你还记得我的学习进度吗?")
    print(response2)

if __name__ == "__main__":
    test_agent_without_memory()