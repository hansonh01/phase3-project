from db.models import Base, Drink, Food, Customer, Order, MenuItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('sqlite:///db/bobashop.db')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    session.query(Food).delete()
    session.query(Drink).delete()
    session.query(MenuItem).delete()
    session.query(Customer).delete()
    session.query(Order).delete()

    boba_menu = [
        {"name": "Classic Milk Tea", "category": "Milk Tea", "price": 4.99},
        {"name": "Taro Bubble Tea", "category": "Flavored Tea", "price": 5.49},
        {"name": "Strawberry Smoothie", "category": "Smoothie", "price": 6.99},
        {"name": "Matcha Latte", "category": "Latte", "price": 5.99},
        {"name": "Brown Sugar Pearl Tea", "category": "Milk Tea", "price": 6.49},
        {"name": "Honeydew Bubble Tea", "category": "Flavored Tea", "price": 5.99},
        {"name": "Mango Yakult", "category": "Yakult", "price": 4.79},
        {"name": "Peach Green Tea", "category": "Tea", "price": 4.49},
        {"name": "Coconut Smoothie", "category": "Smoothie", "price": 6.49},
        {"name": "Vietnamese Coffee", "category": "Coffee", "price": 5.79},
        {"name": "Red Bean Milk Tea", "category": "Milk Tea", "price": 5.29},
        {"name": "Blueberry Yogurt Drink", "category": "Yogurt", "price": 5.99},
        {"name": "Passion Fruit Green Tea", "category": "Tea", "price": 4.99},
        {"name": "Mango Bubble Tea", "category": "Flavored Tea", "price": 5.49},
        {"name": "Lavender Latte", "category": "Latte", "price": 6.29},
        {"name": "Lychee Smoothie", "category": "Smoothie", "price": 6.49},
        {"name": "Strawberry Kiwi Yogurt Drink", "category": "Yogurt", "price": 5.99},
        {"name": "Pineapple Green Tea", "category": "Tea", "price": 4.79},
        {"name": "Caramel Macchiato", "category": "Coffee", "price": 6.49},
        {"name": "Watermelon Slush", "category": "Slush", "price": 5.99}]
    
    food_menu = [
    {"name": "Popcorn Chicken", "spice_level": 2, "price": 5.99},
    {"name": "Fried Tofu", "spice_level": 1, "price": 4.99},
    {"name": "Sweet Potato Fries", "spice_level": 1, "price": 3.99},
    {"name": "Taiwanese Sausage", "spice_level": 3, "price": 6.49},
    {"name": "Fried Calamari", "spice_level": 2, "price": 5.49}]

    full_menu = []

    def create_drinks():
        for boba_tea in boba_menu:
            drink = Drink(
                name = boba_tea['name'],
                category = boba_tea['category'],
                price = boba_tea['price']
            )
            session.add(drink)
            session.commit()
            full_menu.append(boba_tea)
    
    def create_foods():
        for food_item in food_menu:
            food = Food(
                name = food_item["name"],
                spice_level = food_item["spice_level"],
                price = food_item["price"]
            )
            session.add(food)
            session.commit()
            full_menu.append(food_item)
    
    def create_menu():
        for item in full_menu:
            menuitem = MenuItem(
                name = item['name'],
                price = item['price']
            )
            session.add(menuitem)
            session.commit()

    create_drinks()
    create_foods()
    create_menu()

    admin_ = []

    def example_customer(admin,num):
        admin = Customer(
            id=1,
            name=admin,
            phone_number=num
        )
        session.add(admin)
        session.commit()
        admin_.append(admin)
    
    def example_order(item,num,id):
        admin = Order(
            items=item,
            total_price=num,
            customer_id=id
        )
        session.add(admin)
        session.commit()

    example_customer('Admin',1234)
    example_order("Mango Yakult",4.79,admin_[0].id)