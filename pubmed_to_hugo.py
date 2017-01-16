#!/usr/bin/env python3

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

if __name__ == "__main__":
    import xml.etree.ElementTree as ET
    from sys import argv
    from jinja2 import Environment
    from os.path import exists
    from datetime import date as da

    template = Environment().from_string(MD)

    root = ET.parse(argv[1]).getroot()
    for child in root:
        article = {}
        article["pmid"] = child.find(".//PMID").text
        article["title"] = child.find(".//ArticleTitle").text
        if child.find(".//AbstractText") is not None:
            article["abstract"] = child.find(".//AbstractText").text
        else:
            article["abstract"] = ""
        article["authors"] = ", ".join([
            '"' + x.find("ForeName").text + " " + x.find("LastName").text + '"'
            for x in child.findall(".//Author")
            ])
        article["keywords"] = ", ".join([
            '"' + x.text + '"' for x in child.findall(".//Keyword")
            ])
        article["doi"] = child.find(
            ".//ArticleId[@IdType='doi']").text
        article["journal"] = child.find(".//Journal/Title").text
        date = child.find(".//PubMedPubDate[@PubStatus='pubmed']")
        article["date"] = da(int(date.find("Year").text),
                             int(date.find("Month").text),
                             int(date.find("Day").text)).isoformat()
        print(article["keywords"])
        filename = "content/pubs/PM{}.md".format(article["pmid"])
        if not exists(filename):
            with open(filename, "w") as f:
                f.write(template.render(**article))
