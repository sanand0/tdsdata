# /// script
# requires-python = ">=3.13"
# dependencies = ["faker"]
# ///
import argparse
import os
import random
from pathlib import Path
from collections import defaultdict
from faker import Faker

random.seed(int(os.environ.get("RANDOM_SEED", 42)))
fake = Faker()
fake.seed_instance(int(os.environ.get("RANDOM_SEED", 42)))


def create_structure():
    files = ["index.html"]
    for depth in range(4):
        for _ in range(random.randint(10, 40)):
            parts = [fake.word().lower() for _ in range(random.randint(1, depth + 1))]
            files.append("/".join(parts) + ".html" if depth else f"{parts[0]}.html")
    return list(set(files))


def ensure_connectivity(files):
    graph = defaultdict(list)
    for file in files:
        if file != "index.html":
            source = random.choice([f for f in files if f != file])
            graph[source].append(file)
        graph[file].extend(
            random.sample(
                [f for f in files if f != file], min(random.randint(1, 3), len(files) - 1)
            )
        )
    return graph


def generate_html(filename, links):
    title = Path(filename).stem.replace("-", " ").title()
    nav = "".join(
        f'<a href="{os.path.relpath(f"html/{link}", f"html/{os.path.dirname(filename)}")}">'
        f"{Path(link).stem.replace('-', ' ').title()}</a><br>\n"
        for link in set(links)
    )
    return f"""<!DOCTYPE html>
<html><head><title>{title}</title></head>
<body><h1>{title}</h1><nav>{nav}</nav></body></html>"""


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--list", action="store_true")
    files = create_structure()
    
    if parser.parse_args().list:
        print(*sorted(files), sep='\n')
        return
    
    graph = ensure_connectivity(files)
    Path("html").mkdir(exist_ok=True)
    
    for file in files:
        path = Path(f"html/{file}")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(generate_html(file, graph[file]))
    
    print(f"Generated {len(files)} HTML files")

if __name__ == "__main__":
    main()
