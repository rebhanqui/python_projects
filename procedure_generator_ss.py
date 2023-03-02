#this program will take in information recieved from customer
#then combine information to print out procedure required depending on input
#to help service agents quickly gather information and share information with customer
#regarding what happens depending on appliance/warranty/etc 
#making calls with issues more seamless and allows customer to tell their story while agent gathers info
#without the need to disturb and ask questions again which frustrates customer

#Author: Rebecca Hannah Quinn 2/3/22

# first input Appliance Brand and Type 
cst_brand = "What brand is the appliance? "
print(cst_brand)
cst_brand_response = input()
appliance_list = ["Hotpoint", "Bosch", "Samsung"]
#is_registered = "Is the appliance registered? "

if cst_brand_response == appliance_list[0:2] :
    print("Is this registered")
# !!!result keeps going to elif result or else result - needs to compare to listed brands
elif cst_brand_response != appliance_list[0:2] :
    print("This product does not require registration")

    #some appliance types are customer only dealings or swapouts - display this
    # if particulars apply


# input Registration
# input Customer details
# if not registered must check if can be registered or if within the first year
    # determined by input of dop or dod or date of install or all
# if registered or within warranty continue
    # separate branch for appliances within 24hrs or new brand depending
# input SN or equivalent
# confirm eircode
# print email body for service call/notes/follow up info and procedure for particular
