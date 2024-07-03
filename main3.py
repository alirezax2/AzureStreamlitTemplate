# https://github.com/mstaal/streamlit_msal_sample/blob/main/app/dashboard.py#L1

import streamlit as st

from msal_streamlit_authentication import msal_authentication

from appconfig import TENANT_ID, CLIENT_ID, CLIENT_SECRET,AUTHORITY , SCOPE

value = msal_authentication(
    auth={
        "clientId": CLIENT_ID,
        "authority": AUTHORITY,
        "redirectUri": "/",
        "postLogoutRedirectUri": "/"
    },
    cache={
        "cacheLocation": "sessionStorage",
        "storeAuthStateInCookie": False
    },
    login_request={
        "scopes": [f"{CLIENT_ID}/.default"]
    },
    key=1)
st.write("Received", value)