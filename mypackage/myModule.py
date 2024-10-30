def top_n (items, n):
    """Returns the top n items in an array in desc order,
    
    Args:
        items: (array): list of array like object
         n: (int): number of items to return
         
         Returns: array: top n items in an array in desc order
         
         Egs:
            >>> top_n([8,3,2,7,4], 3) 
            [8,7,3]
        """
    
        for i in range(n): # keep sorting until we have the top n items
            for j in range(len(items)-1-i):

                if items[j] > items[j+1]: # if this item is bigger than than next item
                    items[j], items[j+1] = items[j+1], items[j] # swap the two!

        # get last two items
    top_n = items[-n:]

    # returns in descending 
    return top_n[:: - 1 -]