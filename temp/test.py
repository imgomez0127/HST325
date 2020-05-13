import pandas as pd

if __name__ == "__main__":
    df = pd.read_csv("NYC_Wi-Fi_Hotspot_Locations.csv")
    providers = df["Provider"]
    mapping = {provider:i for i, provider in enumerate(set(providers))}
    all_providers = [mapping[provider] for provider in providers]
    print("HELLO")
    print(max(all_providers))
    df["ProviderClass"] = all_providers
    YearActivated = [date[-4:] for date in df["Activated"]]
    df["YearActivated"] = YearActivated
    print(df)
    print(set(providers))
    print(set(df["Type"]))
    print(set(df["Activated"]))
    print(set(YearActivated))
