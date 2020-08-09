# https://www.interviewcake.com/question/python3/cafe-order-checker?course=fc1&section=array-and-string-manipulation
# technique: pointers
# time: O(n)
# space: O(1) additional space
# edge cases
# 1) either list is empty
# 2) one list is longer than the other
# 3) one list is exhausted before the other

# Bonus:
# This assumes each customer order in served_orders is unique. How can we adapt this to handle lists of customer orders with potential repeats?
# Our implementation returns True when all the items in dine_in_orders and take_out_orders are first-come first-served in served_orders and False otherwise. That said, it'd be reasonable to raise an exception if some orders that went into the kitchen were never served, or orders were served but not paid for at either register. How could we check for those cases?
# Our solution iterates through the customer orders from front to back. Would our algorithm work if we iterated from the back towards the front? Which approach is cleaner?

# my solution
def IsFirstComeFirstServed(take_out_orders, dine_in_orders, served_orders):

	takeOut_start_index = 0;
	dineIn_start_index = 0;
	served_orders_index = 0;

	takeOutResult = False
	dineInResult = False

	# BONUS: a dictionary to track order count
	# O(n + m) additional space
	# O(n) lookup
	served_orders_dict = {}
	requested_orders_dict = {}

	# populate dict of served orders
	for i in served_orders:
		if i not in served_orders_dict:
			served_orders_dict[i] = 1 # if first key value, initialize with 1
		else:
			served_orders_dict[i] += 1 # if existing key value, increment count

	# check take out not served
	# populate requested orders count dict
	for t in take_out_orders:
		if t not in served_orders_dict:
			raise Exception("Take out order not served!")
		elif t not in requested_orders_dict:
			requested_orders_dict[t] = 1
		else:
			requested_orders_dict[t] += 1


	# check dine in not served
	for d in dine_in_orders:
		if d not in served_orders_dict:
			raise Exception("Dine in not served!")
		elif d not in requested_orders_dict:
			requested_orders_dict[d] = 1
		else:
			requested_orders_dict[d] += 1

	# check orders served but not paid
	for o in served_orders_dict:
		if o not in requested_orders_dict:
			raise Exception("Order served but not paid for!")

	while served_orders_index < len(served_orders):

		isTakeOutExhausted = takeOut_start_index >= len(take_out_orders)
		isDineInExhausted = dineIn_start_index >= len(dine_in_orders)

		# If we still have orders in take_out_orders
        # and the current order in take_out_orders is the same
        # as the current order in served_orders
		if (not isTakeOutExhausted and served_orders[served_orders_index] == take_out_orders[takeOut_start_index]):
			takeOut_start_index += 1
		# If we still have orders in dine_in_orders
        # and the current order in dine_in_orders is the same
        # as the current order in served_orders
		elif (not isDineInExhausted and served_orders[served_orders_index] == dine_in_orders[dineIn_start_index]):
			dineIn_start_index += 1
		# if this is a repeat order, continue to the next order
		elif served_orders_index > 1 and served_orders[served_orders_index] == served_orders[served_orders_index - 1]:
			served_orders_index += 1
			continue
		# If the current order in served_orders doesn't match the current
        # order in take_out_orders or dine_in_orders, then we're not serving first-come,
        # first-served.
		else:
			return False;

		served_orders_index += 1

	# Check for any extra orders at the end of take_out_orders or dine_in_orders
	if takeOut_start_index != len(take_out_orders) or dineIn_start_index != len(dine_in_orders):
		return False;

	return True;

takeOut = [1, 3, 5]
dineIn = [2, 4, 6]
served = [1, 2, 4, 6, 5, 3]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [17, 8, 24]
dineIn = [12, 19, 2]
served = [17, 8, 12, 19, 24, 2]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [17]
dineIn = [8]
served = [17, 8]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [17]
dineIn = []
served = [17]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [1, 3, 13, 5]
dineIn = [2, 4, 6]
served = [1, 2, 4, 6, 3, 5]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

# must return True (repeat order)
takeOut = [17, 8, 24]
dineIn = [12, 19, 2]
served = [17, 8, 12, 19, 19, 24, 2]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

# take out not served
takeOut = [17, 8, 24, 9]
dineIn = [12, 19, 2]
served = [17, 8, 12, 19, 24, 2]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

# dine in not served
takeOut = [17, 8, 24]
dineIn = [12, 19, 2, 10]
served = [17, 8, 12, 19, 24, 2]

# print(IsFirstComeFirstServed(takeOut, dineIn, served))

# case order served but not paid for in either register
# should throw an exception
takeOut = [17, 8, 24]
dineIn = [12, 19, 2]
served = [17, 20, 8, 12, 19, 24, 2]

print(IsFirstComeFirstServed(takeOut, dineIn, served))

