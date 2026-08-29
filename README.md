# Arcaea Randomizer

## Introduction

*This is a fun project with a simple task: Giving you a chart to play!*

Arcaea's built-in random button is really limited. Every time I use it I get disappointed, so I made this small script.

## Features

* Ability to pick a range of CCs to pick from.
* A single value mode, which allows you to pick some random charts with the same CC.
* Lets you choose the number of charts to pick at a time.
* Display the note count. along with some other info.

## Other Planned Features

- [X] Ability to pick the difficulty.
- [X] No-duplicates mode (Turn true random off)
- [ ] Ability to use your own dataset with your own score.
- [ ] Score and PTT based picks.
- [ ] Cool Arcaea themed backgrounds (When I eventually learn to draw lol)
* Other things that I had in mind but forgot about them :P

## Installation

### 1. Using The Online Version:

You don't really have to install anything. Just use the [online version](https://arcaea.anas-elgamed.duckdns.org/)

- The only case where the online version might not be suitable for you would be: 
restricting the selection pool to only owned charts

In that case, you should do the following:

1. Clone the repo as instructed below.
2. Replace the spreadsheet link with a link to your own spreadsheet with only your owned charts.

### 2. Clone The Repo:

#### Bash:

```bash
git clone https://github.com/AnasElgamed8/Arcaea-Randomizer
cd Arcaea-Randomizer/
# If you are on Arch, you will have to make a venv
python -m venv .venv
source .venv/bin/activate
# (Or install packages globally which is a pain. You can figure that out yourself :D)
pip install -r requirements.txt
streamlit run src/app.py
```
and then go to http://localhost:8501/ on your web browser (It should've been opened by default)

### 3. Using Docker:

The dockerfile is already included, though I will add some detailed steps later.


## Credits

- [@ayatough](https://github.com/ayatough) for their [VScode Arcaea theme](https://github.com/ayatough/vscode-arcaea-theme/) (That's where I got the colors).
- [u/Chibu68_](https://www.reddit.com/user/Chibu68_/) for their [Arcaea B30 Calculator (community) V2](https://docs.google.com/spreadsheets/d/1RJkupRtpRxxrTrMpb0VwCLZzOU0JtX_jsuo8xUnEO1k/edit?usp=sharing) spreadsheet.
- hokandor7 for the making the original spreadsheet.
## Notes

Feel free to open a pull request if you have anything you want to add.

Or clone the repo and experiment however you like!

AI usage on anything related to this project is not allowed (Even though I can't really prevent you. But I'd appreciate it if you respect my wishes!)
