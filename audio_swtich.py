import subprocess
import time

def execute_applescript(script):
    """Execute the given AppleScript and return the output."""
    process = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate(script)
    return output.strip()

def check_active_tab():
    """Check the active tab in Safari or Chrome."""
    script = '''
    tell application "System Events"
        set frontApp to name of first application process whose frontmost is true
    end tell

    if frontApp = "Safari" then
        tell application "Safari"
            set tabName to name of current tab of front window
            return tabName
        end tell
    else if frontApp = "Google Chrome" then
        tell application "Google Chrome"
            set tabName to title of active tab of front window
            return tabName
        end tell
    else
        return "Unknown Application"
    end if
    '''
    return execute_applescript(script)

def control_spotify(play):
    """Control Spotify playback. Play if 'play' is True, else pause."""
    if play:
        action = "play"
    else:
        action = "pause"

    script = f'''
    tell application "Spotify"
        {action}
    end tell
    '''
    execute_applescript(script)

# Periodically check the active tab
while True:
    tab_name = check_active_tab()
    if "YouTube" in tab_name:
        control_spotify(False)  # Pause Spotify
    else:
        control_spotify(True)  # Play Spotify
    time.sleep(1)  # Check every 10 seconds
