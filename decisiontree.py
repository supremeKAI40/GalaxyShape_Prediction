import numpy as np
from sklearn.tree import DecisionTreeClassifier
#splitdata_train_test function here
def splitdata_train_test(data, fraction_training):
  # complete this function
    np.random.shuffle(data)
    rows= int(fraction_training*len(data))
    training_set= data[:rows]
    testing_set= data[rows:]
    return training_set,testing_set

#generate_features_targets function here
def generate_features_targets(data):
  #calculating the concentrations
    targets = data['class']
    features = np.empty(shape=(len(data), 13))
    features[:, 0] = data['u-g']
    features[:, 1] = data['g-r']
    features[:, 2] = data['r-i']
    features[:, 3] = data['i-z']
    features[:, 4] = data['ecc']
    features[:, 5] = data['m4_u']
    features[:, 6] = data['m4_g']
    features[:, 7] = data['m4_r']
    features[:, 8] = data['m4_i']
    features[:, 9] = data['m4_z']
  # concentration in u filter
    features[:, 10] = data['petroR50_u']/data['petroR90_u']
  # concentration in r filter
    features[:, 11] = data['petroR50_r']/data['petroR90_r']
  # concentration in z filter
    features[:, 12] = data['petroR50_z']/data['petroR90_z']
    return features, targets

#splitting the data set and training a decision tree classifier
def dtc_predict_actual(data):
  # splitting the data into training and testing sets using a training fraction of 0.7
    training_set, testing_set= splitdata_train_test(data, 0.7)
  # generate the feature and targets for the training and test sets
    training_features,training_target= generate_features_targets(training_set)
    test_features,test_target= generate_features_targets(testing_set)
    dtr = DecisionTreeClassifier()
  # train the classifier with the train_features and train_targets
    dtr.fit(training_features, training_target)
  # predictions for the test_features
    predictions = dtr.predict(test_features)
    return predictions, test_target


if __name__ == '__main__':
  data = np.load('galaxy_catalogue.npy')
    
  predicted_class, actual_class = dtc_predict_actual(data)

  # Print some of the initial results to check
  print("Some initial results...\n   predicted,  actual")
  for i in range(10):
    print("{}. {}, {}".format(i, predicted_class[i], actual_class[i]))
 