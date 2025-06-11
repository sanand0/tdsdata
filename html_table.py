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


def generate_table(table_num, rows=100, cols=10):
    rows = "".join(
        f"<tr>{''.join(f'<td>{fake.word()}</td>' for _ in range(cols))}</tr>" for _ in range(rows)
    )
    headers = "".join(f"<th>Col {i + 1}</th>" for i in range(cols))
    return f"<h1>Table {table_num}</h1><table><tr>{headers}</tr>{rows}</table>"


html = f"""<!DOCTYPE html><html><head><title>Tables</title></head><body>
{generate_table(1, rows=100, cols=10)}
</body></html>"""

Path("html_table").mkdir(exist_ok=True)
Path("html_table/index.html").write_text(html)
print("Generated html_table/index.html with 3 tables")
