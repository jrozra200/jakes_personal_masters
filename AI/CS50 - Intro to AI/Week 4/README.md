# Week 4 - Learning

## Lecture Notes

- Supervised learning: given a set of input-output pairs, learn a function to 
map inputs to outputs
    - Classification: task of learning a function mapping an input point to a 
    discrete category 
        - nearest-neighbor classification: given an input, chooses the class of 
        the nearest data point to that input
        - k-nearest-neighbor classification: given an input, chooses the most 
        common class out of the k nearest data points to that input
        - Logistic Regression
        - Support Vector Machines: designed to find the maximum margin 
        separator, the boundary that maximizes the distance between any of the 
        data points
    - Regression: task of learning a function mapping an input point to a 
    continuous value
        - Linear regression

- Evaluating hypotheses
    - 0-1 loss function: 0 if actual equals predicted, 1 otherwise
        - goal is minimize the loss
    - L1 loss function: abs(actual - predicted)
    - L2 loss function: (actual - predicted)^2
    - Overfitting: a model that fits too closely to a particular data set and 
    therefore may fail to generalize to future data
        - regularization: penalizing a hypothesis that is more complex by 
        adding a complexity term to the cost function
        - holdout cross-validation: splitting the data into a training set and a 
        text set, such that learning happens on the training set and evaluated 
        on the test set
        - k-fold cross-validation: splitting the data into k sets, and 
        experimenting k times, using each set as a test set once, and using the 
        remaining data as a training set
        
- Reinforcement learning: given a set of rewards or punishments, learn what 
actions to take in the future
    - Markov Decision Process: model for decision-making, representing states, 
    actions, and their rewards
    - Q-learning: method for learning a function Q(s, a), estimate of the value 
    of performing action a in state s.
    
- Unsupervised learning: given input data without additional feedback, learn 
patterns.
    - Clustering: organizing a set of objects into groups in such a way that 
    similar groups are labeled the same
    - k-means clustering: algorithm for clustering data based on repeatedly 
    assigning points to clusters and updating those clusters centers
    