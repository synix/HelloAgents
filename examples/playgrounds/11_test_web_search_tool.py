from dotenv import load_dotenv
from hello_agents.tools.builtin.search_tool import SearchTool, search
from hello_agents.tools.registry import ToolRegistry

load_dotenv()

def create_web_search_registry():
    registry = ToolRegistry()
    registry.register_function(
        name="web_search",
        description="高级搜索工具, 整个Tavily和SerpAPI多个搜索源, 提供更全面的搜索结果",
        func=search
    )

    return registry

def test_web_search():
    registry = create_web_search_registry()
    
    print("🔍 测试联网搜索工具")

    test_queries = [
        "Python编程语言的历史",
        "人工智能的最新进展",
        "2025年科技趋势"
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"测试 {i}: {query}")
        result = registry.execute_tool("web_search", query)
        print(f"结果: {result}\n")
        print("-" * 60 + "\n")

if __name__ == "__main__":
    test_web_search()
