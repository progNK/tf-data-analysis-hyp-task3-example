import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu
from scipy import stats

chat_id = 1068869116 # Ваш chat ID, не меняйте название переменной

def solution(x, y) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 0.05
    p = stats.mannwhitneyu(x, y).pvalue
    return p < alpha
