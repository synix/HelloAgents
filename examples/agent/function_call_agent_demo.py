"""最简 FunctionCallAgent 示例"""

from dotenv import load_dotenv
from hello_agents.agents import FunctionCallAgent
from hello_agents.core.llm import HelloAgentsLLM
from hello_agents.tools.registry import ToolRegistry


def get_horoscope(sign: str) -> str:
    sample_data = {
        "白羊座": "保持耐心，合作能带来额外好运。",
        "金牛座": "适合整理计划，财务上保持谨慎。",
        "双子座": "沟通顺畅，适合推进新想法。",
        "巨蟹座": "关注家人需求，情绪管理很重要。",
    }
    return sample_data.get(sign.strip(), "今天以平静面对生活，一切都会慢慢变好。")


def main() -> None:
    load_dotenv()

    # 需提前配置 OPENAI_API_KEY，或在 HelloAgentsLLM 中传入 api_key/base_url
    llm = HelloAgentsLLM(model="gpt-4o-mini")

    registry = ToolRegistry()
    registry.register_function(
        name="get_horoscope",
        description="获取某个星座的今日运势。",
        func=get_horoscope,
    )

    agent = FunctionCallAgent(
        name="demo-agent",
        llm=llm,
        tool_registry=registry,
    )

    question = "请告诉我金牛座今天的运势，并说明是如何得到信息的。"
    answer = agent.run(question)
    print("Agent:", answer)


if __name__ == "__main__":
    main()
