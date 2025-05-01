import pyperclip
import re
import sys
import webbrowser

url = str(input("Scribd URL: "))

link_format = r"^https://www.scribd.com/document/[0-9]{9}/.+$"

if re.match(link_format, url):

    document_id = re.split(r"https://www.scribd.com/document/", url)[1]

    document_id = re.split(r"/", document_id)[0]


    bypass_url = f"https://www.scribd.com/embeds/{document_id}/content?start_page=1&view_mode=scroll"
    
    pyperclip.copy(bypass_url)
    pyperclip.paste()

    print(f"Link copied to clipboard, {bypass_url}")


    open_consent = str(input("Do you want to open the link in your browser? (Y/N): ")).capitalize()


    if open_consent == "Y":
        webbrowser.open(bypass_url)
        sys.exit("Link opened in your default browser.")

    else:
        sys.exit("Thank you for trying Scribd-Viewer!")

else:
    sys.exit("Invalid Scribd URL, Please try again.")
