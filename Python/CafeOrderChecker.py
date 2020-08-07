# https://www.interviewcake.com/question/python3/cafe-order-checker?course=fc1&section=array-and-string-manipulation
# technique: pointers
# time: O(n)
# space: O(1) no additional space
# edge cases
# 1) either list is empty
# 2) one list is longer than the other
# 3) one list is exhausted before the other

# my solution
def IsFirstComeFirstServed(take_out_orders, dine_in_orders, served_orders):

	takeOut_start_index = 0;
	dineIn_start_index = 0;
	served_orders_index = 0;

	takeOutResult = False
	dineInResult = False

	# can we merge both while loops below?

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

		served_orders_index += 1

	# if the take out orders list is exhausted after completing all served orders
	# then it is first come first served
	if takeOut_start_index >= len(take_out_orders):
		takeOutResult = True

	# if the dine in orders list is exhausted after completing all served orders
	# then it is first come first served
	if dineIn_start_index >= len(dine_in_orders):
		dineInResult = True

	# check take out orders
	#while served_orders_index < len(served_orders):

	#	isTakeOutExhausted = takeOut_start_index >= len(take_out_orders)
		
	#	if not isTakeOutExhausted and served_orders[served_orders_index] == take_out_orders[takeOut_start_index]:
	#		takeOut_start_index += 1

	#	served_orders_index += 1

	#if takeOut_start_index >= len(take_out_orders):
	#	takeOutResult = True

	## check dine in orders	
	#served_orders_index = 0;
	#while served_orders_index < len(served_orders):
				
	#	isDineInExhausted = dineIn_start_index >= len(dine_in_orders)

	#	if not isDineInExhausted and served_orders[served_orders_index] == dine_in_orders[dineIn_start_index]:
	#		dineIn_start_index += 1			

	#	served_orders_index += 1;

	#if dineIn_start_index >= len(dine_in_orders):
	#	dineInResult = True

	#print("takeout:" + str(takeOutResult))
	#print("dinein:" + str(dineInResult))
	return takeOutResult and dineInResult

takeOut = [1, 3, 5]
dineIn = [2, 4, 6]
served = [1, 2, 4, 6, 5, 3]

print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [17, 8, 24]
dineIn = [12, 19, 2]
served = [17, 8, 12, 19, 24, 2]

print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [17]
dineIn = [8]
served = [17, 8]

print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [17]
dineIn = []
served = [17]

print(IsFirstComeFirstServed(takeOut, dineIn, served))

takeOut = [1, 3, 13, 5]
dineIn = [2, 4, 6]
served = [1, 2, 4, 6, 3, 5]

print(IsFirstComeFirstServed(takeOut, dineIn, served))

