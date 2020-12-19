import pandas as pd


def min_points(df_laliga,season):
    laliga = df_laliga[['season','club','points']]
    laligaSeason = laliga.loc[laliga['season']==season]
    ans = laligaSeason[laligaSeason.points == laligaSeason.points.min()]
    ans = ans[['club','points']]
    ans = ans.to_dict('r')
    ans = ans[0]
    return ans
    
    
    
       
def max_points(df_laliga,season):
    laliga = df_laliga[['season','club','points']]
    laligaSeason = laliga.loc[laliga['season']==season]
    ans = laligaSeason[laligaSeason.points == laligaSeason.points.max()]
    ans= ans[['club','points']]
    ans= ans.to_dict('r')
    ans = ans[0]
    return ans
