[//]: # (Image References)

[image2]: https://raw.githubusercontent.com/ravishchawla/Reinforcement-Learning-Navigation/master/Project%202%20-%20Continous%20Control/chart.png "Results"

# Reinforcement Learning Continous Control

### Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Project Motivation](#motivation)
4. [File Descriptions](#files)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Description <a name="description"></a>
In this project, we trained a Reinforcement Learning agent to learn how to maintain a Double-Jointed arm's location in it's place. 

For the final report, see the Report file in this repository.


The Environment is based on Unity. It maintains a Double Jointed arm provding reward when the arm is in the correct location.

The environment is based on a 33-dimensional state space, containing information such as the agent's velocity, rotation, and position. The action is based on a contionus space between -1 and 1.

The task is episodic, and in order to solve the environment, the goal is to train the agent and get an average score of +30 over 100 consecutive episodes.

## Installation <a name="installation"></a>

This project uses Python 3, along with Jupyter Notebook. The following libraries are necessary for running the notebook:
* Pandas
* Numpy
* MatplotLib
* PyTorch
* `python/`

For the last package, packages are included in the `python/` directory. To install them, `cd` into the directory and run `pip install .`

Packages used by this project can also be installed as a Conda Environment using the provided Requirements.txt file.

In addition, the Unity environment must be installed and included into the main project directory for the code to run:

1. Download the environment from one of the links below.  You need only select the environment that matches your operating system:
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P2/Reacher/one_agent/Reacher_Windows_x86_64.zip)

2. Place the file in the main root project directory, and unzip (or decompress) the file.

To Run the code, open the notebook `Continous_Control.ipynb`, and run code cells sequentially.

## Project Motivation<a name="motivation"></a>

For this project, I was interested in learning how to train an Actor-Critic network, and practice the following skills:
1. How a DDPG Actor-Critic Network is designed, and how it is trained.
2. How to tune Reinforcement Learning model with different model configurations to obtain better results.
3. How a Trained DDPG Model can be used to interact and play in an actual environment.

## File Descriptions <a name="files"></a>

The main code for this project is included in the notebook `Continous_Control.ipynb`, and files `model.py` and `agent.py`. The notebooks contain code for running the agent, while the model file contains Model Configuration, and Agent has code for training the Actor and Critic models.

Other files in the project are:

- `python/` - this directory contains required packages for running the Unity environment
- `pth` extension files - these are model checkpoint files for the deep networks

## Results<a name="results"></a>
In my final results, I learnt answwers to the above 3 questions, which I answered in the report.
The trained DDPG models were able to solve the environment quickly and well.

With the final tuned network, the model was able to get an average score of +30 in 140 episodes.

![Training results][Image2]

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit to Udacity for providing the data and environment. You can find the Licensing for the data and other descriptive information from [Udacity](https://www.udacity.om). This code is free to use.
