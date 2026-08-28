import streamlit as st

from Sheet import Sheet
from st_social_media_links import SocialMediaIcons


# Functions
@st.cache_resource
def load_sheet():
    return Sheet()


def difficulty_format(dif: str) -> str:
    return difficulty[dif]


@st.cache_data
def load_icons():
    social_media_links = [
        "https://www.youtube.com/@AnasElgamed",
        "https://www.github.com/AnasElgamed8",
        "https://www.reddit.com/user/Practical_Trouble165",
        "https://www.discord.com/users/anaselgamed",
    ]
    SocialMediaIcons(social_media_links).render(sidebar=True)


# Page

# TODO: Move the about section to a md file

# Set the title and about section
st.set_page_config(
    page_title="Arcaea Randomizer By AnasElgamed8",
    menu_items={
        "About": """Hello! Anas here.
        \nI wrote this app because I was bored (lol)
        \nAnd it's a fun way to implement things I learn along the way.
        \nHope that it improves your Arcaea experience even by a little!
        \nIf you find any errors or have any suggestions. Feel free to open an issue on Github.
        \nOr contact me via Discord [@anaselgamed](https://discordapp.com/users/anaselgamed)"""
    },
)

st.title("Arcaea random chart picker")
st.sidebar.title("Options")

test_sheet = load_sheet()

# TODO: change to the with method
left_column, right_column = st.columns(2)
if st.sidebar.checkbox("Single Value Mode"):
    max_constant = min_constant = left_column.number_input(
        "Pick the constant:",
        step=0.1,
        min_value=1.0,
        max_value=12.0,
        value=1.0,
        key="mini",
    )
    size = right_column.number_input("How many charts do you want?", 1)

else:
    min_constant = left_column.number_input(
        "Pick the minimum allowed constant:",
        step=0.1,
        min_value=1.0,
        max_value=12.0,
        value=1.0,
        key="mini",
    )
    max_constant = right_column.number_input(
        "Pick the maximum allowed constant:",
        step=0.1,
        min_value=min_constant,
        max_value=12.0,
        value=12.0,
        key="maxi",
    )
    size = st.number_input("How many charts do you want?", 1)

difficulty = {
    "PST": "Past",
    "PRS": "Present",
    "FTR": "Future",
    "BYD": "Beyond",
    "ETR": "Eternal",
}


if st.sidebar.checkbox("Difficulty Selection"):
    options = st.pills(
        "Select difficulty:",
        options=difficulty,
        selection_mode="multi",
        default=difficulty,
        format_func=difficulty_format,
    )
else:
    options = None
# Random mode selection:
true_random = st.toggle(
    "True Random Mode", value=True, help="Whether to allow duplicates across runs"
)


# Button trigger
if st.button("Randomize!", width="stretch", type="primary"):
    if true_random:
        st.dataframe(
            test_sheet.true_random(
                min_constant=min_constant,
                max_constant=max_constant,
                size=size,
                difficulty=options,
            ),
            hide_index=True,
        )
    else:
        if "normal_random" in st.session_state:
            pass
        else:
            st.session_state["normal_random"] = test_sheet.random(
                min_constant=min_constant,
                max_constant=max_constant,
                size=size,
                difficulty=options,
            )
            st.dataframe(
                st.session_state["normal_random"],
                hide_index=True,
            )
st.sidebar.divider()
load_icons()
