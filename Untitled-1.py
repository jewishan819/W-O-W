import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 假设数据已经加载到一个DataFrame中
df = pd.read_excel("C:\\Users\\zj200\\Desktop\\副本regularized.xlsx", sheet_name='Data')
columns = ['Country Code', 'Search Trend', 'Int', 'Continent', 'GDP (million USD)']

# 设置主题和调色板
sns.set_theme(style="whitegrid", palette="husl")
plt.figure(figsize=(12, 8))

# 绘制散点图
scatter = sns.scatterplot(
    x='GDP (million USD)', 
    y='Search Trend', 
    hue='Continent', 
    size='Int',  # 根据 Int 列调整点的大小
    sizes=(50, 500),  # 点的大小范围
    alpha=0.8,  # 点的透明度
    data=df
)

# 添加标题和标签
plt.title('Search Trend vs GDP by Continent', fontsize=16, fontweight='bold')
plt.xlabel('GDP (million USD)', fontsize=14)
plt.ylabel('Search Trend', fontsize=14)

# 调整图例
plt.legend(title='Continent', title_fontsize=12, fontsize=10, bbox_to_anchor=(1.05, 1), loc='upper left')

# 添加网格线
plt.grid(True, linestyle='--', alpha=0.6)

# 显示图表
plt.tight_layout()
plt.show()