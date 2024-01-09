import pandas as pd

#JSON 파일을 데이터프레임으로 불러오기
dataframe = pd.read_json('한국어 대화 요약/Training/[라벨]한국어대화요약_train/개인및관계.json')

# 데이터프레임 확인
print(dataframe)