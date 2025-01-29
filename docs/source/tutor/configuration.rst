.. _configuration:

Configuration
===========

Setup & Configuration
---------------------

Environment Setup
~~~~~~~~~~~~~~~~~

1. Install dependencies:
   .. code-block:: bash

      pip install -r requirements.txt

2. Place your dataset (e.g., ``CoAt-Set.csv``) in the ``./dataset`` directory.
3. Update the dataset path in the code:
   .. code-block:: python

      file_path = os.path.join("dataset", "your_dataset.csv")  # Adjust path as needed

Dataset Configuration
~~~~~~~~~~~~~~~~~~~~~

- **Binary Classification (Default)**:
  .. code-block:: python

     df = df.drop(columns=['Label'])  # Drops multi-class labels
     y_df = df['Attack']              # Target: 0 (benign) or 1 (attack)

- **Multi-Class Classification**:
  .. code-block:: python

     y_df = df['Label']  # Retain 'Label' column for multi-class targets

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

Model Customization
-------------------

Neural Network Architecture
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``create_model()``:

.. code-block:: python

   def create_model():
       model = Sequential([
           Dense(64, activation='relu', input_shape=(input_dim,)),
           Dense(32, activation='tanh'),   # Example modified layer
           Dense(1, activation='sigmoid')  # Output layer
       ])
       model.compile(optimizer='adam', loss='binary_crossentropy')
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

.. code-block:: bash

   python simulator.py

Outputs Generated:
- **Logs**: Real-time metrics (accuracy, F1-score) in the console.
- **Visualizations**: PNG plots of accuracy vs. rounds (saved to ``./results``).
- **CSV Files**: Detailed metrics per client (e.g., ``global_metrics.csv``).

Troubleshooting
---------------

Common Issues:
- **Dataset Not Found**:
  - Verify ``file_path`` points to the correct CSV file.
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