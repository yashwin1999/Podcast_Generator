import yaml
import xml.etree.ElementTree as xml_tree

# Load YAML data
with open("feed.yaml", "r") as file:
    yaml_data = yaml.safe_load(file)

# Create RSS root
rss = xml_tree.Element(
    "rss",
    {
        "version": "2.0",
        "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd"
    }
)

# Create channel
channel = xml_tree.SubElement(rss, "channel")

# Channel info
title = xml_tree.SubElement(channel, "title")
title.text = yaml_data["title"]

description = xml_tree.SubElement(channel, "description")
description.text = yaml_data["description"]

language = xml_tree.SubElement(channel, "language")
language.text = yaml_data["language"]

subtitle = xml_tree.SubElement(channel, "itunes:subtitle")
subtitle.text = yaml_data["subtitle"]

author = xml_tree.SubElement(channel, "itunes:author")
author.text = yaml_data["author"]

category = xml_tree.SubElement(channel, "itunes:category")
category.set("text", yaml_data["category"])

# Podcast image
image = xml_tree.SubElement(channel, "itunes:image")
image.set("href", yaml_data["image"])

# Process podcast episodes
for episode in yaml_data["item"]:

    item = xml_tree.SubElement(channel, "item")

    item_title = xml_tree.SubElement(item, "title")
    item_title.text = episode["title"]

    item_description = xml_tree.SubElement(item, "description")
    item_description.text = episode["description"]

    pub_date = xml_tree.SubElement(item, "pubDate")
    pub_date.text = episode["published"]

    duration = xml_tree.SubElement(item, "itunes:duration")
    duration.text = str(episode["duration"])

    enclosure = xml_tree.SubElement(
        item,
        "enclosure",
        {
            "url": episode["file"],
            "type": yaml_data["format"],
            "length": str(episode["length"]).replace(",", "")
        }
    )

# Write XML output
tree = xml_tree.ElementTree(rss)

tree.write(
    "podcast.xml",
    encoding="utf-8",
    xml_declaration=True
)

print("podcast.xml generated successfully!")
