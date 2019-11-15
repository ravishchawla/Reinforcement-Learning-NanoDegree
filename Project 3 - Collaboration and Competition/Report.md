[//]: # (Image References)

[image1]: https://raw.githubusercontent.com/ravishchawla/Reinforcement-Learning-NanoDegree/master/Project%203%20-%20Collaboration%20and%20Competition/multiagent.png "MultiAgent"
[image2]: https://raw.githubusercontent.com/ravishchawla/Reinforcement-Learning-NanoDegree/master/Project%203%20-%20Collaboration%20and%20Competition/results.png "Results"

[image3]: https://raw.githubusercontent.com/ravishchawla/Reinforcement-Learning-NanoDegree/master/Project%203%20-%20Collaboration%20and%20Competition/tennis.gif
"Agent"

# Reinforcement Learning Continous Control Report

### Table of Contents

1. [Learning Algorithm](#algorithm)
2. [Plot of Rewards](#plot)
3. [Ideas for Future Work](#futurework)

## Learning Algorithm <a name="algorithm"></a>
The base algorithm used in this project is the DDPG Actor Critic Model. The agent is wrapped in a Multi Agent structure, to share the Replay Memory buffer between the two agents. Initial code for the Agent and Model is an extension of the algorithm used in Project 2 of this NanoDegree.

The paper _Multi-Agent Actor-Critic for Mixed Cooperative Competitive Environments_ (https://arxiv.org/pdf/1706.02275.pdf) goes over the design of the agent, and how it can be used to train such environments. The figure below (from the paper) shows an overview of Multiple Actor Critic models.

![Model Pseudocode][Image1]

The Actor Critic Model itself consists of 2 Neural Networks, an Actor model and a Critic model. The Actor model is used to estimate the policy, and takes as input the current state to output the action to take at that step. The Critic Model is used for value estimation, to maximize the value from the input state.

The Actor and Critic Models have Local and Target models each, where the Target model is copied from the Local models after each iteration to slowly track the local models.

Like other Reinforcment Learning models, a Replay Buffer is used to sample experience tuples to update the neural networks at each iteration as well. Random batches of State-Action-Reward-NextAction tuples are sampled to update the policy and value networks.

In the Multi Agent algorithm, multiple Agents are instantiated together, where each of them sample experience events from the same Replay Buffer. The Environment returns states for multiple agents, and each is used to update and take an action on from the individual agents.

The Models used for training are:

| Actor Model Layer | Shape |
| ------------- | ------------- |
| Input Layer  | _24_ x 128  |
| BatchNorm Layer  | 128  |
| Dense Hidden Layer  | 128 x 64  |
| Output Layer | 64 x _2_ |

| Critic Model Layer | Shape |
| ------------- | ------------- |
| Input Layer  | _24_ x 128  |
| BatchNorm Layer  | 128  |
| Dense Hidden Layer  | 130 x 64  |
| Dropout Layer | 0.2 |
| Output Layer | 64 x _2_ |

The Input shape is number of states, _24_, and output is actions for agents being trained, _2_.


The Parameters used for the Agent are:

| Hyperparameter  | value |
| ------------- | ------------- |
| Replay Buffer Size  | 1e5  |
| Minibatch Size  | 128  |
| Discount Rate  | 0.99  |
| TAU  | 1e-3  |
| Actor Learning Rate  | 1e-4  |
| Critic Learning Rate  | 1e-4  |
| L2 Weight Decay  | 1e-6  |


## Plot of Rewards <a name="plot"></a>

![Solved Agent][Image3]

The goal of this project was to get an average reward from the last 100 episodes (of either agent) to be over 0.5 . After training the agent with different model configurations, the best performing model is the configuration shown above. After multiple hyperparameter tuning configurations, using a Learning Rate of `1e-4` was ideal, and showed significant improvement over smaller and bigger values than it.


With the current configuration, the target average reward reached in **2,453 episodes**.

![Results][Image2]

## Ideas for Future Work <a name="futurework"></a>
There are several things we can do to improve the results for this project. These are

- Further tune Hyperparameters for the model to improve results. Different model configurations could also be used, such as adding additional hidden dense layers.

- Add Prioritized Replay for the DDPG Algorithm, which changes the way samples are selected from the Replay Buffer. This method has been shown to show significant improvement over random sampling.

- Experiment with other algorithms mentioned in the Udacity Lectures, including SAC and TD3 algorithms.

- Apply this agent to different Cooperative and Competitive environments, such as the Soccer playing agents.