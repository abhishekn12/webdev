# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import pandas as pd


# %%
import seaborn
import matplotlib


# %%
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')
tips = sns.load_dataset("tips")
tips.head()


# %%
sns.distplot(tips['total_bill'])


# %%



