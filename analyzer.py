print("Welcome to Banty's Inventory List Analyzer!")
print()

items = []
quantity_list = []
category_set = set()
item_quantity_dict = {}

while True:
    name = input("Enter item name: ").strip()
    category = input("Enter category: ").strip().lower()

    qty_input = input("Enter quantity: ")
    if qty_input.isdigit():
        quantity = int(qty_input)
    else:
        print("Invalid quantity! Setting quantity = 0")
        quantity = 0

    items.append((name, category, quantity))
    quantity_list.append(quantity)
    item_quantity_dict[name] = quantity
    category_set.add(category)

    more = input("Do you want to add more items? (y/n): ").strip().lower()
    print()
    if more != 'y':
        break

print("============ INVENTORY SUMMARY ============")
print()

total_items = len(items)
print("Total Different Items:", total_items)
print("Explanation: You entered " + str(total_items) +
      " different items: " + ", ".join(i[0] for i in items) + ".")
print()

total_quantity = sum(quantity_list)
print("Total Quantity in Stock:", total_quantity)
print("Explanation: Sum of all quantities: " +
      " + ".join(str(q) for q in quantity_list) +
      " = " + str(total_quantity))
print()

average = total_quantity / total_items
print("Average Quantity per Item:", average)
print("Explanation: Average = " + str(total_quantity) +
      " total / " + str(total_items) + " items")
print()

max_item = items[0]
for item in items:
    if item[2] > max_item[2]:
        max_item = item

min_item = items[0]
for item in items:
    if item[2] < min_item[2]:
        min_item = item

print("Most Stocked Item:", max_item[0], f"({max_item[2]} units)")
print(f"Explanation: {max_item[0]} Has The Highest Quantity Among All Items.")
print()
print("Least Stocked Item:", min_item[0], f"({min_item[2]} units)")
print(f"Explanation: {min_item[0]} Has The Lowest Quantity.")
print()
print("------------------------------------------")
print()
print("Unique Categories in Inventory:", category_set)
print("Explanation: Categories are taken from user input and converted to lowercase.")
print()

sorted_items = items[:]
n = len(sorted_items)
for i in range(n):
    for j in range(0, n - i - 1):
        if sorted_items[j][2] < sorted_items[j + 1][2]:
            sorted_items[j], sorted_items[j + 1] = sorted_items[j + 1], sorted_items[j]

print("------------------------------------------")
print("📦 Items Sorted by Quantity (High to Low):")
print()

counter = 1
for item in sorted_items:
    print(str(counter) + ". " + item[0] + " - " + str(item[2]) + " units")
    counter += 1

print()
print("Explanation: Items are sorted from highest to lowest quantity.")
print()

sorted_categories = sorted(category_set)

print("------------------------------------------")
print("📂 Categories in Alphabetical Order:")
print()

counter = 1
for c in sorted_categories:
    print(str(counter) + ". " + c)
    counter += 1

print()
print("Explanation: Categories are shown alphabetically.")
print()

print("=========== END OF REPORT ===========")
