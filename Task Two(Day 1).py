#Getting the Input
charges_per_hour = 20.00
wall_size = float(input("Enter the wall size: "))

#Calculations
number_of_galons = (wall_size / 115)
hours_required = ((8 * wall_size) / 115)
price_of_paint_per_galon = float(input("Enter the price of paint: "))
cost_of_paint = number_of_galons * price_of_paint_per_galon
labour_charges = charges_per_hour * hours_required
total_cost = cost_of_paint + labour_charges

#Format the floating values
format_number_of_galons = format(number_of_galons,",.2f")
format_hours_required = format(hours_required,",.2f")
format_price_of_paint_per_galon = format(price_of_paint_per_galon,",.2f")
format_cost_of_paint = format(cost_of_paint,",.2f")
format_labour_charges = format(labour_charges,",.2f")
format_total_cost = format(total_cost,",.2f")


#Printing the Outputs
print("Number of paint galons required: ",format_number_of_galons)
print("Labour hours required: ",format_hours_required)
print("Cost of paint: $",format_cost_of_paint,sep = "")
print("Labour Charges: $",format_labour_charges,sep = "")
print("Total cost of paint job: $",format_total_cost,sep = "")
