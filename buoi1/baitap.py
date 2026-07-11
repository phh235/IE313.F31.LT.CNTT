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

# Xem dữ liệu
print(df.head())
print(df.tail())

# Thông tin
print(df.shape)
print(df.columns)
print(df.dtypes)
df.info()

# Thống kê
print(df.describe())
print(df.describe(include="all"))

# Truy xuất
print(df["price"])
print(df[["make", "price"]])

print(df.iloc[0])
print(df.iloc[0:5])
print(df.iloc[0, 2])

print(df.loc[:, "price"])
print(df.loc[:, ["make", "price"]])

# Xuất dữ liệu
df.to_csv("datasetV2.csv", index=False)
