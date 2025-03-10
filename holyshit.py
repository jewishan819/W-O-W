import pandas as pd
import plotly.express as px

# 硬编码数据
data = {
    'Country': ['POL', 'FRA', 'USA', 'SVN', 'ITA', 'JPN', 'BRA', 'DEU', 'ARG', 'SRB',
                'CAN', 'CUB', 'NDL', 'UKR', 'IRN', 'BEL', 'TUR', 'CZE', 'BGR', 'EGY',
                'QAT', 'AUS', 'TUN', 'NZL'],
    'Critic': [1613.459429, 1051.577646, 839.943401, 656.581014, 584.963543, 503.787046,
               278.138726, 155.737185, 135.785306, 117.922387, 107.913038, 98.194357,
               43.247993, 36.764545, 30.069388, 29.074435, 25.11101, 22.34974, 19.33081,
               17.916054, 16.203021, 8.233561, 5.74748, 4.462882],
    'GDP': [0.5209467011674929, 0.7063107462975684, 1.0, 0.2018792952000698, 0.6631743808135174,
            0.761895414258585, 0.6570750533582842, 0.756815528992418, 0.5098106905831715,
            0.2048027095586273, 0.6714503882226669, 0.4900536313243711, 0.5693418558568107,
            0.3278177579441883, 0.4451085297406325, 0.4979384220455464, 0.5574276895237382,
            0.4067218526155872, 0.2496463216501179, 0.4722499231747061, 0.3796902911617813,
            0.6149286420931873, 0.0, 0.4707532899819392],
    'Popularity': [0.3947083097518977, 0.339983232573828, 1.0, 0.7794051861124806, 0.3947083097518977,
                   0.0, 0.169991616286914, 0.7794051861124806, 0.2694303372517385, 0.694834414896847,
                   0.9280576048600373, 0.4394219535386525, 0.3947083097518977, 0.0, 0.3947083097518977,
                   0.4394219535386525, 0.339983232573828, 0.4394219535386525, 0.6290437286590969,
                   0.2694303372517385, 0.679966465147656, 0.2694303372517385, 0.7088522907903909,
                   0.7221120638799268],
    'Rating': [1.0, 0.6507553927201659, 0.519203933106304, 0.4052391221819828, 0.3607256760677136,
               0.3102726815168474, 0.1700172867158332, 0.09393093434230845, 0.08153569036627774,
               0.07043036454888504, 0.06420432328825411, 0.05816910163620347, 0.0240165588903922,
               0.01999166256895981, 0.01582588795284953, 0.01520676918984262, 0.01274388287222856,
               0.01102742943104077, 0.009150009209260275, 0.00827287964168433, 0.007204741927170646,
               0.002296456055374005, 0.00108105017615157, 0.0]
}

# 转换为DataFrame
df = pd.DataFrame(data)

# 将国家缩写转换为ISO3代码（用于匹配地图数据）
country_to_iso3 = {
    'POL': 'POL', 'FRA': 'FRA', 'USA': 'USA', 'SVN': 'SVN', 'ITA': 'ITA',
    'JPN': 'JPN', 'BRA': 'BRA', 'DEU': 'DEU', 'ARG': 'ARG', 'SRB': 'SRB',
    'CAN': 'CAN', 'CUB': 'CUB', 'NDL': 'NLD', 'UKR': 'UKR', 'IRN': 'IRN',
    'BEL': 'BEL', 'TUR': 'TUR', 'CZE': 'CZE', 'BGR': 'BGR', 'EGY': 'EGY',
    'QAT': 'QAT', 'AUS': 'AUS', 'TUN': 'TUN', 'NZL': 'NZL'
}
df['iso_alpha'] = df['Country'].map(country_to_iso3)

# 定义绘制地图的函数
def plot_world_map(metric, title, color_scale):
    fig = px.choropleth(
        df,
        locations="iso_alpha",  # 使用ISO3代码
        locationmode='ISO-3',  # 使用ISO-3代码匹配国家
        color=metric,
        hover_name="Country",
        hover_data=[metric],
        title=title,
        color_continuous_scale=color_scale,
        range_color=(df[metric].min(), df[metric].max()),
        labels={metric: title}
    )
    fig.update_layout(
        geo=dict(showframe=False, showcoastlines=True, projection_type='equirectangular'),
        title_font_size=20,
        title_x=0.5,
        coloraxis_colorbar=dict(
            title=title,
            thickness=20,
            len=0.75,
            yanchor='middle',
            y=0.5
        )
    )
    fig.show()

# 绘制四张地图，使用更鲜艳的颜色渐变
plot_world_map('Critic', 'Critic Scores by Country', 'OrRd')  # 橙红色渐变
plot_world_map('GDP', 'GDP Scores by Country', 'Bluered')  # 蓝红色渐变
plot_world_map('Popularity', 'Popularity Scores by Country', 'Greens')  # 绿色渐变
plot_world_map('Rating', 'Rating Scores by Country', 'Purpor')  # 紫色渐变