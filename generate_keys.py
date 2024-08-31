import pickle
from pathlib import Path

import streamlit_authenticator as stauth 

names = ["Aritra Ghosh", "hello", "hehe hehe"]
usernames = ["aritrag1905@gmail.com", "hello@gmail.com", "soclicheobelisk@gmail.com"]
passwords = ["XXXX", "XXXX", "XXXX"]

hashed_passwords = stauth.Hasher(passwords).generate()

file_path = Path(__file__).parent / "hashed_pw.pkl"

with file_path.open("wb") as file:
    pickle.dump(hashed_passwords, file)