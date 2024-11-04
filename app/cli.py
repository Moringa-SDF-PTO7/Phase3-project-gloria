import click
from .database import SessionLocal, init_db
from .models import Author, Book

@click.group()
def cli():
    """A simple CLI for managing authors and books."""
    pass

@cli.command()
def init():
    """Initialize the database."""
    init_db()
    click.echo("Database initialized.")

@cli.command()
@click.argument('name')
def add_author(name):
    """Add a new author."""
    db = SessionLocal()
    new_author = Author(name=name)
    db.add(new_author)
    db.commit()
    db.refresh(new_author)
    click.echo(f"Added author: {new_author.name} with ID {new_author.id}")
    db.close()

@cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
def add_book(title, author_id):
    """Add a new book with the given author ID."""
    db = SessionLocal()
    new_book = Book(title=title, author_id=author_id)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    click.echo(f"Added book: {new_book.title} with ID {new_book.id} for author ID {author_id}")
    db.close()

@cli.command()
def list_authors():
    """List all authors."""
    db = SessionLocal()
    authors = db.query(Author).all()
    for author in authors:
        click.echo(f"ID: {author.id}, Name: {author.name}")
    db.close()

@cli.command()
def list_books():
    """List all books."""
    db = SessionLocal()
    books = db.query(Book).all()
    for book in books:
        click.echo(f"ID: {book.id}, Title: {book.title}, Author ID: {book.author_id}")
    db.close()

if __name__ == "__main__":
    cli()
