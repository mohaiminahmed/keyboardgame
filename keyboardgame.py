import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Keyboard Game",
    layout="wide"
)

# Dictionary of keys and their positions
keyboard_layout = [
    ["`", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "=", "<"],
    ["Tab", "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "[", "]", "\\"],
    ["CapsLock", "A", "S", "D", "F", "G", "H", "J", "K", "L", ";", "'", "Enter"],
    ["Shift-Left", "Z", "X", "C", "V", "B", "N", "M", ",", ".", "/", "Shift-Right"],
    ["Space"]
]

# Store the current pressed key
if "pressed_key" not in st.session_state:
    st.session_state.pressed_key = ""

# Function to display the keyboard and trigger action on key press
def display_keyboard():
    for row in keyboard_layout:
        cols = st.columns([1]*len(row))  # Create columns for each key in the row, adjust size for better spacing
        for i, key in enumerate(row):
            display_key = key.split('-')[0]  # Display "Shift" instead of "Shift-Left"/"Shift-Right"
            if cols[i].button(f"{display_key}", key=f"{key}", use_container_width=True):
                # Update the pressed key and trigger the popup immediately
                st.session_state.pressed_key = display_key  # Update the session state with the clicked key

# Display the keyboard and trigger actions
display_keyboard()

# Show the popup with the pressed key
if st.session_state.pressed_key:
    # Display the pressed key in large format
    st.markdown(f"<h1 style='font-size: 300px; text-align: center;'>{st.session_state.pressed_key}</h1>", unsafe_allow_html=True)
