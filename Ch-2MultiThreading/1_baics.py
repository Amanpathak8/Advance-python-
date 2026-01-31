from concurrent.futures import ThreadPoolExecutor

def transformation(input):
    # extract values
    src = input['src']
    dest = input["dest"]
    
    print(f"Reading from {src}")
    print("transforming......")
    print(f"writing data to {dest}")
    
    # return result back to executor.map
    return f"{src} to {dest}"
    

array = [
    {"src": "table-1", "dest": "table-1"},
    {"src": "table-2", "dest": "table-2"},
    {"src": "table-3", "dest": "table-3"},
]

# ThreadPoolExecutor → runs functions in PARALLEL using multiple threads
# max_workers=3 → allow 3 tasks to run at same time when used in for loop we can use workder as lenth of list so we can have concurrency 
with ThreadPoolExecutor(max_workers=3) as executor:

    # executor.map runs transformation() on each item in array concurrently
    # It returns a generator of results (NOT printed yet)
    my_futures = executor.map(transformation, array)

# Convert results to list → this actually forces execution and collects return values
print(list(my_futures))
