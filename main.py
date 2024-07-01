
import streamlit as st
import msal
from msal import ConfidentialClientApplication
import requests

from appconfig import TENANT_ID, CLIENT_ID, CLIENT_SECRET,AUTHORITY , SCOPE

# Azure AD app credentials
# TENANT_ID = "your-tenant-id"
# CLIENT_ID = "your-client-id"
# CLIENT_SECRET = "your-client-secret"
# AUTHORITY = f"https://login.microsoftonline.com/{TENANT_ID}"
# SCOPE = ["User.Read"]

# Initialize MSAL client
msal_client = msal.ConfidentialClientApplication(
    CLIENT_ID,
    authority=AUTHORITY,
    client_credential=CLIENT_SECRET
)

REDIRECT_URI = "refactored-system-r4gj6677jq3p7qr-8501.app.github.dev"

def get_auth_url():
    return msal_client.get_authorization_request_url(SCOPE, redirect_uri=REDIRECT_URI)

def get_token(auth_code):
    result = msal_client.acquire_token_by_authorization_code(auth_code, SCOPE, redirect_uri=REDIRECT_URI)
    return result.get("access_token")

def is_user_in_group(access_token, user_id, group_id):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    response = requests.get(
        f"https://graph.microsoft.com/v1.0/users/{user_id}/memberOf",
        headers=headers
    )
    if response.status_code == 200:
        groups = response.json().get("value", [])
        return any(group["id"] == group_id for group in groups)
    return False

def main():
    st.title("Azure AD Login")

    if "access_token" not in st.session_state:
        auth_url = get_auth_url()
        st.write("Please login using the following URL:")
        st.write(auth_url)
        auth_code = st.text_input("Enter the authorization code:")
        if auth_code:
            access_token = get_token(auth_code)
            if access_token:
                st.session_state.access_token = access_token
                st.experimental_rerun()
            else:
                st.error("Failed to obtain access token.")
    else:
        # Get user information
        headers = {
            "Authorization": f"Bearer {st.session_state.access_token}",
            "Content-Type": "application/json"
        }
        response = requests.get("https://graph.microsoft.com/v1.0/me", headers=headers)
        if response.status_code == 200:
            user_info = response.json()
            user_id = user_info.get("id")
            user_name = user_info.get("displayName")

            if is_user_in_group(st.session_state.access_token, user_id, GROUP_ID):
                st.success(f"Welcome, {user_name}! You are authorized to use this app.")
                # Add your app functionality here
            else:
                st.error("You are not authorized to use this app.")
        else:
            st.error("Failed to retrieve user information.")

        if st.button("Logout"):
            del st.session_state.access_token
            st.experimental_rerun()

if __name__ == "__main__":
    main()