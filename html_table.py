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


Path("html_table").mkdir(exist_ok=True)

for i in range(1, 51):
    html = f"""<!DOCTYPE html><html><head><title>Table {i}</title></head><body>
{generate_table(i, rows=100, cols=10)}
</body></html>"""
    Path(f"html_table/{i}.html").write_text(html)

print("Generated html_table/*.html")
