import streamlit as st
from streamlit_msal import Msal

#based on https://github.com/WilianZilv/streamlit_msal


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
import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Load the Iris dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Sidebar for parameter selection
st.sidebar.title("Model Parameters")
n_estimators = st.sidebar.slider("Number of estimators", 10, 200, 100, 10)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a RandomForestClassifier
clf = RandomForestClassifier(n_estimators=n_estimators, random_state=42)
clf.fit(X_train, y_train)

# Streamlit app
st.title("Iris Flower Classifier")
st.write("This app classifies Iris flowers into one of three species.")


account = auth_data["account"]
name = account["name"]
username = account["username"]
account_id = account["localAccountId"]

# st.title(account)
# st.title(account_id)
st.write(f"Hello {name}!")
# st.title(username)


# Input fields for features
sepal_length = st.slider("Sepal length (cm)", float(X['sepal length (cm)'].min()), float(X['sepal length (cm)'].max()), float(X['sepal length (cm)'].mean()))
sepal_width = st.slider("Sepal width (cm)", float(X['sepal width (cm)'].min()), float(X['sepal width (cm)'].max()), float(X['sepal width (cm)'].mean()))
petal_length = st.slider("Petal length (cm)", float(X['petal length (cm)'].min()), float(X['petal length (cm)'].max()), float(X['petal length (cm)'].mean()))
petal_width = st.slider("Petal width (cm)", float(X['petal width (cm)'].min()), float(X['petal width (cm)'].max()), float(X['petal width (cm)'].mean()))

# Predict the class
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=X.columns)
prediction = clf.predict(input_data)
prediction_proba = clf.predict_proba(input_data)

# Display results
st.write(f"Predicted class: {iris.target_names[prediction][0]}")
st.write(f"Prediction probabilities: {prediction_proba[0]}")

