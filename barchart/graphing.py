import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def main():
    data = pd.read_csv('USA_compulsory_sterilization_totals_years.csv')
    regions = set(data['region'])
    data = [data[data['region'] == region] for region in regions]
    regional_sterilizations = {set(region['region']).pop():region.iloc[:, 5:]
                               for region in data}
    domain = regional_sterilizations['northeast'].shape[1]
    fig = plt.figure
    ax = plt.subplot(111)
    for region, sterilizations in regional_sterilizations.items():
        total_sterilizations = np.asarray(sterilizations.sum(axis=0))
        print(region)
        print(total_sterilizations)
        ax.plot(list(range(1943,domain+1943)), total_sterilizations, label=region)
    ax.legend()
    plt.xticks(list(range(1943,domain+1943)))
    plt.show()
if __name__ == '__main__':
    main()
