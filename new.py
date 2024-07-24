import pandas as pd

data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'David'],
    'Age': [28, 35, 22, 30, 25],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo'],
    'Salary': [60000, 80000, 45000, 70000, 55000]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print()


print("Filtering data where Age > 25:")
filtered_df = df[df['Age'] > 25]
print(filtered_df)
print()

df['Income_Category'] = pd.cut(df['Salary'], bins=[0, 50000, 70000, 100000], labels=['Low', 'Medium', 'High'])
print("DataFrame with Income Category:")
print(df)
print()

print("Average Salary by City:")
avg_salary_by_city = df.groupby('City')['Salary'].mean().reset_index()
print(avg_salary_by_city)
print()


print("Sorting DataFrame by Age in descending order:")
sorted_df = df.sort_values(by='Age', ascending=False)
print(sorted_df)
print()

df.to_csv('output.csv', index=False)
print("DataFrame saved to output.csv")
