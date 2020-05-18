def remove_duplicates_from_sorted_array(arr):
    """
    remove duplicates from sorted array.

    The algorithm I am thinking of is that we start iterating through the array,
    and keep a variable keeping track of the last valid element, so that we have something
    to compare the current element with.

    initially, when we start the loop, our variable to compare with is the first element.

    however, before comparing any element, we should see if there's a None element in the
    list that we previously set. If there is, first we place the current element in that None
    spot in the list, and make the current element None.

    """
    if len(arr) > 1:
        element_to_compare_with = 0
        none_element = None

        for x in range(1, len(arr)):
            current_valid_index = x
            if none_element: # handle the case, first we have to make a swap with the none
                # element.
                arr[none_element] = arr[x]
                current_valid_index = none_element
                arr[x] = None

            if arr[current_valid_index] == arr[element_to_compare_with]:
                arr[current_valid_index] = None
                none_element = current_valid_index

            else:
                element_to_compare_with += 1

                if none_element:
                    none_element += 1