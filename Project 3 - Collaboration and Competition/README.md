[//]: # (Image References)

[image1]: https://raw.githubusercontent.com/ravishchawla/Reinforcement-Learning-NanoDegree/master/Project%203%20-%20Collaboration%20and%20Competition/tennis.gif
"Agent"

[image2]: https://raw.githubusercontent.com/ravishchawla/Reinforcement-Learning-Navigation/master/Project%202%20-%20Continous%20Control/chart.png "Results"

# Reinforcement Learning Continous Control

### Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Project Motivation](#motivation)
4. [File Descriptions](#files)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

![Solved Agent][Image1]

## Description <a name="description"></a>
In this project, we trained a pair of Reinforcement Learning agents to learn how to use Tennis racquets to control and hit a tennis ball back and forth between them.

For the final report, see the Report file in this repository.


The Environment is based on Unity.It maintains a Tennis raquet, getting a positive reward for getting the ball to the opposite side, and negative reward for losing it.

The environment is based on a 8-dimensional state space, containing information such as the balls and rackquet's position and velocity. The action is based on a contionus space between -1 and 1.

The task is episodic, and in order to solve the environment, the goal is to train the agent and get an average score of +0.5 over 100 consecutive episodes, from either of the two agents.

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
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P3/Tennis/Tennis_Windows_x86_64.zip)

2. Place the file in the main root project directory, and unzip (or decompress) the file.

To Run the code, open the notebook `Tennis.ipynb`, and run code cells sequentially.

## Project Motivation<a name="motivation"></a>

For this project, I was interested in learning how to train multiple agents that interact with the same environment, and practice the following skills:

1. How a Multi Agent network is designed, and how it is trained.
2. How to tune the Reinforcement Learning models individually with different configurations to obtain better results.
3. How a Trained Multi DDPG Model can be used to interact and play in an actual environment.

## File Descriptions <a name="files"></a>

The main code for this project is included in the notebook `Tennis.ipynb`, and files `model.py`, `agent.py`, and `multiagents.py`. The notebooks contain code for running the agent, while the model file contains Model Configuration, the Agent has code for training the Actor and Critic models, and the MultiAgents file contains code for implementing Multiple Agents.

Other files in the project are:

- `python/` - this directory contains required packages for running the Unity environment
- `checkpoints/` - Checkpoints from the models at different episode training periods.

## Results<a name="results"></a>
In my final results, I learnt answwers to the above 3 questions, which I answered in the report.
The trained Multi DDPG models were able to solve the environment consistently and well.

With the final tuned network, the model was able to get an average score of +0.5 in 2,400 episodes.

![Training results][Image2]

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit to Udacity for providing the data and environment. You can find the Licensing for the data and other descriptive information from [Udacity](https://www.udacity.om). This code is free to use.
