import sqlalchemy
from sqlalchemy import Column,Integer,String, Float, ForeignKey
from sqlalchemy.orm import relationship, backref

Base = sqlalchemy.orm.declarative_base()

class Drink(Base):
    __tablename__ = 'drinks'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())
    price = Column(Float())

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.category}, {self.price})"

class Food(Base):
    __tablename__ = 'foods'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    spice_level = Column(Integer())
    price = Column(Float())

    def __repr__(self):
        return f"({self.id},{self.name},{self.spice_level}, {self.price})"

class MenuItem(Base):
    __tablename__ = 'menuitems'
    
    id = Column(Integer(),primary_key=True)
    name = Column(String())
    price = Column(Float())

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.price})"

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phone_number = Column(String())

    order = relationship("Order",backref=backref('customers'))
    history = relationship('History',backref=backref('customers'))

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.phone_number}, {self.order})"

class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer(), primary_key=True)
    items = Column(String())
    total_price = Column(Float())
    customer_id = Column(Integer(), ForeignKey('customers.id'))

    def __repr__(self):
        return f"({self.id}, {self.items}, {self.total_price}, {self.customer_id})"

class History(Base):
    __tablename__ = 'histories'

    id = Column(Integer(),primary_key=True)
    items = Column(String())
    total_price = Column(Float())
    customer_id = Column(Integer(), ForeignKey("customers.id"))

    def __repr__(self):
        return f"({self.id}, {self.items}, {self.total_price}, {self.customer_id})"