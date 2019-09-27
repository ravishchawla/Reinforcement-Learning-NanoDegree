[//]: # (Image References)

[image1]: https://miro.medium.com/max/1000/1*ZJezBP0mdDudLtgtbbuJuA.gif "Trained Agent"
[image2]: https://miro.medium.com/max/4775/1*OBX8pz2pNJWVQnCtpoYJPw.png "Results"

# Reinforcement Learning Navigation

### Table of Contents

1. [Description](#description)
2. [Installation](#installation)
3. [Project Motivation](#motivation)
4. [File Descriptions](#files)
5. [Results](#results)
6. [Licensing, Authors, and Acknowledgements](#licensing)

## Description <a name="description"></a>
In this project, we trained a Reinforcement Learning agent to navigate a Unity environment, with a goal to collect _yellow bananas_ in order to maximize its score.

For the final report, see the Medium post on the work [here](https://medium.com/ml2vec/reinforcement-deep-q-learning-for-playing-a-game-in-unity-d2577fb50a81).

![Trained Agent][image1]

The Environment is based on Unity. As shown in the above image, there are yellow bananas and blue bananas. You get a reward of +1 every time you pick up a yellow banana, and -1 for every blue banana.

The environment is based on a 37-dimensional state space, containing information such as the agent's velocity, and a ray-based perception of objects around the agent's forward looking direction. The action space consists of 4 available actions:
- **`0`** - move forward.
- **`1`** - move backward.
- **`2`** - turn left.
- **`3`** - turn right.

The task is episodic, and in order to solve the environment, the goal is to train the agent and get an average score of +13 over 100 consecutive episodes.

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
    - Linux: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Linux.zip)
    - Mac OSX: [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana.app.zip)
    - Windows (32-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86.zip)
    - Windows (64-bit): [click here](https://s3-us-west-1.amazonaws.com/udacity-drlnd/P1/Banana/Banana_Windows_x86_64.zip)

2. Place the file in the main root project directory, and unzip (or decompress) the file.

To Run the code, open the notebook `Navigation.ipynb`, and run code cells sequentially. The training cell can be skipped to move directly onto the last cell, to see how the pre-trained model works on the Unity environment.

## Project Motivation<a name="motivation"></a>

For this project, I was interested in learning how to train a Deep Q Learning network, and practice the following skills:
1. How a Deep Q Learning Network is designed, and how it is trained using replay memory.
2. How a Deep Q Learning Network differs from its variations, such as Dueling Networks.
3. How a Trained Deep Q Learning Network model can be used to interact and play in an actual environment.

## File Descriptions <a name="files"></a>

The main code for this project is included in the notebook `Navigation.ipynb`. The notebooks contains code for a Network model, Learning agent, training code, and usage of the trained model to play the navigation game.
The code and results are also posted on Medium as a [blog post](https://medium.com/ml2vec/reinforcement-deep-q-learning-for-playing-a-game-in-unity-d2577fb50a81).

Other files in the project are:

- `python/` - this directory contains required packages for running the Unity environment
- `pt` extension files - these are model checkpoint files for the deep networks

## Results<a name="results"></a>
In my final results, I learnt answwers to the above 3 questions, which I answered on the Medium blog post.
The trained Dueling Deep Q Learning Networks were able to solve the environment quickly and well.

With the Vanilla network, the model was able to get a score of +13 in 250 episodes, and with Dueling networks, in 350 episodes.

![Training results][Image2]

More detailed findings can be found at the post available [here](https://medium.com/ml2vec/reinforcement-deep-q-learning-for-playing-a-game-in-unity-d2577fb50a81).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit to Udacity for providing the data and environment. You can find the Licensing for the data and other descriptive information from [Udacity](https://www.udacity.om). This code is free to use.
