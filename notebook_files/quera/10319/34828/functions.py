import numpy as np
import pandas as pd
def survival_chance(titanic_df,start_age,end_age):
    titanic_df.Age = titanic_df.Age[~titanic_df.Age.isna()]
    titanic_df['Survived'] = titanic_df['Survived'][~titanic_df.Survived.isna()]
    titanic_df['Sex'] = titanic_df['Sex'][~titanic_df.Sex.isna()]
    titanic_df = titanic_df[['PassengerId','Survived','Sex','Age']]
   
    #Male Survival
    male_survival = titanic_df[(titanic_df.Age>= start_age) & (titanic_df.Age<= end_age)]
    male_survival = male_survival[male_survival.Sex == 'male']
    count_survived = 0
    if len(male_survival):
        for i in male_survival.Survived:
            if i:
                count_survived +=1
        male = count_survived / len(male_survival)
    else:
        male = -1
        
    #FEmale Survival
    female_survival = titanic_df[(titanic_df.Age>= start_age) & (titanic_df.Age<= end_age)]
    female_survival = female_survival[female_survival.Sex == 'female']
    count_survived = 0
    if len(female_survival):
        for i in female_survival.Survived:
            if i:
                count_survived +=1
        female = count_survived / len(female_survival)
    else:
        female = -1
    return {'male':round(male,3),'female':round(female,3)}
        
    
        
    