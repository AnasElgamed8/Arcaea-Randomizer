import streamlit as st

from Sheet import Sheet
from st_social_media_links import SocialMediaIcons


# Functions
@st.cache_resource
def load_sheet() -> Sheet:
    """Imports the sheet, about and the random functions"""
    return Sheet()


def difficulty_format(dif: str) -> str:
    """Formats the difficulty options (FTR -> Future)"""
    return difficulty[dif]


def reset_pool():
    """Empties the charts pool to not affect the other queries"""
    if "chart_pool" in st.session_state:
        del st.session_state["chart_pool"]


@st.cache_data
def load_icons():
    """Loads my social media icons and links"""
    social_media_links = [
        "https://www.youtube.com/@AnasElgamed",
        "https://www.github.com/AnasElgamed8",
        "https://www.reddit.com/user/Practical_Trouble165",
        "https://www.discord.com/users/anaselgamed",
    ]
    SocialMediaIcons(social_media_links).render(sidebar=True)


@st.cache_data
def about() -> str:
    """Loads the about section"""
    return data.about


# Page

data = load_sheet()

# Set the title and about section
st.set_page_config(
    page_title="Arcaea Randomizer By AnasElgamed8",
    menu_items={"About": about()},
)

st.title(
    "Arcaea random chart picker",
    text_alignment="center",
    help="Expand the sidebar for more options!",
)

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
    "INS": "Inscribed",
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
    if not options:
        options = "The user is an idiot"
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
    if options == "The user is an idiot":
        st.error("Select a difficulty or disable difficulty selection.")
    # True random block
    elif true_random:
        st.dataframe(
            data.true_random(
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
            st.session_state["random_pool"] = data.random(
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

st.sidebar.divider()
with st.sidebar.expander("About this project"):
    st.markdown(about(), text_alignment="center")

st.sidebar.markdown("Free Palestine 🇵🇸", text_alignment="center")

load_icons()
