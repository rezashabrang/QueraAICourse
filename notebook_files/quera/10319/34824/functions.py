def get_season_table(df_laliga,season_name):
    seasonTable = df_laliga[df_laliga['season'] == season_name]
    seasonTable = seasonTable.sort_values(['points','goal_difference'],ascending = False)
    return seasonTable