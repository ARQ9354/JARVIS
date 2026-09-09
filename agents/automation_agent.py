import subprocess
import webbrowser


def execute_automation(command):
    command = command.lower().strip()

    # Chrome
    if "chrome" in command:
        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )
        return "Chrome opened."

    # Calculator
    elif "calculator" in command or "calc" in command:
        subprocess.Popen("calc.exe")
        return "Calculator opened."

    # YouTube
    elif "youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "YouTube opened."

    else:
        return "I don't know how to perform that action yet."