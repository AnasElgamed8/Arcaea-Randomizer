import streamlit as st

from Sheet import Sheet
from st_social_media_links import SocialMediaIcons


# Functions
@st.cache_resource
def load_sheet():
    return Sheet()


def difficulty_format(dif: str) -> str:
    return difficulty[dif]


def reset_pool():
    if "chart_pool" in st.session_state:
        del st.session_state["chart_pool"]


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
test_sheet = load_sheet()

left_column, right_column = st.columns(2)
if st.sidebar.toggle("Multi Value Mode", value=True, on_change=reset_pool()):
    min_constant = left_column.number_input(
        "Pick the minimum allowed constant:",
        on_change=reset_pool(),
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
        on_change=reset_pool(),
    )
    size = st.number_input("How many charts do you want?", 1, on_change=reset_pool())
else:
    max_constant = min_constant = left_column.number_input(
        "Pick the constant:",
        step=0.1,
        min_value=1.0,
        max_value=12.0,
        value=1.0,
        key="mini",
        on_change=reset_pool(),
    )
    size = right_column.number_input(
        "How many charts do you want?", 1, on_change=reset_pool()
    )


difficulty = {
    "PST": "Past",
    "PRS": "Present",
    "FTR": "Future",
    "BYD": "Beyond",
    "ETR": "Eternal",
}


if st.sidebar.toggle(
    "Difficulty Selection",
    value=True,
    on_change=reset_pool(),
):
    options = st.pills(
        "Select difficulty:",
        options=difficulty,
        selection_mode="multi",
        default=difficulty,
        format_func=difficulty_format,
        on_change=reset_pool(),
    )
else:
    options = None
# Random mode selection:
true_random = st.sidebar.toggle(
    "True Random Mode",
    value=True,
    help="Whether to allow duplicates across runs",
    on_change=reset_pool(),
)


# Button trigger
if st.button("Randomize!", width="stretch", type="primary"):
    # True random block
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
        # Normal random block
        if (
            "random_pool" not in st.session_state
            or st.session_state["random_pool"] is None
            or st.session_state["random_pool"].empty
        ):
            st.session_state["random_pool"] = test_sheet.random(
                min_constant=min_constant,
                max_constant=max_constant,
                size=size,
                difficulty=options,
            )
        # Outside the condition to persist across reruns
        pool = st.session_state["random_pool"]

        if pool is not None and not pool.empty:
            # Size error handling
            pool_size = len(pool)

            if pool_size < size:
                size = min(size, pool_size)
            sample = pool.sample(n=size)
            st.dataframe(sample, hide_index=True)
            pool.drop(sample.index, inplace=True)
            if pool.empty:
                st.info("You ran out of entries, resetting.")
            else:
                st.info(f"{pool_size} chart(s) left.")


load_icons()
