from flask import Flask, render_template, jsonify, request
import pandas as pd
import random

app = Flask(__name__, static_folder='static', static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/restaurants', methods=['POST'])
def get_restaurants():
    # 读取 CSV 文件
    df = pd.read_csv('restaurants.csv')  # 替换为实际的文件路径

    # 获取前端传递的参数
    location = request.form.get('location', '沒有想法')
    price = request.form.get('price', '沒有想法')
    category = request.form.get('category', '沒有想法')
    n = int(request.form.get('n', 1))
    location = location.strip()
    price = price.strip()
    category = category.strip()

# 将条件转换为小写
    location = location.lower()
    price = price.lower()
    category = category.lower()
    # 根据参数过滤数据
    filtered_df = df[
    ((df['地點'].str.strip().str.lower().isin(location.split(','))) | (location == '沒有想法')) &
    ((df['價格'].str.strip().str.lower() == price) | (price == '沒有想法')) &
    ((df['類型'].str.strip().str.lower().isin(location.split(',')) == category) | (category == '沒有想法'))
]

    # 获取餐厅名列表
    restaurant_names = filtered_df['餐廳名稱'].tolist()

    # 随机选择 n 个餐厅
    if (n<=len(restaurant_names)):
        selected_restaurants = random.sample(restaurant_names, n)
        
    else:
        selected_restaurants=['不要瞎掰好嗎']
        #return jsonify({'message': 'There is no such restaurants.'})
    return jsonify({'restaurants': selected_restaurants})

    

if __name__ == '__main__':
    app.run(debug=True)
