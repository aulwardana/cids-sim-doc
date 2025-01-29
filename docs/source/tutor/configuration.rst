.. _configuration:

Configuration
===========

Setup & Configuration
---------------------

Environment Setup
~~~~~~~~~~~~~~~~~

1. Install dependencies. Follow more detail instruction on :ref:`installation` section.
   
   .. code-block:: bash

      pip install -r requirements.txt

2. Place your dataset (e.g., ``CoAt-Set.csv``) in the ``./dataset`` directory.
3. Update the dataset path in the code if you place the dataset in other directory or you use other dataset.
  
   .. code-block:: python

      file_path = os.path.join("your_dataset_path", "your_dataset.csv")  # Adjust path as needed

Dataset Configuration
~~~~~~~~~~~~~~~~~~~~~

1. By default, the simulator run **Binary Classification**. The target label is using ``Attack`` column in the dataset.

   .. code-block:: python

     df = df.drop(columns=['Label'])  # Drops multi-class labels
     y_df = df['Attack']              # Target: 0 (benign) or 1 (attack)

2. If you want to run **Multi-Class Classification**, you need change the target label is using ``Label`` column in the dataset.
  
  .. code-block:: python

     df = df.drop(columns=['Attack'])
     y_df = df['Label']  # Retain 'Label' column for multi-class targets

3. Do not forget to edit the neural network architecture in ``create_model()``:
4. Extra code for doing **Multi-Class Classification** also need to provide. This version of simulator is not cover yet, maybe in the future.

Federated Learning Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configure in ``cids_federated_training()``:

.. code-block:: python

   # Example settings
   num_nodes = 10     # Number of clients
   num_rounds = 20    # Training rounds
   epochs = 10        # Local epochs per round
   batch_size = 1000  # Batch size per client

Data Distribution Settings
~~~~~~~~~~~~~~~~~~~~~~~~~~

Modify in ``load_data()``:

.. code-block:: python

   # Non-IID partitioning example
   def load_data():
       # Each client receives 2% of the dataset
       fraction = 0.02
       # Customize shuffling/sampling logic here

Aggregation Algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~

The default method for aggregation algorithm in this simulator is ``Federated Averaging (FedAvg)``. You can modify the aggregation algorithm in the simulator by modify this code:

.. code-block:: python
   
   #Modify this code to change FedAvg with other aggregation algorithm.
   #You can also refer other aggregation algorithm concept from here https://www.sciencedirect.com/science/article/pii/S0167739X23003333
   new_weights = [np.mean([weight[layer] for weight in local_weights], axis=0) for layer in range(len(global_weights))]

Model Customization
-------------------

Neural Network Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``create_model()``:

.. code-block:: python

   def create_model(input_shape):
    model = keras.Sequential([
        layers.Dense(20, activation='relu', input_shape=(input_shape,)),
        layers.Dense(10, activation='relu'), #Edit activation using other method. You can see here https://keras.io/api/layers/activations/#available-activations
        layers.Dense(5, activation='relu'), #Edit number of neuron in each layer (e.g. change 5 with 1000)
        layers.Dense(3, activation='relu'),
        layers.Dense(1, activation='sigmoid') 
    ])
    #Edit loss with other method. You can see here https://keras.io/api/losses/#available-losses  
    #Edit optimizer with other method. You can see here https://keras.io/api/optimizers/#available-optimizers  
    model.compile(loss='mean_squared_error', optimizer='sgd', metrics=['accuracy', Recall(), Precision()])
    return model

Preprocessing Adjustments
~~~~~~~~~~~~~~~~~~~~~~~~~

Replace scalers in the preprocessing pipeline:

.. code-block:: python

   from sklearn.preprocessing import StandardScaler

   # Replace QuantileTransformer
   preprocessor = StandardScaler()

Execution & Outputs
-------------------

Run the Simulation
~~~~~~~~~~~~~~~~~~

Run ``jupyter notebook`` first.

.. code-block:: bash

   jupyter notebook

After that, you can open ``CIDS-Sim_Non-IID.ipynb`` and ``CIDS-Sim_Heterogeneous.ipynb`` in jupyter notebook.

Outputs Generated:

- **Logs**: Real-time metrics (accuracy, F1-score, and etc.) in the console.
- **Visualizations**: Graphic plots of metric in each rounds.
- **CSV Files**: Detailed metrics in each round and save in files (e.g., ``global_metrics.csv``).

Troubleshooting
---------------

Common Issues:

- **Dataset Not Found**:
    
    - Verify ``file_path`` points to the correct dataset file.
    - Check filesystem permissions.

- **Poor Model Performance**:
    
    - Increase ``num_rounds`` or ``epochs``.
    - Add more layers to ``create_model()``.

- **High Memory Usage**:

    - Reduce ``batch_size`` or ``num_nodes``.
    - Disable resource tracking in the code.

Support
-------
For further assistance, open an issue on the `GitHub repository <https://github.com/your-repo>`_.