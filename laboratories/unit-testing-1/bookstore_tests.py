import pytest

from bookstore.book import Book
from bookstore.book_repository import InMemoryBookRepository
from bookstore.services.book_filtering_service import BookFilterService
from bookstore.services.bookstore_service import BookStoreService


@pytest.fixture
def create_book_service():
    """
    INSTRUCTIONS:
    - Create and return a BookService instance
    - Use InMemoryBookRepository for storage
    - Use default BookFilterService
    """
    repository = InMemoryBookRepository()
    book_filter_service = BookFilterService()
    return BookStoreService(repository, book_filter_service)


@pytest.fixture
def create_sample_book():
    """
    INSTRUCTIONS:
    - Create a Book instance with sample data
    - Use realistic values for title, author, genre, and price
    """
    return Book(title="1984", author="George Orwell", genre="Dystopian", price=35.50)


def test_add_book(create_book_service, create_sample_book):
    """
    TESTING OBJECTIVES:
    1. Create a book service using the fixture
    2. Create a sample book using the fixture
    3. Add the book to the service
    4. Verify:
       - Book has a non-None ID
       - Book attributes match the original book
    """
    service = create_book_service
    book = create_sample_book
    
    added_book = service.add_book(book)
    
    assert added_book.id is not None
    assert added_book.title == "1984"
    assert added_book.author == "George Orwell"
    assert added_book.genre == "Dystopian"
    assert added_book.price == 35.50


def test_add_book_validation(create_book_service):
    """
    TESTING OBJECTIVES:
    1. Attempt to add a book with invalid data
    2. Verify appropriate exception is raised
    """
    service = create_book_service
    
    with pytest.raises(ValueError):
        service.add_book(Book(title="", author="Author", genre="Sci-Fi", price=20.0))
        
    with pytest.raises(ValueError):
        service.add_book(Book(title="Title", author="", genre="Sci-Fi", price=20.0))


@pytest.mark.parametrize("search_genre, expected_count", [
    ("Sci-Fi", 2),
    ("sci-fi", 2),
    ("Fantasy", 1),
    ("Romance", 0)
])
def test_get_books_by_genre(create_book_service, search_genre, expected_count):
    """
    TESTING OBJECTIVES:
    1. Add multiple books with different genres
    2. Filter books by specific genres
    3. Verify:
       - Only books of the specified genre are returned
       - Filtering is case-insensitive
    """
    service = create_book_service
    
    service.add_book(Book("Dune", "Frank Herbert", "Sci-Fi", 50.0))
    service.add_book(Book("Foundation", "Isaac Asimov", "sci-fi", 45.0))
    service.add_book(Book("The Hobbit", "J.R.R. Tolkien", "Fantasy", 60.0))

    filtered_books = service.get_books(genre=search_genre)

    assert len(filtered_books) == expected_count


@pytest.mark.parametrize("min_price, max_price, expected_count", [
    (20.0, 50.0, 2),
    (None, 30.0, 2),
    (35.0, None, 2),
    (100.0, 200.0, 0)
])
def test_price_range_filtering(create_book_service, min_price, max_price, expected_count):
    """
    TESTING OBJECTIVES:
    1. Add books at different price points
    2. Test filtering by min, max, and combined
    """
    service = create_book_service
    
    service.add_book(Book("Book 1", "Author", "Fiction", 15.0))
    service.add_book(Book("Book 2", "Author", "Fiction", 25.0))
    service.add_book(Book("Book 3", "Author", "Fiction", 40.0))
    service.add_book(Book("Book 4", "Author", "Fiction", 60.0))

    filtered_books = service.get_books(min_price=min_price, max_price=max_price)

    assert len(filtered_books) == expected_count


def test_update_book(create_book_service, create_sample_book):
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Update the book's details
    3. Verify updates and unchanged attributes
    """
    service = create_book_service
    added_book = service.add_book(create_sample_book)
    
    updated_book = service.update_book(added_book.id, price=99.99, genre="Classic")
    
    assert updated_book.price == 99.99
    assert updated_book.genre == "Classic"
    
    assert updated_book.title == "1984"
    assert updated_book.author == "George Orwell"


def test_remove_book(create_book_service, create_sample_book):
    """
    TESTING OBJECTIVES:
    1. Add a book to the service
    2. Remove the book
    3. Verify successful removal and non-existent removal
    """
    service = create_book_service
    added_book = service.add_book(create_sample_book)
    
    success = service.remove_book(added_book.id)
    assert success is True
    
    toate_cartile = service.get_books()
    assert not any(book.id == added_book.id for book in toate_cartile)
    
    success_not_found = service.remove_book(999)
    assert success_not_found is False