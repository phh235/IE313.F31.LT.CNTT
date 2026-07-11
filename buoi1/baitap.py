import pandas as pd

# | Lệnh            | Ý nghĩa             |
# | --------------- | ------------------- |
# | `pd.read_csv()` | Đọc file CSV        |
# | `df.head()`     | Xem 5 dòng đầu      |
# | `df.tail()`     | Xem 5 dòng cuối     |
# | `df.shape`      | Số dòng, số cột     |
# | `df.columns`    | Tên các cột         |
# | `df.dtypes`     | Kiểu dữ liệu        |
# | `df.info()`     | Thông tin DataFrame |
# | `df.describe()` | Thống kê            |
# | `df["price"]`   | Lấy 1 cột           |
# | `df.iloc[]`     | Lấy theo vị trí     |
# | `df.loc[]`      | Lấy theo tên        |
# | `df.to_csv()`   | Xuất CSV            |

data_path = "data.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
           "num-of-doors", "body-style", "drive-wheels", "engine-location",
           "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
           "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(data_path, names=headers)

print(df.head())

