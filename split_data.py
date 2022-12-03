import pandas as pd


def main():
    df = pd.read_csv('./data/bp_weather_data.csv')
    TEST_RATIO = 0.2

    cut_idx = int(len(df)*(1-TEST_RATIO))

    train_df = df.iloc[:cut_idx]
    test_df = df.iloc[cut_idx:]

    train_df.to_csv('./data/train_data.csv',index=False)
    test_df.to_csv('./data/test_data.csv',index=False)


if __name__ == '__main__':
    main()