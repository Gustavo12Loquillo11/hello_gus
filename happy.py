word = input("Word: ")
# List Comprehension and Print:
print(
    "\n".join(
        [
            "".join(
                [
                    ( 
                        # This ternary operation decides what character to show:
                        #If the (x,y) point lies inside the heart shape (i.e., the heart equation evaluates to True), then it chooses a character from the word based on the index [(x - y) % len(word)].
                        # If the (x,y) point lies outside the heart shape, it displays a space " ".
                        word[(x - y) % len(word)]
                        # The equation used here:
                        if ((x * 0.05) ** 2 + (y * 0.1)**2-1) ** 3 - (x * 0.05)**2*(y * 0.1)
                        ** 3<= 0
                        else " "
                    )
                    for x in range(-30, 30)
                ]
            )
            for y in range(15, -15, -1)
        ]
    )
)
print(f"Happy {word}!!")
# clcoding.com
