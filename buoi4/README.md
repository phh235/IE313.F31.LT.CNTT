# Buổi 4 - Tiền xử lý dữ liệu

## Nội dung chính

Bài này thực hành làm sạch dữ liệu ô tô trong file `dataset_02.csv`, gồm:

- Nhận biết và xử lý dữ liệu khuyết.
- Chuyển kiểu dữ liệu cho đúng.
- Chuẩn hóa dữ liệu bằng Min-Max và Z-score.

Notebook thực hành: `baitap.ipynb`.

## 1. Đọc và xem dữ liệu

```python
import pandas as pd
import numpy as np

df = pd.read_csv("dataset_02.csv")

df.head()
df.shape
df.dtypes
```

Một số lệnh thường dùng:

- `head()`: xem các dòng đầu.
- `shape`: xem số dòng và số cột.
- `dtypes`: xem kiểu dữ liệu của từng cột.
- `info()`: xem tổng quát DataFrame.

## 2. Xử lý dữ liệu khuyết

Trong bộ dữ liệu này, ô bị thiếu được ghi bằng dấu `?`. Trước khi xử lý cần đổi chúng thành `NaN`:

```python
df.replace('?', np.nan, inplace=True)
```

Kiểm tra số lượng dữ liệu thiếu:

```python
df.isna().sum()
```

Chỉ hiện các cột có dữ liệu thiếu:

```python
df.isna().sum()[df.isna().sum() > 0]
```

### Xóa dòng bị thiếu

Nếu cột quan trọng như `price` bị thiếu thì có thể xóa cả dòng:

```python
df.dropna(subset=['price'], inplace=True)
```

Xóa tất cả các dòng vẫn còn dữ liệu thiếu:

```python
df.dropna(inplace=True)
```

### Điền bằng giá trị trung bình

Áp dụng với cột số như `horsepower`:

```python
df['horsepower'] = pd.to_numeric(df['horsepower'], errors='coerce')
mean_horsepower = df['horsepower'].mean()
df['horsepower'] = df['horsepower'].fillna(mean_horsepower)
```

Giá trị trung bình phù hợp với dữ liệu số, nhưng có thể bị ảnh hưởng nếu dữ liệu có nhiều giá trị quá lớn hoặc quá nhỏ.

### Điền bằng mode

Mode là giá trị xuất hiện nhiều nhất:

```python
df['normalized-losses'] = pd.to_numeric(
    df['normalized-losses'], errors='coerce'
)

mode_value = df['normalized-losses'].mode()[0]
df['normalized-losses'] = df['normalized-losses'].fillna(mode_value)
```

Mode có thể dùng cho cả dữ liệu số và dữ liệu phân loại.

## 3. Chuyển kiểu dữ liệu

Dữ liệu đọc từ CSV có thể mang kiểu `object` dù bên trong là số. Có thể dùng `pd.to_numeric()` để chuyển:

```python
df['price'] = pd.to_numeric(df['price'], errors='coerce')
```

Trong đó `errors='coerce'` sẽ đổi giá trị không chuyển được thành `NaN`.

Một số kiểu dữ liệu trong bài:

- `bore`, `stroke`: `float64` vì có số thập phân.
- `price`, `peak-rpm`, `normalized-losses`: `int64`.
- Các cột như `make`, `fuel-type`, `body-style`: dữ liệu dạng chữ.

Khi đổi từ số thực sang số nguyên nên kiểm tra hoặc làm tròn trước:

```python
df['horsepower'] = df['horsepower'].round().astype('int64')
```

## 4. Chuẩn hóa dữ liệu

Các cột số có đơn vị và khoảng giá trị khác nhau. Ví dụ `price` có thể lên đến hàng chục nghìn, còn `bore` chỉ khoảng vài đơn vị. Chuẩn hóa giúp đưa chúng về cùng một thang đo.

Trong bài, chuẩn hóa ba cột giống ví dụ trong slide là `length`, `width` và `height`.

### Cách 1: Min-Max

Công thức:

```text
x_new = (x - x_min) / (x_max - x_min)
```

Sau khi chuẩn hóa, giá trị nằm trong khoảng từ 0 đến 1.

```python
df_minmax = df.copy()

df_minmax['length'] = (df['length'] - df['length'].min()) / (
    df['length'].max() - df['length'].min()
)
```

Min-Max dễ hiểu và giữ được quan hệ giữa các giá trị, nhưng khá nhạy với giá trị ngoại lệ.

Cũng có thể dùng `MinMaxScaler` như trong slide 17:

```python
from sklearn.preprocessing import MinMaxScaler

mm = MinMaxScaler()
df_minmax_sklearn = df.copy()
df_minmax_sklearn['length'] = mm.fit_transform(df[['length']])
```

`fit_transform()` vừa tìm giá trị nhỏ nhất, lớn nhất của cột, vừa thực hiện chuẩn hóa.

### Cách 2: Z-score

Công thức:

```text
x_new = (x - mean) / standard_deviation
```

Sau khi chuẩn hóa, dữ liệu có trung bình gần 0 và độ lệch chuẩn gần 1.

```python
df_zscore = df.copy()

df_zscore['length'] = (
    (df['length'] - df['length'].mean()) / df['length'].std()
)
```

Z-score không giới hạn kết quả trong đoạn `[0, 1]`. Giá trị âm nghĩa là nhỏ hơn trung bình, giá trị dương nghĩa là lớn hơn trung bình.

## 5. So sánh hai cách chuẩn hóa

| Phương pháp | Kết quả | Khi nên dùng |
|---|---|---|
| Min-Max | Giá trị nằm trong `[0, 1]` | Khi cần một khoảng giá trị cố định |
| Z-score | Trung bình gần 0, độ lệch chuẩn gần 1 | Khi quan tâm độ lệch so với trung bình |

Chuẩn hóa chỉ thay đổi thang đo, không xử lý dữ liệu khuyết. Vì vậy cần làm sạch và chuyển kiểu dữ liệu trước khi chuẩn hóa.

## 6. Quy trình cần nhớ

```text
Đọc dữ liệu
    ↓
Đổi ký hiệu thiếu thành NaN
    ↓
Kiểm tra số lượng dữ liệu thiếu
    ↓
Xóa hoặc điền dữ liệu theo yêu cầu
    ↓
Chuyển kiểu dữ liệu
    ↓
Kiểm tra lại
    ↓
Chuẩn hóa dữ liệu
```

## 7. Một số lưu ý

- Nên dùng `copy()` khi muốn tạo nhiều phiên bản dữ liệu chuẩn hóa khác nhau.
- Không nên chuẩn hóa trực tiếp các cột dạng chữ.
- Cần kiểm tra cột có giá trị lớn nhất bằng giá trị nhỏ nhất hay không trước khi dùng Min-Max, vì khi đó mẫu số bằng 0.
- Tương tự, không dùng Z-score cho cột có độ lệch chuẩn bằng 0.
- Sau mỗi bước xử lý nên kiểm tra lại bằng `isna().sum()`, `dtypes` hoặc `describe()`.

## Kết quả của bài

Sau khi làm sạch, dữ liệu còn 193 dòng và 26 cột, không còn giá trị khuyết. Ba DataFrame được sử dụng là:

- `df`: dữ liệu sạch ban đầu.
- `df_minmax`: dữ liệu chuẩn hóa Min-Max.
- `df_zscore`: dữ liệu chuẩn hóa Z-score.
