import pandas as pd
import time

class NJCleaner():
    def __init__(self, path: str) -> None:
        self.data = pd.read_csv(path)

    def order_by_scheduled_time(self) -> pd.core.frame.DataFrame:
        ordered = self.data.sort_values(by=['scheduled_time'])
        return ordered

    def drop_columns_and_nan(self) -> pd.core.frame.DataFrame:
        dropped = self.data.drop(['from'], axis=1)
        dropped = dropped.drop(['to'], axis=1)
        dropped = dropped.dropna()

        return dropped

    def convert_date_to_day(self) -> pd.core.frame.DataFrame:
        df_with_day = self.data
        df_with_day['day'] = pd.to_datetime(df_with_day['date']).dt.day_name()
        df_with_day = df_with_day.drop(['date'], axis=1)
        
        return df_with_day

    def convert_scheduled_time_to_part_of_the_day(self) -> pd.core.frame.DataFrame:
        df_new = self.data
        
        df_new['scheduled_time'] = pd.to_datetime(df_new['scheduled_time'])
        hour = df_new['scheduled_time'].dt.hour
    
        df_new['part_of_the_day'] = hour.apply(lambda x: 'late_night' if 0 <= x < 4 else
                                                 'early_morning' if 4 <= x < 8 else
                                                 'morning' if 8 <= x < 12 else
                                                 'afternoon' if 12 <= x < 16 else
                                                 'evening' if 16 <= x < 20 else 'night')

        df_new = df_new.drop(['scheduled_time'], axis=1)
        return df_new

    def convert_delay(self) -> pd.core.frame.DataFrame:
        df_new = self.data

        df_new['delay'] = df_new['delay_minutes'].apply(lambda x: 1 if x >= 5 else 0)

        return df_new

    def drop_unnecessary_columns(self) -> pd.core.frame.DataFrame:
        dropped = self.data.drop(['train_id'], axis=1)
        dropped = dropped.drop(['actual_time'], axis=1)
        dropped = dropped.drop(['delay_minutes'], axis=1)
        
        return dropped

    def save_first_60k(self, path: str):
        first_60k = self.data.head(60000)
        first_60k.to_csv(path_or_buf=path, index=False)

    def prep_df(self, path = 'data/NJ.csv'):
        self.data = self.order_by_scheduled_time()
        self.data = self.drop_columns_and_nan()
        self.data = self.convert_date_to_day()
        self.data = self.convert_scheduled_time_to_part_of_the_day()
        self.data = self.convert_delay()
        self.data = self.drop_unnecessary_columns()
        self.save_first_60k(path)
