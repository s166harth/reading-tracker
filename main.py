import click
from database import add_entry
from ui import display_entries

@click.group()
def cli():
    pass

@cli.command()
@click.argument("type")
@click.argument("title")
@click.argument("link")
@click.argument("tags")
def add(type, title, link, tags):
    # Extract a placeholder title from the link if the type is YouTube, or use a generic title
   # title = link.split("/")[-1] if type.lower() == "youtube" else "Untitled"
    tag_list = [tag.strip() for tag in tags.split(",")]
    add_entry(type, title, link, tag_list)
    click.echo(f"Added {type} entry with link: {link} and tags: {tags}")

@cli.command()
def view():
    display_entries()

if __name__ == '__main__':
    cli()

