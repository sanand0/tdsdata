# /// script
# requires-python = ">=3.13"
# dependencies = ["faker", "networkx"]
# ///
from collections import defaultdict
from faker import Faker
from networkx.generators.community import connected_caveman_graph
from pathlib import Path
from random import randint, seed
import argparse
import json
import networkx as nx
import os

seed_value = int(os.environ.get("TDS_RANDOM_SEED", 42))
seed(seed_value)
fake = Faker()
fake.seed_instance(seed_value)


def create_structure():
    files = ["index.html"]
    for depth in range(4):
        for _ in range(randint(10, 40)):
            parts = [fake.word().lower() for _ in range(randint(1, depth + 1))]
            files.append("/".join(parts) + ".html" if depth else f"{parts[0]}.html")
    return list(sorted(set(files)))


def ensure_connectivity(strings, k=5):
    G = connected_caveman_graph((len(strings) + k - 1) // k, k)  # O(nk) edges, always connected
    G = nx.relabel_nodes(G, dict(zip(G.nodes, strings)))

    # Replace extra nodes with the first node
    def replace(v):
        return strings[0] if isinstance(v, int) else v

    return {replace(u): [replace(v) for v in G.neighbors(u)] for u in G}


def generate_html(filename, links):
    title = Path(filename).stem.replace("-", " ").title()
    nav = "".join(
        f'<a href="{os.path.relpath(f"crawl_html/{link}", f"crawl_html/{os.path.dirname(filename)}")}">'
        f"{Path(link).stem.replace('-', ' ').title()}</a><br>\n"
        for link in sorted(set(links))
    )
    return f"""<!DOCTYPE html>
<html><head><title>{title}</title></head>
<body><h1>{title}</h1><nav>{nav}</nav></body></html>"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    files = create_structure()

    if parser.parse_args().list:
        print(*sorted(files), sep="\n")
        counts = defaultdict(int)
        for file in files:
            filename = Path(file).stem
            if filename and filename[0].isalpha():
                counts[filename[0].lower()] += 1
        print(json.dumps(dict(counts)))
        return

    graph = ensure_connectivity(files)
    Path("crawl_html").mkdir(exist_ok=True)

    for file in files:
        path = Path(f"crawl_html/{file}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(generate_html(file, graph[file]))

    print(f"Generated {len(files)} HTML files")


if __name__ == "__main__":
    main()
