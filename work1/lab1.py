import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


i=1
fall=None
while i<=31:
    file_name="d:/vuz/andre/dsbd/lab1/doing_data_science/dds_datasets/dds_ch2_nyt/nyt"+str(i)+".csv"
    f1=pd.read_csv(file_name,sep=",")
    f1.count
    f2=pd.concat([fall,f1])
    fall=f2
    f2.count
    i=i+1
fall["Age_group"] = fall["Age"].apply(lambda x:" <18" if x<18 else "18-24"  if x<=24 else "25-34" if x<=34  else "35-44" if x<=44   else "45-54" if x<=54  else "55-64" if x<=64  else "65+")
fall["Women"]=fall["Gender"].apply(lambda x:1-x)
fall["Men"]=fall["Gender"]
fall["People"]=1
print("Розбивка за віком та статтю")
print(fall.groupby(["Age_group","Gender"])["Age"].count())
fall_sum=fall.groupby(["Age_group"], as_index=False).sum()
fall_sum["CAT"]=fall_sum["Clicks"]/fall_sum["Impressions"]*100
diag=fall_sum[["Age_group","Impressions","CAT"]]
print("діаграма - кількість показів та показник переходів ")
print(diag)
print("Мій DataFrame")
print(fall_sum)
fall_gender=fall.groupby(["Age_group","Gender"], as_index=False).sum()

info = fall_gender.iloc[0:20,]
f, (ax1, ax2, ax3,data) = plt.subplots(4, figsize=(12,8))
# matplotlib
ax1.bar(fall_sum.Age_group, fall_sum.Signed_In)
# pandas
fall_sum.plot(x="Age_group", y="CAT", kind="bar", ax=ax2)
# seaborn
#sns.barplot(x=fall_sum.Age_group, y=fall_sum.Impressions, ax=ax3)
sns.lineplot(ax=ax3, x=fall_sum.Age_group, y=fall_sum.Impressions)
sns.lineplot(x = "Age_group", y = "People", data=info, hue="Gender", palette = "Set1")
plt.show()



