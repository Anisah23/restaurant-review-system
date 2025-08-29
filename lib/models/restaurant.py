from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from lib.models import Base, session

class Restaurant(Base):
    __tablename__ = 'restaurants'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    # Relationships
    reviews = relationship('Review', back_populates='restaurant', cascade='all, delete-orphan')
    menu_items = relationship('MenuItem', back_populates='restaurant', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Restaurant {self.id}: {self.name}>'
    
    # ORM Methods 
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def find_by_name(cls, name):
        return session.query(cls).filter(cls.name.ilike(f'%{name}%')).all()
    
    @classmethod
    def create(cls, name):
        restaurant = cls(name=name)
        session.add(restaurant)
        session.commit()
        return restaurant
    
    def delete(self):
        session.delete(self)
        session.commit()
    
    @property
    def average_rating(self):
        if not self.reviews:
            return 0
        total = sum(review.star_rating for review in self.reviews)
        return round(total / len(self.reviews), 1)