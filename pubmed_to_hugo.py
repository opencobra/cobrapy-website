#!/usr/bin/env python3

from sys import argv
from jinja2 import Environment
import pandas as pd

MD = """+++
authors = [{{authors}}]
title = "{{title}}"
journal = "{{journal}}"
what = "article"
doi = "{{doi}}"
pubmed = "{{pmid}}"
date = "{{date}}"
keywords = [{{keywords}}]
+++

{{abstract}}"""

template = Environment().from_string(MD)


def write_entry(article):
    filename = "content/pubs/PM{}.md".format(article["pmid"])
    article["authors"] = ", ".join('"' + name.replace('"', "\\") + '"' for name in article["authors"])
    with open(filename, "w") as f:
        f.write(template.render(**article))


if __name__ == "__main__":
    articles = pd.read_csv(argv[1])
    articles.columns = [
        "pmid",
        "title",
        "authors",
        "citation",
        "first_author",
        "journal",
        "year",
        "date",
        "pmcid",
        "nihms_id",
        "doi",
    ]
    articles["date"] = articles["date"].str.replace("/", "-")
    articles["authors"] = articles["authors"].str.split(",\s*")
    articles["title"] = articles["title"].str.replace('"', '\\"').str.replace("\n", "")
    print(f"Found {articles.shape[0]} articles.")

    articles.apply(write_entry, axis=1)
