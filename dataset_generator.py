import pandas as pd
from crisis_dataset import crisis_data

df = pd.DataFrame(crisis_data)
df.to_csv("crisis_dataset.csv", index=False)
print("✅ CSV exported successfully")
