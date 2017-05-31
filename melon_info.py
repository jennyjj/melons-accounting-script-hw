
from melons import melons

def print_out_melon_info(melons):
    """Print out all the melons in our inventory."""

    additional_info = (raw_input("Do you have additional things to track? ")).lower()
    if additional_info == "yes":
        melon = raw_input("Which melon is it for? ")
        characteristic = raw_input("What is the new characteristic? ")
        additional_value = raw_input("What is the value of this new characteristic? ")
        melons[melon][characteristic] = additional_value   

    for melon, characteristics in melons.items():
        print melon.upper()
        for characteristic, value in characteristics.items():
            print "{}: {}".format(characteristic, value)    
        print  

print_out_melon_info(melons)



# def print_melon(name, seedless, price):
#     """Print each melon."""

#     have_or_have_not = 'have'
#     if seedless:
#         have_or_have_not = 'do not have'

#     print "{}s {} seeds and are ${:.2f}".format(name, have_or_have_not, price)


# for i in melon_names:
#     print_melon(melon_names[i], melon_seedlessness[i], melon_prices[i])
