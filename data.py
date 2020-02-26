import matplotlib.pyplot as plt
girls=[50,20,10]
total=[2,3,4]
boys=[20,30,40]
others=[10,15,20]
activities=['girls','boys','others']
cols=['red','blue','Yellow']
plt.pie(total, labels=activities,
         colors=cols,
         shadow=True,
         startangle=90,
         explode=(0,0.1,0),
         autopct='%1.1f%%')
plt.title('Population in Nepal According to census 2020')
plt.show()
