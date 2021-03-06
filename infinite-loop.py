# Motive: to learn how to harness the power of infinite loops

# Task: Take input from user and keep asking for more inputs till the user deny to answer.


# Infinite Loop

while True:
    name = input("Enter your name: ")
    mobile_no = int(input("Enter your number: "))

    # now we need to write the data to file

    # opening the file
    phone_book = open("phonebook.csv", "a+")

    # appending in the file
    # we need to pass placeholders, i.e
    # %s to accept the string(name)
    # %d to accept the digits(mobile number)
    # a % sign to create division, because comma will separate values and write() only takes one argument
    phone_book.write("\n%s, %d" % (name, mobile_no))

    should_continue = input("Dou you want to continue? (Y/N)")
    if (should_continue == "N" or should_continue == "n"):
        phone_book.close()
        break
print("You opt to exit the program")
