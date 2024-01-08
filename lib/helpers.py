from db.models import Base, Drink, Food, Customer, Order, MenuItem
from sqlalchemy import create_engine, update, delete
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///db/bobashop.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def exit_program():
    print("Goodbye! ")
    exit()

def intro():
    print('Welcome to Teatopia! ')
    print("-"*70)

    username = input('Please enter your name: ')
    phone = input('Please enter your phone number: ')
    if isinstance(username,str) and 3 <= len(username) <= 10:
        existing_customer = session.query(Customer).filter_by(name=username,phone_number=phone).first()
        if existing_customer:
            print('-'*70)
            print(f'Welcome back! {existing_customer.name}')
            user = existing_customer.name
        else:
            print('-'*70)
            print(f"Welcome! {username}")
            customer = Customer(name=username.lower(),phone_number=phone)
            user = customer.name
            session.add(customer)
            session.commit()
    return user

def show_menu(user):
    menu = session.query(MenuItem).all()
    for item in menu:
        print(f"{item.id}: {item.name} - ${item.price}")
    place_order(user)

def place_order(user):
    order_items = []
    total_price = 0
    while True:
        print("-"*70)
        print(f"\nTo place an order, enter item's number: ")
        print(f'\nTo return back to Main Menu Enter "0"')
        choice = (input("> "))
        
        try:
            item_number = int(choice)
            item = session.query(MenuItem).filter_by(id=item_number).first()
            if item_number == 0:
                break
            elif item and item_number <= 25:
                order_items.append(item)
                print(f"\n {item.name} has been added to your order.")    
            else:
                print("Not a Valid Entry. Please Try Again.")
        except ValueError as ve:
            print("Not a Valid Entry. Please Try Again.",ve)
    
    for item in order_items:
        total_price += item.price
    
    if order_items != []:
        print("\nYou ordered: ")
        for item in order_items:
            print(item.name)
        print(f"\nYour total is: ${total_price:.2f}")
        order_item_names = ", ".join(item.name for item in order_items)
        customer = session.query(Customer).filter_by(name=user).first()
        new_order = Order(
            items = order_item_names,
            total_price = total_price,
            customer_id = customer.id
        )
        session.add(new_order)
        session.commit()
    else:
        print("\nYour Order is currently Empty.")

def find_item_by_ID():
    id_ = input("Enter item's ID: ")
    item = session.query(MenuItem).filter_by(id=id_).first()
    print(item) if item else print(f'Item {id_} not found')

def find_item_by_name():
    name_ = input("Enter item's name: ")
    item = session.query(MenuItem).filter_by(name=name_).first()
    print(item) if item else print(f'Item {name_} not found')

def update_order(user):
    user_ = session.query(Customer).filter_by(name=user).first()
    id_ = int(input("Enter Order ID: "))
    order_ = session.query(Order).filter_by(id=id_,customer_id=user_.id).first()
    if order_:
        print(f"{order_.items}")
        print(f"{order_.total_price:.2f}")
        print("-"*70)
        print("Choose one of the following options: ")
        print("0. Return")
        print("1. Add items")
        print("2. Remove items")
        choice = int(input("> "))
        while True:
            if choice == 0:
                break
            elif choice == 1:
                add_item(order_)
    else:
        print("Order Not Found")

def add_item(order_):
    items_ = order_.items.split(", ")
    total = order_.total_price
    menu = session.query(MenuItem).all()
    for item in menu:
        print(f"{item.id}: {item.name} - ${item.price}")
    while True:
        print("-"*70)
        print(f"\nTo place an order, enter item's number: ")
        print(f'\nTo return back to Main Menu Enter "0"')
        choice = input("> ")
        try:
            item_number = int(choice)
            item = session.query(MenuItem).filter_by(id=item_number).first()
            if item_number == 0:
                break
            elif item and item_number <= 25:
                items_.append(item.name)
                total += item.price
                print(f"\n {item.name} has been added to your order.")    
            else:
                print("Not a Valid Entry. Please Try Again.")
        except ValueError as ve:
            print("Not a Valid Entry. Please Try Again.",ve)
    
    order_item_names = ", ".join(item for item in items_)
    update_order = update(Order).where(Order.id == order_.id).values(total_price=total,items=order_item_names)
    session.execute(update_order)
    session.commit()


def delete_order(user):
    user_ = session.query(Customer).filter_by(name=user).first()
    id_ = int(input("Enter Order ID: "))
    order_ = session.query(Order).filter_by(id=id_,customer_id=user_.id).first()
    while True:
        if order_:
            print(f"Confirm Actions (y/n): ")
            choice = input("> ")
            if choice == 'y':
                order_.delete()
            else:
                break
        else:
            print('Invalid ID. Please Try Again.')


def view_order_history(user):
    user_ = session.query(Customer).filter_by(name=user).first()
    if user:
        print("Order history:")
        for orders in user_.history:
            print("-" * 70)
            print(f"Order ID: {orders.id}")
            print(f"Items ordered: {orders.order_items} \n")
            print(f"Order total:  ${orders.total:.2f}")
    else:
        print("It seems like you haven't ordered from us yet.")

