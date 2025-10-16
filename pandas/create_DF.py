import pandas as pd

column = ["Maria", "Batman", "Spongebob"]
titled_clolumns = {"name": column,
                  "height": [1.17, 1.9, 0.25],
                  "weight": [54, 100, 1]}
data = pd.DataFrame(titled_clolumns)
select_column = data["weight"][1]
select_row = data.iloc[1][1]
print(select_row)