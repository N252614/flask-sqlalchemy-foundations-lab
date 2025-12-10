from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

class Earthquake(db.Model):
    """Model representing an earthquake record in the database."""

    # Name of the table in the database
    __tablename__ = "earthquakes"

    # Primary key column: unique integer ID for each earthquake
    id = db.Column(db.Integer, primary_key=True)

    # Magnitude of the earthquake (floating point value)
    magnitude = db.Column(db.Float)

    # Location of the earthquake 
    location = db.Column(db.String)

    # Year when the earthquake occurred
    year = db.Column(db.Integer)

    def __repr__(self):
        """Readable string representation of an Earthquake instance."""
        return f"<Earthquake {self.id}, {self.magnitude}, {self.location}, {self.year}>"
