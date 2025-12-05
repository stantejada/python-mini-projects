import pandas as pd

data = pd.read_csv("data.csv")

filtered_data = data[data["Primary Fur Color"].isin(["Gray", "Cinnamon", "Black"])]

color_counts = filtered_data["Primary Fur Color"].value_counts()

new_df = pd.DataFrame({
    "Fur Color" : color_counts.index,
    "Count" : color_counts.values
})

print(new_df)
