import os

def save_graph(bbytes: bytes):
    os.makedirs("output", exist_ok=True)
    with open("output/graph.png", "wb") as f:
        f.write(bbytes)


