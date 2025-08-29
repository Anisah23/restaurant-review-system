from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.models import Base, session

class Review(Base):
    __tablename__ = 'reviews'
    
    id = Column(Integer, primary_key=True)
    star_rating = Column(Integer)  
    comment = Column(String)  
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))  
    
   
    restaurant = relationship('Restaurant', back_populates='reviews')
    
    def __repr__(self):
        return f'<Review {self.id}: {self.star_rating} stars>'
    
    # CLASS METHODS
    
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def create(cls, star_rating, comment, restaurant_id):
        review = cls(star_rating=star_rating, comment=comment, restaurant_id=restaurant_id)
        session.add(review)
        session.commit()
        return review
    
    # INSTANCE METHODS
    
    def delete(self):
        session.delete(self)
        session.commit()
    
    # VALIDATION 
    @validates('star_rating')
    def validate_rating(self, key, rating):
        """Ensure rating is between 1 and 5 stars"""
        rating = int(rating)
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be between 1 and 5 stars")
        return rating