# billing-system
This Python program simulates an ice cream parlour's billing system. Customers can order various ice cream products, and the program calculates the total bill, including taxes and discounts. Additionally, it provides system settings for managing the menu and other configurations.

Getting Started
Clone this repository:

bash
Copy code
git clone https://github.com/your-username/ice-cream-parlour.git
Navigate to the project directory:

bash
Copy code
cd ice-cream-parlour
Run the program:

bash
Copy code
python ice_cream_parlour.py
Features
Menu: The program provides a menu of ice cream products with their prices.

Billing: Customers can add products to their order, and the program calculates the total bill, including taxes and discounts.

Taxes: A General Sales Tax (GST) of 17% is applied to all food-related products.

Discounts: Customers receive a 10% discount when paying with a card.

Service Charges: A 10% service charge is applied to dine-in orders.

System Settings: The program offers system settings to manage the menu, including adding, updating, and deleting products.

Menu
The menu is stored in a dictionary with product names as keys and their respective prices as values.

python
Copy code
menu = {
    "vanilla ice cream": 120,
    "strawberry ice cream": 120,
    "caramel ice cream": 120,
    "waffle cone": 190,
    "waffle bowl": 190,
    # ... (other menu items)
}
System Settings
The program includes system settings accessible via extensions. Here are the available extensions:

Extension 2: Update the price of a product.
Extension 3: Delete a product from the menu.
Extension 4: Add a new product to the menu.
Extension 5: Display all products and their prices.
Extension 6: Update the General Sales Tax (GST) rate.
Usage
Start the program by running python ice_cream_parlour.py.

Choose a shift (1st or 2nd) for the cashier on duty.

Enter bill to generate a bill for a customer or setting to access system settings.

Follow the prompts to enter the customer's order.

The program calculates the bill, including taxes and discounts.

Payment can be made using either cash or a card (with a 10% discount).

The program displays the receipt with details of the transaction.

You can continue processing bills or access system settings as needed.

Extensions
To access system settings, enter the corresponding extension number:

Enter 2 to update the price of a product.
Enter 3 to delete a product from the menu.
Enter 4 to add a new product to the menu.
Enter 5 to display all products and their prices.
Enter 6 to update the General Sales Tax (GST) rate.
