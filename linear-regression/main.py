import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

data = {
    "Площадь (м²)": [30, 50, 80, 100, 120],
    "Цена ($)": [50000, 100000, 160000, 200000, 240000]
}
df = pd.DataFrame(data)

X = df[["Площадь (м²)"]]
y = df["Цена ($)"]

model = LinearRegression()
model.fit(X, y)

y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)
print(f"Среднеквадратичная ошибка (MSE): {mse}")

plt.scatter(X, y, color="blue", label="Реальные данные")
plt.plot(X, y_pred, color="red", label="Предсказания")
plt.xlabel("Площадь (м²)")
plt.ylabel("Цена ($)")
plt.legend()
plt.show()

new_area = 70
predicted_price = model.predict([[new_area]])
print(f"Предсказанная цена для квартиры площадью {new_area} м²: {predicted_price[0]:.2f} $")
