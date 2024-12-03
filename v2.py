import sys
import os

# Add the 'scripts' folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, "scripts"))

# Import the required functions
from instagram_lookup import getInfo, advanced_lookup

import streamlit as st

# App Configuration
st.set_page_config(page_title="Instagram User Lookup", layout="wide")

# App Title and Description
st.title("Instagram User Lookup Tool")
st.markdown(
    """
    Welcome to the **Toutatis Instagram User Lookup Tool**.  
    Use the application to gain information related to a person's Instagram Account. 
    Please enter your Instagram Session ID followed by the target's username to begin the process.

    *Do take note that Instagram will detect scraping behaviour if the session ID used for this tool is used often, it is recommended that the user uses a sock puppet account to avoid any issues*
    """
)

# Input Fields
session_id = st.text_input("Session ID", type="password")
username = st.text_input("Instagram Username")

# Fetch Button
if st.button("Fetch Details"):
    if not session_id or not username:
        st.error("Both Session ID and Username are required!")
    else:
        # Fetch Basic Info
        with st.spinner("Fetching user information..."):
            user_info = getInfo(username, session_id)
        
        if user_info["error"]:
            st.error(user_info["error"])
        else:
            user_info = user_info["user"]
            st.success(f"Information retrieved for @{username}")
            
            # Display User Info
            with st.container():
                st.header("User Information")
                st.write(f"**Username:** {user_info['username']}")
                st.write(f"**Full Name:** {user_info['full_name']}")
                st.write(f"**Verified:** {user_info['is_verified']}")
                st.write(f"**Business Account:** {user_info['is_business']}")
                st.write(f"**Private Account:** {user_info['is_private']}")
                st.write(f"**Follower Count:** {user_info['follower_count']}")
                st.write(f"**Following Count:** {user_info['following_count']}")
                st.write(f"**Number of Posts:** {user_info['media_count']}")
                st.write(f"**External URL:** {user_info.get('external_url', 'N/A')}")
                st.write(f"**Biography:** {user_info['biography']}")
            
            # Fetch Advanced Info
            advanced_info = advanced_lookup(username)
            if advanced_info["error"]:
                st.error("Rate limit reached. Please try again later.")
            else:
                with st.container():
                    st.header("Advanced Information")
                    obfuscated_email = advanced_info["user"].get("obfuscated_email", "N/A")
                    obfuscated_phone = advanced_info["user"].get("obfuscated_phone", "N/A")
                    st.write(f"**Obfuscated Email:** {obfuscated_email}")
                    st.write(f"**Obfuscated Phone:** {obfuscated_phone}")

# Footer Section
st.markdown(
    """
    ---
    **© 2024 Instagram User Lookup Tool by sangvis_reaper. All rights reserved.**
    """
)
