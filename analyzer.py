print()
print("Welcome to Banty's Inventory List Analyzer!")
print()

items = []              
quantity_list = []       
category_set = set()     
item_quantity_dict = {} 

while True:
    name = input("Enter item name: ").strip()
    category = input("Enter category: ").strip().lower()
    quantity = int(input("Enter quantity: "))
           
    items.append((name, category, quantity))
    quantity_list.append(quantity)
    item_quantity_dict[name] = quantity
    category_set.add(category)
    print()
    more = input("Do you want to add more items? (y/n): ").strip().lower()
    print()
    if more != 'y':
        break
print("============ INVENTORY SUMMARY ============")
print()
total_items = len(items)
print(f"Total Different Items: {total_items}")
print(f"Explanation: You entered {total_items} different items: "
      + ", ".join([i[0] for i in items]) + ".")
print()

total_quantity = sum(quantity_list)
print(f"Total Quantity in Stock: {total_quantity}")
print(f"Explanation: Sum of all quantities: "
      f"{' + '.join(str(q) for q in quantity_list)} = {total_quantity}")
print()

average = total_quantity / total_items
print(f"Average Quantity per Item: {average}")
print(f"Explanation: Average = {total_quantity} total / {total_items} items")
print()

most_item = max(items, key=lambda x: x[2])
least_item = min(items, key=lambda x: x[2])

print(f"Most Stocked Item: {most_item[0]} ({most_item[2]} units)")
print(f"Explanation: {most_item[0]} Has The Highest Quantity Among All Items.")
print()
print(f"Least Stocked Item: {least_item[0]} ({least_item[2]} units)")
print(f"Explanation: {least_item[0]} Has The Lowest Quantity.")
print()


print("------------------------------------------")
print()
print(f"Unique Categories in Inventory: {category_set}")
print("Explanation: Categories are taken from user input and converted to lowercase.")
print("No duplicates are shown here.")
print()

sorted_by_qty = sorted(items, key=lambda x: x[2], reverse=True)

print("------------------------------------------")
print("📦 Items Sorted by Quantity (High to Low):")
print()

for i, item in enumerate(sorted_by_qty, 1):
    print(f"{i}. {item[0]} - {item[2]} units")
print()
print("Explanation: Items are sorted using quantity from highest to lowest.")
print()

sorted_categories = sorted(category_set)

print("------------------------------------------")
print("📂 Categories in Alphabetical Order:")
print()

for i, c in enumerate(sorted_categories, 1):
    print(f"{i}. {c}")
print()
print("Explanation: The set of unique categories was sorted alphabetically for display.")
print()
print("=========== END OF REPORT ===========")