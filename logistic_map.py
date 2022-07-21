import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame()
pops = np.linspace(0, 1, 11)
r_list = np.linspace(0, 5, 1000)
df['g_rate'] = r_list

pops = list(pops)[1:-1]

for pop in pops:
    cont = list()
    for r in r_list:
        t = 0
        x = pop
        while t < 1000:
            x = r*x*(1-x)
            t += 1
        cont.append(x)
    df[pop] = cont

plt.clf()

for data in df.columns:
    if data == 'g_rate':
        continue
    plt.scatter(df['g_rate'], df[data], marker='.', color= 'black')

plt.show()