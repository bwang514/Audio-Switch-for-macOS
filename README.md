# Audio Switch for macOS

## Overview
This script is designed to enhance the audio listening experience on a MacBook. It's a Python script that seamlessly integrates with AppleScript to control audio playback, primarily focusing on an automated switch between Spotify and YouTube. When you are using apps other than YouTube, Spotify music plays in the background. As soon as you switch to a YouTube tab, Spotify pauses, allowing for uninterrupted video watching.

### Use Case
This script is useful for those who frequently switch between coding tutorials on YouTube and other tasks. It automates the process of pausing and playing Spotify music, eliminating the need to manually control your music playback every time you switch tabs.

## Features
- **Automatic Playback Control:** Automatically plays Spotify music when not on YouTube and pauses when a YouTube tab is active.
- **Cross-Browser Compatibility:** Works with both Safari and Google Chrome.
- **Continuous Monitoring:** Periodically checks the active browser tab to ensure timely switching of audio playback.

## Prerequisites
- macOS Operating System
- Python 3
- Spotify application installed
- Safari or Google Chrome browser

## Installation and Usage
1. Clone or download the script to your local machine.
2. Open the Terminal and navigate to the directory containing the script.
3. Run the script using the command: `python3 audio_switch.py`
4. The script will run in the background, monitoring your active browser tab.

## Limitations and Future Improvements
- Currently, the script only supports Safari and Google Chrome. Support for other browsers may be added in future updates.
- The script is designed to work with Spotify. Integration with other music apps could be considered for future versions.
- The tab monitoring interval is set to 1 seconds. This can be adjusted for more or less frequent checks.

## Contributing
Feedback and contributions are welcome. If you have ideas on improving this script or want to report a bug, please open an issue or submit a pull request.



Readme written with GPT-4 :) 
