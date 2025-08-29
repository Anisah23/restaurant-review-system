from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, validates
from lib.models import Base, session

class MenuItem(Base):
    __tablename__ = 'menu_items'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    restaurant_id = Column(Integer, ForeignKey('restaurants.id'))
  
    restaurant = relationship('Restaurant', back_populates='menu_items')
    
    def __repr__(self):
        return f'<MenuItem {self.id}: {self.name} - ${self.price}>'
    
    # ORM Methods
    @classmethod
    def get_all(cls):
        return session.query(cls).all()
    
    @classmethod
    def find_by_id(cls, id):
        return session.query(cls).filter(cls.id == id).first()
    
    @classmethod
    def find_by_restaurant(cls, restaurant_id):
        return session.query(cls).filter(cls.restaurant_id == restaurant_id).all()
    
    @classmethod
    def create(cls, name, price, description, restaurant_id):
        menu_item = cls(name=name, price=price, description=description, restaurant_id=restaurant_id)
        session.add(menu_item)
        session.commit()
        return menu_item
    
    def delete(self):
        session.delete(self)
        session.commit()
    
    # Validation
    @validates('price')
    def validate_price(self, key, price):
        price = float(price)
        if price <= 0:
            raise ValueError("Price must be greater than 0")
        return price