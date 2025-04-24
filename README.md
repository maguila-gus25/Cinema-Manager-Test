# Cinema Manager System

A Python-based cinema management system that handles movies, rooms, sessions, tickets, sales, and clients.

## Project Structure

```
cinema-manager/
├── database.py           # Database configuration and connection
├── movie.py             # Movie class and operations
├── room.py              # Room class and operations
├── session.py           # Session class and operations
├── ticket.py            # Ticket class and operations
├── sale.py              # Sale class and operations
├── client.py            # Client class and operations
└── main.py              # Main application and example usage
```

## Database Structure

The system uses SQLite with the following tables:

- `movies`: Stores movie information
- `rooms`: Stores room information
- `seats`: Stores seat information
- `sessions`: Stores session information
- `tickets`: Stores ticket information
- `sales`: Stores sale information
- `clients`: Stores client information

## Features

- Movie Management
  - Add, update, and remove movies
  - Track movie details (title, duration, genre, age rating, synopsis)

- Room Management
  - Add, update, and remove rooms
  - Track room details (number, type, capacity)

- Session Management
  - Create, update, and cancel sessions
  - Track session details (movie, room, time, date, available tickets)

- Ticket Management
  - Issue and cancel tickets
  - Check ticket availability
  - Track ticket status

- Sale Management
  - Register and cancel sales
  - Generate receipts
  - Track payment methods and totals

- Client Management
  - Track client information
  - Maintain purchase history

## Getting Started

1. Clone the repository
2. Install dependencies (if any)
3. Run `main.py` to initialize the database and see example usage

## Example Usage

```python
# Initialize database
from database import init_db
init_db()

# Create a movie
from movie import Movie
movie = Movie("Inception", 148, "Sci-Fi", "PG-13", "A thief who steals corporate secrets...")
movie.add_movie()

# Create a room
from room import Room
room = Room(1, "Standard", 100)
room.add_room()

# Create a session
from session import Session
session = Session(movie.id, room.id, "19:00", "2024-03-20", 100)
session.create_session()

# Create a ticket
from ticket import Ticket
ticket = Ticket(session.id, 1, 15.00)
ticket.issue_ticket()

# Register a client
from client import Client
client = Client("John Doe", "john@example.com", "1234567890")
client.save()

# Make a sale
from sale import Sale
sale = Sale(client.id, ticket.id, "Credit Card", 15.00)
sale.register_sale()
```

## Dependencies

- Python 3.x
- SQLite3

## License

This project is free to use for anyone. Feel free to use, modify, and distribute it as you wish.

## 🤝 Contributing

Contributions are welcome! To contribute to the project:

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👥 Authors

- maguila-gorila25 - [@maguila-gorila25](https://github.com/maguila-gorila25)

## 🙏 Acknowledgments

- Thanks to everyone who has contributed to this project
- Special thanks to the open-source community for inspiration and tools

---

© 2024 Cinema Manager - Made with ❤️
