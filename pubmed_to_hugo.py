#!/usr/bin/env python3

from sys import argv
from jinja2 import Environment
from os.path import exists
from datetime import date as da
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


def write_entry(article):
    filename = "content/pubs/PM{}.md".format(article["pmid"])
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

    articles.apply(write_entry, axis=1)
