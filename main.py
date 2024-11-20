from database import add_entry
from ui import display_entries
import sys
type = sys.argv[0]
title = sys.argv[1]
link = sys.argv[2]
tags = sys.argv[3]

tag_list = [tag.strip() for tag in tags.split(",")]
add_entry(type, title, link, tag_list)
print(f"Added {type} entry with link: {link} and tags: {tags}")



