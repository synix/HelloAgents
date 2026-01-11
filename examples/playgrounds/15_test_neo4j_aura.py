import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

URI = os.getenv('NEO4J_URI')
USERNAME = os.getenv('NEO4J_USERNAME')
PASSWORD = os.getenv('NEO4J_PASSWORD')
AUTH = (USERNAME, PASSWORD)
DATABASE_NAME = os.getenv('NEO4J_DATABASE')


def verify_neo4j_connectivity():
    with GraphDatabase.driver(uri=URI, auth=AUTH) as driver:
        driver.verify_connectivity()


def create_example_graph(driver: GraphDatabase):
    summary = driver.execute_query("""
        CREATE (a:Person {name: $name})
        CREATE (b:Person {name: $friendName})
        CREATE (a)-[:KNOWS]->(b)
        """,
        name="Alice", friendName="David", database_=DATABASE_NAME
    ).summary

    print("Created {nodes_created} nodes in {time} ms.".format(nodes_created=summary.counters.nodes_created, time=summary.result_available_after))


def query_graph(driver: GraphDatabase):
    records, summary, keys = driver.execute_query("""
        MATCH (p:Person)-[:KNOWS]->(:Person)
        RETURN p.name AS name
    """, database_=DATABASE_NAME)

    for record in records:
        print(record.data())

    print("The query `{query}` returned {records_count} records in {time} ms.".format(
        query=summary.query, records_count=len(records), time=summary.result_available_after
    ))


if __name__ == "__main__":
    verify_neo4j_connectivity()
    driver = GraphDatabase.driver(uri=URI, auth=AUTH)
    # create_example_graph()
    query_graph(driver)
    driver.close()
