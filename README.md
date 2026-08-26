# Arcaea Randomizer

## Introduction

*This is a fun project with a simple task: Giving you a chart to play!*

Arcaea's built-in random button is really limited. Every time I use it I get dissappointed, so I made this small script.

## Features

* Ability to pick a range of CCs to pick from.
* A single value mode, which allows you to pick some reandom charts with the same CC.
* Lets you choose the number of charts to pick at a time.
* Display the note count. along with some other info.

## To Be Added

* Ability to pick the difficulty.
* Ability to use your own dataset with your own score.
* Score and PTT based picks.
* Currently only supports a true-random mode, planning to add another mode that remembers the previous turns to avoid giving you duplicates.
* Other things that I had in mind but forgot about them :P

## Instalation

### 1. Using The Online Version:

You don't really have to install anything. Just use the online version: (Once I'm done making it)

### 2. Clone The Repo:

#### Bash:

```bash
git clone https://github.com/AnasElgamed8/Arcaea-Randomizer
cd Arcaea-Randomizer/
# If you are on Arch, you will have to make a venv
python -m venv .venv
# (Or install packages globaly which is a pain. You can figure that out yourself :D)
source venv/bin/activate
pip install -r requirements.txt
streamlit run src/app.py
```
and then go to http://localhost:8501/ on your web browser (It should've been opened by default)

### 3. Using Docker:

The dockerfile is already included, though I will add some detailed steps later.


## Credits

to be added

## Notes

to be added
