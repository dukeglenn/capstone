import pickle
model = pickle.load(open('model.pkl', 'rb'))
print(type(model))