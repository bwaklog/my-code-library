from random import randint
from sklearn.linear_model import LinearRegression


# Training
TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = list()
TRAIN_OUTPUT = list()
for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)
    op = a + (2*b) + (3*c)
    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(op)

# Creating a Linear Regression Model
predictor = LinearRegression(n_jobs=1)
predictor.fit(X=TRAIN_INPUT, y=TRAIN_OUTPUT)

# Test Data
X_TEST = [[10, 20, 30]]
outcome = predictor.predict(X=X_TEST)
coefficietns = predictor.coef_

print(f'Outcomes : {outcome}\nCoefficients : {coefficietns}')
