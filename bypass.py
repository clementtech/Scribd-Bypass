# Import modules
# Pyperclip is used to copy the bypass link to the clipboard
import pyperclip
# Re is used to match the URL format
import re
# Sys is used to exit the program
import sys
# Webbrowser is used to open the link in the default browser
import webbrowser

# Prompt the user for a Scribd URL
url = str(input("Scribd URL: "))

# Define the regex pattern for a valid Scribd URL
# The pattern matches URLs that start with "https://www.scribd.com/document/" followed by 9 digits of document ID and the title name
link_format = r"^https://www.scribd.com/document/[0-9]{9}/.+$"

# Check if the URL matches the defined pattern
if re.match(link_format, url):

    # Extract the document ID from the URL using regex
    document_id = re.split(r"https://www.scribd.com/document/", url)[1]
    document_id = re.split(r"/", document_id)[0]

    # Construct the bypass URL using the extracted document ID
    bypass_url = f"https://www.scribd.com/embeds/{document_id}/content?start_page=1&view_mode=scroll"
    
    # Copy the bypass URL to the clipboard using pyperclip
    pyperclip.copy(bypass_url)
    pyperclip.paste()

    # Print the bypass URL and a message indicating that it has been copied to the clipboard
    print(f"Link copied to clipboard, {bypass_url}")

    # Prompt the user for consent to open the link in their browser
    open_consent = str(input("Do you want to open the link in your browser? (Y/N): ")).capitalize()

    # If the user consents, open the link in the default web browser
    if open_consent == "Y":

        # Open the bypass URL in the default web browser using webbrowser module
        print("Opening link in your default browser...")
        webbrowser.open(bypass_url)
        sys.exit("Link opened in your default browser.")

    # If the user does not consent or enter other input, exit the program
    else:
        sys.exit("Thank you for trying Scribd-Viewer!")

# If the URL does not match the defined pattern, exit the program with an error message
# indicating that the URL is invalid
else:
    sys.exit("Invalid Scribd URL, Please try again.")
