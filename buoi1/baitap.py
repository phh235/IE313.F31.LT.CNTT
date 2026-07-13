import pandas as pd
# -----------------------------------------
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
# -----------------------------------------

data_path = "data.csv"

headers = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
           "num-of-doors", "body-style", "drive-wheels", "engine-location",
           "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
           "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
           "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg", "price"]

df = pd.read_csv(data_path, names=headers)

# Xem dữ liệu
print("Xem 5 dòng đầu:")
print(df.head())
print("\nXem 5 dòng cuối:")
print(df.tail())

# Thông tin
print("\nSố dòng và số cột:")
print(df.shape)
print("\nTên các cột:")
print(df.columns)
print("Kiểu dữ liệu:")
print(df.dtypes)
df.info()

# Thống kê
print("\nThống kê:")
print(df.describe())
print(df.describe(include="all"))

# Truy xuất
print("Truy xuất cột price")
print(df["price"])
print("Truy xuất cột make và price")
print(df[["make", "price"]])

print("Truy xuất dòng đầu tiên")
print(df.iloc[0])
print("Truy xuất 5 dòng đầu tiên")
print(df.iloc[0:5])
print("Truy xuất dòng đầu tiên cột thứ 3")
print(df.iloc[0, 2])

print("Truy xuất cột price")
print(df.loc[:, "price"])
print("Truy xuất cột make và price")
print(df.loc[:, ["make", "price"]])

# Xuất dữ liệu
# df.to_csv("datasetV2.csv", index=False)
