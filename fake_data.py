import pandas as pd

# Create fake Chinese data
data = {
    "姓名": ["张伟", "李娜", "王强", "赵敏", "陈杰"],  # Names
    "地址": ["北京市", "上海市", "广州市", "深圳市", "杭州市"],  # Cities
    "职业": ["工程师", "教师", "医生", "设计师", "程序员"],  # Jobs
    "工资": [12000, 8000, 15000, 11000, 13000],  # Salaries in CNY
}

# Create a DataFrame
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
df.to_excel("chinese_fake_data.xlsx", index=False, sheet_name='数据')

print("Excel file with Chinese fake data created successfully!")
