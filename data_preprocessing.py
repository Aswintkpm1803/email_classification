import pandas as pd
df=pd.read_csv("spam_classifier_dataset.csv",encoding='latin-1')
print("Columns in dataset:", df.columns)
df=df.iloc[:,[0,1]]
df.columns=["label","message"]
df.dropna()
df['label']=df['label'].map({'ham':0,'spam':1})
df.to_csv("cleaned_spam_classifier_dataset.csv",index=False)
print("Data preprocessing completed. Cleaned dataset saved as 'cleaned_spam_dataset.csv'.")