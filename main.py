import datetime
import requests

import pandas as pd
from pydash import chunk


def read_data(company_name):
    try:
        time = {
            "period_1": 1000000000,
            "period_2": int(datetime.datetime.now().timestamp())}

        url_ = f"https://query1.finance.yahoo.com/v7/finance/download/{company_name}?period1={time['period_1']}&period2={time['period_2']}&interval=1d&events=history&includeAdjustedClose=true"

        session = requests.Session()
        response = session.get(url_, headers={'User-Agent': ''}).text

        data = chunk(response.split("\n"), 1)
        list_ = [i[0].split(",") for i in data]

        df = pd.DataFrame(list_)
        df.columns = df.iloc[0]
        df = df[1:]

        # df["Open"] = df["Open"].apply(lambda x: float(x))

        return df.to_dict("records")

    except Exception as e:
        return {'status': 'ERROR__', 'message': str(e)}


def read_csv(company_name):
    data = pd.read_csv(f"files_csv/{company_name}.csv")
    return data.to_dict("records")


if __name__ == '__main__':
    print(read_data("PINS"))
    # print(read_csv("ZUO"))
