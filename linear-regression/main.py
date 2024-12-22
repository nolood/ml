import pandas as pd

data = {
	"Площадь (m2)": [30, 50, 80, 100, 120],
	"Цена ($)": [50000, 100000, 160000, 200000, 240000],
}


df = pd.DataFrame(data)

print(df)