# TDS Datasets

Utilities to create datasets for the [Tools in Data Science](https://tds.s-anand.net/) course.

## HTML files for crawling

`make_html.py` generates a connected web of HTML files with random paths and cross-links for testing crawlers, web scrapers, and link analysis tools. It creates a hierarchical structure of HTML files (0-3 levels deep) with:

- Random English words for file and directory names. It uses the environment variable `RANDOM_SEED` for reproducible generation.
- Generates multiple files at each level
- Cross-references ensuring every file is reachable from `index.html` and creates links between files

How it works:

1. **Structure Generation**: Creates file paths using Faker (random English words), building a tree structure with varying depths
2. **Connectivity**: Ensures graph connectivity by giving every file at least one incoming link, plus random cross-links (1-3 per file)
3. **HTML Generation**: Creates minimal HTML files with titles and navigation links using relative paths

Usage:

```bash
# Generate HTML files in html/ directory
python make_html.py

# List file paths without creating files
python make_html.py --list

# Use custom random seed
RANDOM_SEED=123 python make_html.py
```

# License

[MIT](LICENSE)
