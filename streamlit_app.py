import streamlit as st
import main_functions
import requests

st.title("Detect languages")
st.header("Please type a sentence in any language")

lang_list = main_functions.read_from_file("lang_list.json")

sent = st.text_input("Enter sentence")

if sent:
    sent=sent.replace(" ", "+")

    api_key=main_functions.read_from_file("api_key.json")
    my_key=api_key["my_key"]

    url = "https://ws.detectlanguage.com/0.2/detect?q=" + sent + "&key=" + my_key

    response = requests.get(url).json()


    conf = 10000
    lang = ""
    for i in response["data"]["detections"]:
        if i['confidence'] < conf:
            conf, lang = i['confidence'], i['language']

    for i in lang_list:
        if i["code"]==lang:
            lang = i["name"].title()

    st.text("{0} with {1} confidence.".format(lang,conf))

