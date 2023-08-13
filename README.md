# Automated Fishing Script

This script provides automated mouse and keyboard actions to simulate fishing in the roblox game Fishing Simulator. It uses image recognition to detect fish and air bubbles on the screen and performs actions accordingly.

## Features

-   Simulates mouse clicks and movements.
-   Detects fish and air bubbles using pixel color recognition.
-   Randomized click timings to simulate human-like interactions.
-   Keeps track of the number of fish caught.
-   Exits when the inventory is full.

## Prerequisites

-   Python 3.8

## Installation

1. Clone the repository:

```
git clone https://github.com/Luois45/roblox-fishing-simulator-bot.git
```

2. Navigate to the project directory:

```
cd roblox-fishing-simulator-bot
```

3. Install the required packages:

```
pip install -r requirements.txt
```

## Usage

1. Start the roblox game Fishing Simulator
2. Position the game window such that the script can detect the necessary pixels (Fullscreen is recommended on a 1920x1080 screen)
3. Run the script:

```
python fishing_script.py
```

4. The script will start simulating fishing actions. Press 'q' to stop the script.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the AGPL-3.0 License - see the [LICENSE](LICENSE) file for details.
