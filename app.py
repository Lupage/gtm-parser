import pandas as pd
import streamlit as st
import json

json_data = st.file_uploader('File uploader')
json_data = json.load(json_data)

tag_list = json_data['containerVersion']['tag']

tag_id_list = []
tag_type_list = []
tag_name_list = []
parameter_list = []
event_category_list_key = []
event_category_list_value = []
event_action_list = []
event_label_list = []

for element in tag_list:
    if element['type'] == "ua":
    	tag_id_list.append(element['tagId'])
    	tag_type_list.append(element['type'])
    	tag_name_list.append(element['name'])
    	parameter_list.append(element['parameter'])
    for item in element['parameter']:
        if item["key"] == "eventCategory":
        if item["key"] == "eventAction":
            event_action_list.append(item["value"])
        if item["key"] == "eventLabel":
            event_label_list.append(item["value"])

tag_results = zip(tag_id_list, tag_type_list, tag_name_list, parameter_list)
df = pd.DataFrame(tag_results)
df.columns = ["ID", "Type", "Name", "Parameters]

st.table(df)
