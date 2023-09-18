import pyreadstat
import pandas as pd
import json

# ---- Display Options ----
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# ---- Read the .sav file ----
df, _ = pyreadstat.read_sav("data\\gss\\ZA7500_v5-0-0.sav")
norwegian_df = df[df['country'] == 578]

# ---- Load the schema ----
with open("data\\gss\\data.json", "r", encoding='utf8') as file:
    schema = json.load(file)

# ---- Process data based on schema ----
result = {}

for col in norwegian_df.columns:
    if col in schema:  
        counts = norwegian_df[col].value_counts()
        percentage_distribution = (counts / len(norwegian_df)) * 100
        
        question_text = list(schema[col].keys())[0]
        mapped_distribution = {
            schema[col][question_text][str(index)]: value 
            for index, value in percentage_distribution.items() 
            if str(index) in schema[col][question_text]
        }
        result[col] = {question_text: mapped_distribution}

transformed_data = {
    f"{question} Gi kort! begrunnelse og velg et av Alternativer NB! Du må velge kun ett alternativ fra listen :{list(answers.keys())}": answers 
    for v_data in result.values() 
    for question, answers in v_data.items()
}

# ---- Display Results ----
for key, value in result.items():
    print(key, value)
print(transformed_data)

# ---- Save to JSON file ----
with open('data\\gss\\survey.json', 'w', encoding='utf8') as outfile:
    json.dump(transformed_data, outfile, indent=4, ensure_ascii=False)
