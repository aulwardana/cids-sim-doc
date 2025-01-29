Neural Network Model
==========================

.. _cids.fl.model:

This document explains the code in the provided Jupyter notebook for defining a deep neural network model using Keras in a Non-IID Federated Learning scenario.

1. Function: `create_model(input_shape)`
----------------------------------------

**Purpose**:  

Define and compile a sequential neural network model for binary classification tasks.

**Code**:

.. code-block:: python

   def create_model(input_shape):
       model = keras.Sequential([
           layers.Dense(20, activation='relu', input_shape=(input_shape,)),
           layers.Dense(10, activation='relu'),
           layers.Dense(5, activation='relu'),
           layers.Dense(3, activation='relu'),
           layers.Dense(1, activation='sigmoid')
       ])
       model.compile(
           loss='mean_squared_error',
           optimizer='sgd',
           metrics=['accuracy', Recall(), Precision()]
       )
       return model

**Details**:

2. Model Architecture
---------------------

- **Layer 1**:  

  - ``Dense(20, activation='relu', input_shape=(input_shape,))``  
  - A fully connected layer with 20 neurons and ReLU activation.  
  - ``input_shape`` parameter defines the feature dimensions of the input data (e.g., number of features in ``X_df_scl``).

- **Layer 2**:  

  - ``Dense(10, activation='relu')``  
  - A hidden layer with 10 neurons and ReLU activation.

- **Layer 3**:  

  - ``Dense(5, activation='relu')``  
  - A hidden layer with 5 neurons and ReLU activation.

- **Layer 4**:  

  - ``Dense(3, activation='relu')``  
  - A hidden layer with 3 neurons and ReLU activation.

- **Output Layer**:  

  - ``Dense(1, activation='sigmoid')``  
  - A single neuron with sigmoid activation for binary classification (outputs probabilities between 0 and 1).

3. Model Compilation
--------------------

- **Loss Function**:  

  - ``loss='mean_squared_error'`` (MSE)  
  - Typically used for regression tasks, but here applied to binary classification.  
  - For better performance in classification, consider replacing with ``binary_crossentropy``.

- **Optimizer**:  

  - ``optimizer='sgd'`` (Stochastic Gradient Descent)  
  - A basic optimizer for weight updates during training. Alternatives include ``adam`` or ``rmsprop``.

- **Metrics**:  

  - ``metrics=['accuracy', Recall(), Precision()]``  
  - Tracks classification accuracy, recall (sensitivity), and precision during training/evaluation.  
  - Assumes ``Recall`` and ``Precision`` are imported from ``tensorflow.keras.metrics``.

4. Customization Notes
----------------------

- **Adjusting Layers**:  

  - Modify the number of neurons (e.g., ``Dense(30, ...)``) or add/remove layers to experiment with model capacity.  
  - Example: Replace ``layers.Dense(3, activation='relu')`` with ``layers.Dense(8, activation='tanh')``.

- **Activation Functions**:  

  - Replace ``relu`` with alternatives like ``tanh``, ``leaky_relu``, or ``selu`` for experimentation.  
  - Ensure the output layer uses ``sigmoid`` for binary classification.

- **Compilation Parameters**:  

  - Change the loss to ``binary_crossentropy`` for standard classification tasks.  
  - Experiment with optimizers (e.g., ``optimizer='adam'``) or learning rate tuning.  

5. Dependencies
---------------

- Requires ``tensorflow`` or ``keras`` for model definition.  
- Ensure ``Recall`` and ``Precision`` are imported: 
 
  .. code-block:: python

     from tensorflow.keras.metrics import Recall, Precision

- Assumes input data (``X_df_scl``) has already been scaled and preprocessed.