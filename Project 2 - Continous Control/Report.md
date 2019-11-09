[//]: # (Image References)

[image1]: https://miro.medium.com/max/1626/1*BVST6rlxL2csw3vxpeBS8Q.png "Pseudocode"
[image2]: https://miro.medium.com/max/4775/1*OBX8pz2pNJWVQnCtpoYJPw.png "Results"

# Reinforcement Learning Continous Control Report

### Table of Contents

1. [Learning Algorithm](#algorithm)
2. [Plot of Rewards](#plot)
3. [Ideas for Future Work](#futurework)

## Learning Algorithm <a name="algorithm"></a>
The algorithm I used for this project is the DDPG Actor Critic Model. The model is based on this [paper](https://deepmind.com/research/publications/continuous-control-deep-reinforcement-learning), and initial code for the Agent and Model is derived from the Udacity Deep Reinforcement Learning lectures.

![Model Pseudocode][Image1]

The Actor Critic Model consists of 2 Neural Networks, an Actor model and a Critic model. The Actor model is used to estimate the policy, and takes as input the current state to output the action to take at that step. The Critic Model is used for value estimation, to maximize the value from the input state.

The Actor and Critic Models have Local and Target models each, where the Target model is copied from the Local models after each iteration to slowly track the local models.

Like other Reinforcment Learning models, a Replay Buffer is used to sample experience tuples to update the neural networks at each iteration as well. Random batches of State-Action-Reward-NextAction tuples are sampled to update the policy and value networks.

The Models used for training are:
| Actor Model Layer | Shape |
| ------------- | ------------- |
| Input Layer  | _33_ x 128  |
| BatchNorm Layer  | 128  |
| Dense Hidden Layer  | 128 x 64  |
| Output Layer | 128 x _1_ |

| Critic Model Layer | Shape |
| ------------- | ------------- |
| Input Layer  | _33_ x 128  |
| BatchNorm Layer  | 128  |
| Dense Hidden Layer  | 128 x 64  |
| Dropout Layer | 0.2 |
| Output Layer | 128 x _1_ |

The Input shape is number of states, _33_, and output is actions for agents being trained, _1_.


The Parameters used for the Agent are:
| Hyperparameter  | value |
| ------------- | ------------- |
| Replay Buffer Size  | 1e5  |
| Minibatch Size  | 128  |
| Discount Rate  | 0.99  |
| TAU  | 1e-3  |
| Actor Learning Rate  | 1e-4  |
| Critic Learning Rate  | 1e-4  |
| L2 Weight Decay  | 0  |


## Plot of Rewards <a name="plot"></a>
The goal of this project was to get an average reward from the last 100 episodes to be over 30. After training the agent with different model configurations, the best performing model is the configuration shown above. Adding the Batch Normalization layer improved the model the most, and helped increase the reward much quicker.


With the current configuration, the target average reward reached in **140 episodes**.

![Results][Image2]

## Ideas for Future Work <a name="futurework"></a>
There are several things we can do to improve the results for this project. These are

- Further tune Hyperparameters for the model to improve results. Different model configurations could also be used, such as adding additional hidden dense layers.

- Add Prioritized Replay for the DDPG Algorithm, which changes the way samples are selected from the Replay Buffer. This method has been shown to show significant improvement over random sampling.

- Experiment with other algorithms mentioned in the Udacity Lectures, including PPO, A3C, and A2C algorithms.