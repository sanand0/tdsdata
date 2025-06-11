# TDS Datasets

Utilities to create datasets for the [Tools in Data Science](https://tds.s-anand.net/) course.

## Crawl HTML

`crawl_html.py` generates a connected web of HTML files with random paths and cross-links for testing crawlers, web scrapers, and link analysis tools. It creates a hierarchical structure of HTML files (0-3 levels deep) with:

- Random English words for file and directory names. It uses the environment variable `RANDOM_SEED` for reproducible generation.
- Generates multiple files at each level
- Cross-references ensuring every file is reachable from `index.html` and creates links between files

How it works:

1. **Structure Generation**: Creates file paths using Faker (random English words), building a tree structure with varying depths
2. **Connectivity**: Ensures graph connectivity by giving every file at least one incoming link, plus random cross-links (1-3 per file)
3. **HTML Generation**: Creates minimal HTML files with titles and navigation links using relative paths

Usage:

```bash
# Generate HTML files in crawl_html/ directory
TDS_RANDOM_SEED=... python crawl_html.py

# List file paths without creating files
TDS_RANDOM_SEED=... python crawl_html.py --list
```

## HTML Table

`html_table.py` generates an HTML file with 30 tables containing random data for testing table parsing, scraping, and data extraction tools. Each table has:

- A numbered title (Table 1, Table 2, etc.)
- 50 rows and 10 columns (Col 1 through Col 10)
- Random English words in each cell using Faker
- Uses the environment variable `TDS_RANDOM_SEED` for reproducible generation

Usage:

```bash
# Generate HTML table file in html_table/ directory
TDS_RANDOM_SEED=... python html_table.py
```

# License

[MIT](LICENSE)
