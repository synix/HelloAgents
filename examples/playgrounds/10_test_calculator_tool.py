from dotenv import load_dotenv
from hello_agents.core.llm import HelloAgentsLLM
from hello_agents.tools.builtin.calculator import calculate
from hello_agents.tools.registry import ToolRegistry

load_dotenv()

def create_calculator_registry():
    registry = ToolRegistry()
    registry.register_function(
        name="my_calculator",
        description="简单的数学计算工具, 支持基本运算(+,-,*,/)和sqrt函数",
        func=calculate
    )

    return registry

def test_calculator_tool():
    """测试calculator tool"""
    registry = create_calculator_registry()

    print("✏️ 测试计算器工具\n")

    test_cases = [
        "2 + 3",
        "10 - 4",
        "5 * 6",
        "15 / 3",
        "sqrt(16)",
    ]

    for i, expression in enumerate(test_cases, 1):
        print(f"测试 {i}: {expression}")
        result = registry.execute_tool(name="my_calculator", input_text=expression)
        print(f"结果: {result}\n")

def test_calculator_tool_with_llm():
    """模拟tool与SimpleAgent的集成"""
    llm = HelloAgentsLLM()
    registry = create_calculator_registry()

    print("🤖 与SimpleAgent集成测试:")

    user_question = "请帮我计算 sqrt(16) + 2 * 3"

    print(f"用户问题 {user_question}")

    calc_result = registry.execute_tool(name="my_calculator", input_text="sqrt(16) + 2 * 3")
    print(f"计算结果: {calc_result}")

    final_messages = [
        { "role": "user", "content": f"计算结果是 {calc_result}, 请用自然语言回答用户的问题: {user_question}" }
    ]

    print("\n 🎯 SimpleAgent的回答:")
    response = llm.think(final_messages)
    for chunk in response:
        pass

if __name__ == "__main__":
    test_calculator_tool()
    test_calculator_tool_with_llm()