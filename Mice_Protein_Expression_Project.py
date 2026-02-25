from ucimlrepo import fetch_ucirepo
# Fetch dataset
mice_protein_expression = fetch_ucirepo(id=342)
# Features (protein expression levels)
X = mice_protein_expression.data.features
# Targets (genotype, treatment, behavior, class)
y = mice_protein_expression.data.targets
# metadata 
# print(mice_protein_expression.metadata)
# variable information 
print(mice_protein_expression.variables)



print(X.shape)
print(X.head())
print(X.isna().sum().head())


df = X.copy() 
#  Drop rows where DYRK1A_N is missing
df = df.dropna(subset=["DYRK1A_N"])


df["DYRK1A_N"] = df["DYRK1A_N"].astype(float)




import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


proteins = ["DYRK1A_N","ITSN1_N","BDNF_N","NR1_N","NR2A_N"]  # أعمدة محددة
expression = df[proteins].iloc[0].apply(pd.to_numeric, errors="coerce").fillna(0)

plt.bar(proteins, expression)
plt.xlabel("Protein")
plt.ylabel("Expression Level")
plt.title("Protein Expression Across Mice (First Mouse)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("protein_expression_Parplot.svg") 
plt.show()



import seaborn as sns # Boxplot comparing protein expression by genotype (Control vs Trisomic) 
sns.boxplot(x="Genotype", y="DYRK1A_N", data=df)  # Using DYRK1A_N for example 
plt.title("Protein Expression by Genotype") 
plt.savefig("protein_expression_boxplot.svg")  # Save as SVG 
plt.show() 



# import plotly.express as px # Interactive scatter plot of protein expression across proteins and genotypes 
# fig = px.scatter(df, x="Genotype", y="DYRK1A_N", color="Treatment",  # Using DYRK1A_N for illustration 
#     title="Interactive Protein Expression Plot") 
# fig.write_html("interactive_expression_plot.html")  # Save as HTML 
# fig.show() 





