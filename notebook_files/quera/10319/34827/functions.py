def is_normal(boys_df,girls_df,age_in_days,height_in_cm,gender):
    if gender =='male':
        findRow = boys_df.loc[age_in_days]
        if height_in_cm >= findRow['P15'] and height_in_cm < findRow['P85']:
            return True
        else:
            return False
    else:
        findRow = girls_df.loc[age_in_days]
        if height_in_cm >= findRow['P15'] and height_in_cm < findRow['P85']:
            return True
        else:
            return False
