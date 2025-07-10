# Seller information
seller_name = " ABC Retail"
seller_address = " 200, Xyz street,\n NJ-12345-6789"
seller_contact = "987-654-321"

# Decorating the top segment
print("-" * 50)
print(f"{seller_name}")
print(f"{seller_address}")
print("-" * 50)

apricot_pack = 30
dates_pack = 40
almonds_pack = 50
apricot_dates_combo = (apricot_pack + dates_pack) * .9  # 10% discount
dates_almond_combo = (dates_pack + almonds_pack) * .9  # 10% discount
almond_apricot_combo = (almonds_pack+ apricot_pack) * .9  # 10% discount
gift_pack = (apricot_pack + dates_pack + almonds_pack) * .75  # 25% discount
print("Product(s) \tPrice (per pack)")
print(f"Apricot\t\t{apricot_pack}")
print(f"Dates\t\t{dates_pack}")
print(f"Almond\t\t{almonds_pack}")
print(f"Combo-1\t\t{apricot_dates_combo}")
print(f"Combo-2\t\t{dates_almond_combo}")
print(f"Combo-3\t\t{almond_apricot_combo}")
print(f"GiftBox\t\t{gift_pack}")

# Decorating the bottom segment.
# It contains the contact information.
print("*" * 50)
print(f"For free delivery, contact {seller_contact} ")
print("*" * 50)
