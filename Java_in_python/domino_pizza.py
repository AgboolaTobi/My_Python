def order_list():
    large_size = 10
    medium_size = 6
    small_size = 4
    price_of_large = 5000
    price_of_medium = 3000
    price_of_small = 1200

    super_hungry = 4
    hungry = 2
    classic = 1

    print("""
    ===Available on the Order List===
        1. Large size
        2. Medium size
        3. Small size
        4. Return to menu
        """)
    customers_order = input("Make your order: ")
    if customers_order == "1":
        super_hungry_guests = int(input("Enter the number of super hungry guests: "))
        hungry_guests = int(input("Enter the number of hungry guests: "))
        classic_guests = int(input("Enter number of classic guest: "))
        total_number_of_slices_ordered = (super_hungry * super_hungry_guests) + (hungry * hungry_guests) + (
                classic * classic_guests)
        if total_number_of_slices_ordered % large_size == 0:
            total_number_of_boxes = total_number_of_slices_ordered / large_size
            total_cost_of_order = total_number_of_boxes * price_of_large
            number_of_left_over = 0
            return f"Total number of slices ordered: {total_number_of_slices_ordered}\n The total number of boxes bought: {total_number_of_boxes}\nThe total cost of order: {total_cost_of_order}\nTotal number of left over: {number_of_left_over}"
        else:
            total_number_of_boxes = total_number_of_slices_ordered // large_size + 1
            total_cost_of_order = (total_number_of_slices_ordered // large_size) * price_of_large + price_of_large
            number_of_left_over = (total_number_of_boxes * large_size) - total_number_of_slices_ordered
            return f"Total number of slices ordered: {total_number_of_slices_ordered}\nThe total number of boxes bought: {total_number_of_boxes}\nThe total cost of order: {total_cost_of_order}\nTotal number of left over: {number_of_left_over}"
    elif customers_order == "2":
        super_hungry_guests = int(input("Enter the number of super hungry guests: "))
        hungry_guests = int(input("Enter the number of hungry guests: "))
        classic_guests = int(input("Enter number of classic guest: "))
        total_number_of_slices_ordered = (super_hungry * super_hungry_guests) + (hungry * hungry_guests) + (
                classic * classic_guests)
        if total_number_of_slices_ordered % medium_size == 0:
            total_number_of_boxes = total_number_of_slices_ordered / medium_size
            total_cost_of_order = total_number_of_boxes * price_of_medium
            number_of_left_over = 0

            return f"Total number of slices ordered: {total_number_of_slices_ordered}\n The total number of boxes bought: {total_number_of_boxes}\nThe total cost of order: {total_cost_of_order}\nTotal number of left over: {number_of_left_over}"
        else:
            total_number_of_boxes = total_number_of_slices_ordered // medium_size + 1
            total_cost_of_order = (total_number_of_slices_ordered // medium_size) * price_of_medium + price_of_medium
            number_of_left_over = (total_number_of_boxes * medium_size) - total_number_of_slices_ordered
            return f"Total number of slices ordered: {total_number_of_slices_ordered}\nThe total number of boxes bought: {total_number_of_boxes}\nThe total cost of order: {total_cost_of_order}\nTotal number of left over: {number_of_left_over}"

    elif customers_order == "3":
        super_hungry_guests = int(input("Enter the number of super hungry guests: "))
        hungry_guests = int(input("Enter the number of hungry guests: "))
        classic_guests = int(input("Enter number of classic guest: "))
        total_number_of_slices_ordered = (super_hungry * super_hungry_guests) + (hungry * hungry_guests) + (
                classic * classic_guests)
        if total_number_of_slices_ordered % small_size == 0:
            total_number_of_boxes = total_number_of_slices_ordered / small_size
            total_cost_of_order = total_number_of_boxes * price_of_small
            number_of_left_over = 0

            return f"Total number of slices ordered: {total_number_of_slices_ordered}\n The total number of boxes bought: {total_number_of_boxes}\nThe total cost of order: {total_cost_of_order}\nTotal number of left over: {number_of_left_over}"
        else:
            total_number_of_boxes = total_number_of_slices_ordered // small_size + 1
            total_cost_of_order = (total_number_of_slices_ordered // small_size) * price_of_small + price_of_small
            number_of_left_over = (total_number_of_boxes * small_size) - total_number_of_slices_ordered
            return f"Total number of slices ordered: {total_number_of_slices_ordered}\nThe total number of boxes bought: {total_number_of_boxes}\nThe total cost of order: {total_cost_of_order}\nTotal number of left over: {number_of_left_over}"

    else:
        order_list()


print(order_list())
