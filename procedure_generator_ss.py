#this program will take in information recieved from customer
#then combine information to print out procedure required depending on input
#to help service agents quickly gather information and share information with customer
#regarding what happens depending on appliance/warranty/etc 
#making calls with issues more seamless and allows customer to tell their story while agent gathers info
#without the need to disturb and ask questions again which frustrates customer

#Author: Rebecca Hannah Quinn 2/3/22


# first input Appliance Brand and Type 
# change to while loop ref https://stackoverflow.com/questions/66409689/compare-user-input-with-a-list-in-python
appliance_list = ["Hotpoint", "Bosch", "Samsung"]
customer_issue = True

while customer_issue:
    cst_appliance_brand = input("What Brand is the Appliance? ")
    cst_registered = "Is the appliance Registered? "
    cst_unregistered = "Product does not need registration"
    for elements in appliance_list:
        if cst_appliance_brand in appliance_list:
            print(input(cst_registered))
            break
        else:
            print(cst_unregistered)
            break

unregistered_cst = ["No", "N"]
registered_cst = ["Yes", "Y"]
if cst_unregistered == unregistered_cst :
    #customer information collected previously can be {} added below
    print(input("Provide customer with the following information: "))

elif cst_registered == registered_cst :
    print(input("Log Service Call with the following information: "))

else :
    print("Further information required to determine solution")

# code now asks for yes or no answer if registered and goes through a while loop

# input Registration
  #  print("This product does not require registration")

    #some appliance types are customer only dealings or swapouts - display this
    # if particulars apply
# input Customer details
# if not registered must check if can be registered or if within the first year
    # determined by input of dop or dod or date of install or all
# if registered or within warranty continue
    # separate branch for appliances within 24hrs or new brand depending
# input SN or equivalent
# confirm eircode
# print email body for service call/notes/follow up info and procedure for particular
