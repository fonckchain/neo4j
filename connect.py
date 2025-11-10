from neo4j import GraphDatabase

# Define the connection parameters
URI = "neo4j://127.0.0.1:7687"
AUTH = ("neo4j", "thisiseasy420$") 

try:
    # 1. Use the 'with' statement for automatic resource management (driver.close() is called automatically)
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        
        # 2. Verify connection (optional but good practice)
        driver.verify_connectivity()
        print("✅ Connection verified successfully.")

        # 3. Execute the query INSIDE the 'with' block
        records, summary, keys = driver.execute_query(
            "RETURN COUNT {()} AS count"
        )
        
        # 4. Process and print the result
        if records:
            count = records[0]["count"]
            print(f"Total count returned by query: {count}")
        else:
            print("No records returned.")

# Handle any potential connection or query errors
except Exception as e:
    print(f"❌ An error occurred: {e}")

# The driver is automatically closed here when the 'with' block ends.