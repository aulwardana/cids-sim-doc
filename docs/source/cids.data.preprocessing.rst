Data Preprocessing
==========================

.. _cids.data.preprocessing:

This document explains the code and workflow in the simulator for data preprocessing part.

1. Loading the Dataset
----------------------

**Purpose**: Load the dataset stored in a `.parquet` file for efficient data reading.

**Code**:

.. code-block:: python

   file_path = os.path.join('..', '..', 'dataset', 'CoAt_NF-UQ-NIDS-V2.parquet')
   df = pd.read_parquet(file_path, engine='pyarrow')

**Details**:

- The dataset ``CoAt_NF-UQ-NIDS-V2.parquet`` contains network flow (NF) features tailored for Non-IID scenarios.
- The ``pyarrow`` engine is used to read the Parquet file for better performance.

2. Viewing Dataset Information
------------------------------

**Purpose**: Inspect the structure and metadata of the loaded DataFrame.

**Code**:

.. code-block:: python

   df.info()

**Details**:

- Displays column names, data types, and non-null counts.
- Helps verify the dataset's integrity (e.g., missing values, memory usage).

3. Preparing Binary Labels
--------------------------

**Purpose**: Convert the problem to binary classification by removing the multi-class label.

**Code**:

.. code-block:: python

   df = df.drop(columns=['Label'])
   df.info()

**Details**:

- The original dataset includes a multi-class column ``Label``, which is dropped.
- The remaining column ``Attack`` is used as the binary label (0 = normal, 1 = anomaly).

4. Analyzing Class Distribution
-------------------------------

**Purpose**: Check the balance between normal and anomaly traffic samples.

**Code**:

.. code-block:: python

   df['Attack'].value_counts()

**Details**:

- Outputs the count of samples labeled ``0`` (normal) and ``1`` (anomaly).
- Critical for assessing potential class imbalance issues.

5. Splitting Features and Labels
--------------------------------

**Purpose**: Separate input features (``X``) from target labels (``y``).

**Code**:

.. code-block:: python

   X_df = df.drop(columns=['Attack'])
   y_df = df['Attack']

**Details**:

- ``X_df`` contains all columns except ``Attack`` (input features).
- ``y_df`` contains only the ``Attack`` column (target variable).

6. Feature Scaling
------------------

**Purpose**: Normalize feature values to ensure uniformity in scale.

**Code**:

.. code-block:: python

   scaler = QuantileTransformer(output_distribution='normal')
   X_df_scl = scaler.fit_transform(X_df)

**Details**:

- ``QuantileTransformer`` maps features to a normal distribution, reducing the impact of outliers.
- Suitable for scenarios where features have varying ranges or skewed distributions.

Notes
-----

- **Dependencies**: Requires ``pandas``, ``pyarrow``, and ``scikit-learn`` (for ``QuantileTransformer``).
- **Dataset Assumptions**: The ``Attack`` column is assumed to exist and contain binary labels.
- **Non-IID Context**: The preprocessing steps are tailored for Non-IID data, where sample independence and identical distribution assumptions do not hold.

