.. _installation:

Installation
===========

**Prerequisites**

 * CIDS-Sim requires Python >=3.10

.. note::

    Python == 3.10.15 is strongly recommended.

.. note::

    The creation of a virtual environment is strongly recommended. 
    CIDS-Sim using miniconda to create the virtual environment.

.. note::

    Github: https://github.com/aulwardana/CIDS-Sim

**Miniconda Instalation**

Create folder to download miniconda installation

.. code-block::

    mkdir -p ~/miniconda3

Download miniconda installation

.. code-block::

    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh

Run miniconda installation

.. code-block::

    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3

Remove miniconda instalation folder

.. code-block::

    rm -rf ~/miniconda3/miniconda.sh

Load miniconda

.. code-block::

    ~/miniconda3/bin/conda init bash
    ~/miniconda3/bin/conda init zsh

After that, close the terminal and open again, then you can continue to `Prepare Environment using Miniconda` part.

At this point, the ``complete_pipeline.ipynb`` should run completely. To use GPU, CUDA must be
properly configured.

**Prepare Environment using Miniconda**

Create environment with python 3.10 and install libraries

.. code-block::

    conda create --name cids_env python=3.10

Then activate the environment

.. code-block::

    conda activate cids_env

After that, install jupyter notebook

.. code-block::

    conda install notebook

.. note::

    This research using ``jupyter notebook`` to run the simulator.

**Clone Repositories**

Now you need to clone this repositories. Run the command below, make sure that git is already installed.

.. code-block::

    git clone https://github.com/aulwardana/CIDS-Sim.git

Then open the cloned repositories

.. code-block::

    cd CIDS-Sim

Next, you need to install the requirement for the library.

**CRun Jupyter Notebook**

Run this command to open Jupyter Notebook in browser.

.. code-block::

    git clone https://github.com/aulwardana/CIDS-Sim.git

.. note::

    This will display information about the notebook server in your terminal, including the URL for the web application, which is typically ``http://localhost:8888`` by default.

After all the setup done, you can open `src` folder in github page for the next instruction.

**Development Tool**

Software:
 * This simulator is develop using Python programming language
 * This simulator use Jupyter Notebook as code editor and to run the simulator

Hardware:
 * To develop the simulator, a server with specific technical specifications was utilized: a AMD EPYC 7713 64-Core processor coupled with 64 GB of RAM.

