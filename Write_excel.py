import pandas as pd

df = pd.read_excel(r"write_2.xlsx")

word = "leben"
character = "(v)"
meaning = "生活"
dataframe = pd.DataFrame([[word, character, meaning]], columns=["word", "character", "meaning"])

df_new = df.append(dataframe, ignore_index=True)
print(df_new)
df_new.to_excel(r"write_2.xlsx", sheet_name="Sheet2", index=False, engine="openpyxl")
