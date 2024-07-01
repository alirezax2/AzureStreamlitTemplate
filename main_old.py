
import streamlit as st
from streamlit_msal import Msal


# Azure AD app credentials
# TENANT_ID = "your-tenant-id"
# CLIENT_ID = "your-client-id"
# CLIENT_SECRET = "your-client-secret"
# AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
# SCOPE = ["User.Read"]

from appconfig import TENANT_ID, CLIENT_ID, CLIENT_SECRET,AUTHORITY , SCOPE

with st.sidebar:
    auth_data = Msal.initialize_ui(
        client_id=CLIENT_ID,
        authority=AUTHORITY,
        scopes=[], # Optional
        # Customize (Default values):
        connecting_label="Connecting",
        disconnected_label="Disconnected",
        sign_in_label="Sign in",
        sign_out_label="Sign out"
    )

if not auth_data:
    st.write("Authenticate to access protected content")
    st.stop()

st.write("Protected content available")