def is_known():
    # Remove the current dictionary from the list
    data_dict.remove(current_card)

    # Optional but recommended for this project:
    # Save the updated list to a new CSV so progress isn't lost!
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)

    # Move to the next card
    next_card()