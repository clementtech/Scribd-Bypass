# Scribd-Bypass
Scribd-Bypass is a Python program designed to help users access Scribd document files for educational purposes in a user-friendly manner.

# Why I created this program.
I created this program during high school when I struggled to access documents required for my studies. Many study materials on Scribd are behind a paywall, making education inaccessible for many students around the world.

This program aims to bridge that gap and provide opportunities for less fortunate students to access study materials to support their education.

# How does it work?

### How normal Scribd document link looks like:
```
https://www.scribd.com/document/{document_id}/{document_title}
```

### What does the program do?
- It extracts the document ID from the provided link.
- It builds a unique URL to access the document.
- Copy the unique URL created and paste it into the user's clipboard.
- The program will then ask the user if they want the program to open the unique URL in their default web browser.

# Sneak Peek:

### Prompt user for Scribd document link:
![image](https://raw.githubusercontent.com/clementtech/Scribd-Bypass/refs/heads/main/assets/prompt_for_url.png)

### Successful converted link and prompt user to open the link in their default web browser:
![image](https://raw.githubusercontent.com/clementtech/Scribd-Bypass/refs/heads/main/assets/success_message.png)

### Success message if the user chooses to open the link in their default web browser:
![image](https://raw.githubusercontent.com/clementtech/Scribd-Bypass/refs/heads/main/assets/open_in_browser_success_message.png)

### If the user chooses not to open the link in their default web browser:
![image](https://raw.githubusercontent.com/clementtech/Scribd-Bypass/refs/heads/main/assets/open_in_browser_decline_message.png)

### Error handling:
![image](https://raw.githubusercontent.com/clementtech/Scribd-Bypass/refs/heads/main/assets/error_handling.png)
In progress ....

# Prerequisites:
- [Python](https://www.python.org/downloads/)

# How to use:
1. Download the project onto your computer.
    - You can download the project by using the [git](https://git-scm.com/downloads) command:
    ```
    git clone https://github.com/clementtech/Scribd-Bypass.git
    ```

2. Download the required dependencies.
    - The dependencies can be installed using the following command:
    ```
    pip install -r requirements.txt
    ```
3. Done setup!
    - You can run the program by entering the following command:
    ```
    python bypass.py
    ```

4. Enter the Scribd document link when prompted.
      - The program will extract the document ID from the provided link and build a unique URL to access the document.
      - The unique URL will be copied to the user's clipboard for easy access.
      - The program will then ask the user if they want the program to open the unique URL in their default web browser.

# Disclaimer:
This program is intended for educational purposes only. The author does not endorse or promote any illegal activities, including bypassing paywalls or accessing copyrighted material without permission. Users are responsible for ensuring that they comply with all applicable laws and regulations regarding the use of this program and the content accessed through it. The author disclaims any liability for any misuse of this program or its consequences.