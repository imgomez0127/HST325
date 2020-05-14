import pandas as pd 

acronyms = {
    "Alabama":"AL",
    "Alaska":"AK",
    "Arizona":"AZ",
    "Arkansas":"AR",
    "California":"CA",
    "Colorado":"CO", "Connecticut":"CT",
    "Delaware":"DE",
    "Florida":"FL",
    "Georgia":"GA",
    "Hawaii":"HI",
    "Idaho":"ID",
    "Illinois":"IL",
    "Indiana":"IN",
    "Kansas":"KS",
    "Kentucky":"KY",
    "Louisiana":"LA",
    "Maine":"ME",
    "Maryland":"MD",
    "Massachusetts":"MA",
    "Michigan":"MI",
    "Minnesota":"MN",
    "Mississippi":"MS",
    "Missouri":"MO",
    "Montana":"MT",
    "Nebraska":"NE",
    "Nevada":"NV",
    "New Hampshire":"NH",
    "New Jersey":"NJ",
    "New Mexico":"NM",
    "New York":"NY",
    "North Carolina":"NC",
    "North Dakota":"ND",
    "Ohio":"OH",
    "Oklahoma":"OK",
    "Oregon":"OR",
    "Pennsylvania":"PA",
    "Rhode Island":"RI",
    "South Carolina":"SC",
    "South Dakota":"SD",
    "Tennessee":"TN",
    "Texas":"TX",
    "Utah":"UT",
    "Vermont":"VT",
    "Virginia":"VA",
    "Washington":"WA",
    "West Virginia":"WV",
    "Wisconsin":"WI",
    "Wyoming":"WY",
    "Iowa":"IA"
}
df = pd.read_csv("Unemployment_Data.csv")
print(len(df))
df2 = df.drop(df[df["State/Area"] == "Los Angeles County"].index)
df3 = df2.drop(df2[df2["State/Area"] == "New York city"].index)
df4 = df3.drop(df3[df3["State/Area"] == "District of Columbia"].index)
df5 = df4.drop(df4[df4["Month"] != 1].index)
print(len(df5))
states = df5["State/Area"].map(lambda x: acronyms[x])
print(states)
df5["State/Area"] = states
print(df5)
df5.to_csv("cleaned_unemployment_data.csv",index=False)
