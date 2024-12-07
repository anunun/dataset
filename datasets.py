import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("menu.csv")

# Гіпотеза 1: У категорії Breakfast середня калорійність більшості продуктів перевищує 400 калорій
breakfast_items = df[df['Category'] == 'Breakfast']
breakfast_high_cal = breakfast_items['Calories'] > 400
hypothesis_1 = breakfast_high_cal.mean() > 0.5

# Гіпотеза 2: Продукти з найбільшим вмістом білків (Protein) мають більше жиру (Total Fat)
protein_threshold = df['Protein'].quantile(0.75)  # Верхній квартиль білків
high_protein_items = df[df['Protein'] >= protein_threshold]
low_protein_items = df[df['Protein'] < protein_threshold]
hypothesis_2 = high_protein_items['Total Fat'].mean() > low_protein_items['Total Fat'].mean()

# Гіпотеза 3: Продукти Beef & Pork містять більше натрію (Sodium) у середньому, ніж Breakfast
beef_pork_items = df[df['Category'] == 'Beef & Pork']
hypothesis_3 = beef_pork_items['Sodium'].mean() > breakfast_items['Sodium'].mean()

# Результати
print(f"Гіпотеза 1: {'Так' if hypothesis_1 else 'Ні'}")
print(f"Гіпотеза 2: {'Так' if hypothesis_2 else 'Ні'}")
print(f"Гіпотеза 3: {'Так' if hypothesis_3 else 'Ні'}")

#1 Лінійний графік: Калорії залежно від білків
plt.figure(figsize=(8, 5))
plt.scatter(df['Protein'], df['Calories'], marker='o', linestyle='-')
plt.title('Залежність калорій від білків')
plt.xlabel('Protein (g)')
plt.ylabel('Calories')
plt.grid()
plt.show()

#2 Стовпчаста діаграма: Середня калорійність у кожній категорії
avg_calories = df.groupby('Category')['Calories'].mean()
avg_calories.plot(kind='bar', figsize=(8, 5), color='skyblue')
plt.title('Середня калорійність у кожній категорії')
plt.xlabel('Category')
plt.ylabel('Average Calories')
plt.xticks(rotation=45)
plt.show()

#3 Кругова діаграма: Розподіл продуктів за категоріями
category_counts = df['Category'].value_counts()
category_counts.plot(kind='pie', figsize=(8, 8), autopct='%1.1f%%', startangle=90)
plt.title('Розподіл продуктів за категоріями')
plt.ylabel('')
plt.show()

#4 Стовпчаста діаграма: Сумарна кількість калорій у кожній категорії
total_calories = df.groupby('Category')['Calories'].sum()

plt.figure(figsize=(10, 6))
total_calories.plot(kind='bar', color='coral', edgecolor='black')
plt.title('Сумарна кількість калорій у кожній категорії')
plt.xlabel('Category')
plt.ylabel('Total Calories')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

#5 Діаграма розсіювання: Калорії vs Жири
plt.figure(figsize=(8, 5))
plt.scatter(df['Total Fat'], df['Calories'], alpha=0.7, color='orange')
plt.title('Залежність калорій від жирів')
plt.xlabel('Total Fat (g)')
plt.ylabel('Calories')
plt.grid()
plt.show()