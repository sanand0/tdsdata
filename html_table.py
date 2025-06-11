# /// script
# requires-python = ">=3.13"
# dependencies = ["faker"]
# ///
from faker import Faker
from pathlib import Path
import os

seed_value = int(os.environ.get("TDS_RANDOM_SEED", 42))
fake = Faker()
fake.seed_instance(seed_value)


def generate_table(table_num):
    rows = "".join(
        f"<tr>{''.join(f'<td>{fake.word()}</td>' for _ in range(10))}</tr>" for _ in range(50)
    )
    headers = "".join(f"<th>Col {i + 1}</th>" for i in range(10))
    return f"<h1>Table {table_num}</h1><table><tr>{headers}</tr>{rows}</table>"


html = f"""<!DOCTYPE html><html><head><title>Tables</title></head><body>
{''.join(generate_table(i) for i in range(1, 31))}
</body></html>"""

Path("html_table").mkdir(exist_ok=True)
Path("html_table/index.html").write_text(html)
print("Generated html_table/index.html with 30 tables")
