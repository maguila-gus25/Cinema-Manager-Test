from database import get_db_connection

class Movie:
    def __init__(self, title, duration, genre, age_rating, synopsis=None, id=None):
        self.id = id
        self.title = title
        self.duration = duration
        self.genre = genre
        self.age_rating = age_rating
        self.synopsis = synopsis

    def add_movie(self):
        self.save()
        return f"Movie '{self.title}' added successfully."

    def update_movie(self, title=None, duration=None, genre=None, age_rating=None, synopsis=None):
        if title is not None:
            self.title = title
        if duration is not None:
            self.duration = duration
        if genre is not None:
            self.genre = genre
        if age_rating is not None:
            self.age_rating = age_rating
        if synopsis is not None:
            self.synopsis = synopsis
        self.save()
        return f"Movie '{self.title}' updated successfully."

    def remove_movie(self):
        self.delete()
        return f"Movie '{self.title}' removed successfully."

    def save(self):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            if self.id is None:
                cursor.execute('''
                    INSERT INTO movies (title, duration, genre, age_rating, synopsis)
                    VALUES (?, ?, ?, ?, ?)
                ''', (self.title, self.duration, self.genre, self.age_rating, self.synopsis))
                self.id = cursor.lastrowid
            else:
                cursor.execute('''
                    UPDATE movies
                    SET title = ?, duration = ?, genre = ?, age_rating = ?, synopsis = ?
                    WHERE id = ?
                ''', (self.title, self.duration, self.genre, self.age_rating, self.synopsis, self.id))
            conn.commit()

    def delete(self):
        if self.id is not None:
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('DELETE FROM movies WHERE id = ?', (self.id,))
                conn.commit()

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM movies')
            movies = [Movie(row['title'], row['duration'], row['genre'], 
                          row['age_rating'], row['synopsis'], row['id'])
                     for row in cursor.fetchall()]
            return movies

    @staticmethod
    def get_by_id(movie_id):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM movies WHERE id = ?', (movie_id,))
            row = cursor.fetchone()
            if row:
                return Movie(row['title'], row['duration'], row['genre'],
                           row['age_rating'], row['synopsis'], row['id'])
            return None

    def __str__(self):
        return (f"Movie: {self.title}\n"
                f"Duration: {self.duration} minutes\n"
                f"Genre: {self.genre}\n"
                f"Age Rating: {self.age_rating} years\n"
                f"Synopsis: {self.synopsis}")