import pandas as pd

file_df = pd.read_excel("example.xlsx")

file_df_first_record = file_df.drop_duplicates(subset=["title1", "title2", "title3"], keep="first")
file_df_first_record.to_excel("example_newrecord.xlsx", index=False)
