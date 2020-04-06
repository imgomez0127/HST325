import pandas as pd
import re
import json
def make_categorical(df, column):
    categories = set(df[column])
    category_map = {category:i for i,category in enumerate(categories)}
    column = list(df[column])
    categorical_column = [category_map[category] for category in column]
    df = df.replace(to_replace=column, value=categorical_column)
    return df,category_map

def replace_numeral(column):
    numbers = re.compile("[0-9]+")
    lst = []
    for item in column:
        if isinstance(item, str):
            indices = numbers.search(item).span()
            if indices:
                number = int(item[indices[0]:indices[1]])
                lst.append(number)
            else:
                lst.append(73)
        else:
            lst.append(item)
    return lst

def replace_mean_radius(column):
    numbers = re.compile("[0-9|.|-]")
    plus_equals = re.compile("±")
    new_col = []
    for item in column:
        item = str(item)
        plus_equals_location = plus_equals.search(item)
        if plus_equals_location:
            indices = plus_equals_location.span()
            item = item[0:indices[1]]
        nums = numbers.findall(item)
        new_col.append(float("".join(nums)))
    return new_col

def new_col(column):
    return [1 if 'r' in str(item) else 0 for item in column]

def main():
    columns_to_change = ["Parent", "Name", "Notes", "Discovered by"]
    dataset = pd.read_csv("test.csv")
    dataset = dataset.drop(["Ref(s)"], axis=1)
    for  column in columns_to_change:
        dataset, category_map = make_categorical(dataset, column)
        with open(column+".json","w") as f:
            json.dump(category_map,f)
    numerals = replace_numeral(dataset["Numeral"])
    original_nums = list(dataset["Numeral"])
    dataset = dataset.replace(to_replace=original_nums, value=numerals)
    mean_radius = replace_mean_radius(dataset["Mean radius (km)"])
    original_r = list(dataset["Mean radius (km)"])
    dataset = dataset.replace(to_replace=original_r, value=mean_radius)
    sidereal = replace_mean_radius(dataset["Sidereal period (d) (r = retrograde)"])
    original_s = list(dataset["Sidereal period (d) (r = retrograde)"])
    dataset = dataset.replace(to_replace=original_s, value=sidereal)
    axis = replace_mean_radius(dataset["Semi-major axis (km)"])
    original_a = list(dataset["Semi-major axis (km)"])
    dataset = dataset.replace(to_replace=original_a, value=axis)
    sidereal_during_retrograde = new_col(dataset["Sidereal period (d) (r = retrograde)"])
    dataset["Is sidereal during retrograde"] = sidereal_during_retrograde
    print(dataset)
    dataset.to_csv("dataset.csv",index=False)
if __name__ == "__main__":
    main()
