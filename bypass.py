# Sample URL: https://www.scribd.com/document/441480158/User-Manual-for-LED-Digital-Clock

# Define main function to use self defined function for code testing
def main():

    # Creates a loop to repeat asking user if input is not a valid document link
    while True:

        # If it's a valid document link
        try:

            # 1. Receive link from the user input
            # 2. Convert it to string
            # 3. Bypass function to convert URL into bypass paywall URL
            # 4. Print the new link out with the "Enjoy: " word infront
            print("Enjoy:" , bypass(str(input("Scribd URL: "))))

            # If everything is done, which means no error/valid url
            # Stops the loop and the program will stop functioning
            break

        # If user input not a valid Scribd document id
        except IndexError:

            # Tells the user to input a valid document link
            print("Please enter a valid Scribd Document URL")

        # If control-d is inputted, stop the function
        except EOFError:
            break

# Define new bypass function to remove paywall
def bypass(id):

    # Receive the document id number by spliting everything and only select the number
    id = id.split("/")[4]

    # Return the new URL with paywall bypassed
    return f"https://www.scribd.com/embeds/{id}/content?start_page=1&view_mode=scroll"

# Only run this function if it is intended to do so
if __name__ == "__main__":
    main()
