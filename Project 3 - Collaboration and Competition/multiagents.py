import numpy as np;
import torch;
from agent import Agent, ReplayBuffer;

BUFFER_SIZE = int(1e5)  # replay buffer size
BATCH_SIZE = 128        # minibatch size

class MultiAgents():
    def __init__(self, num_agents, state_size, action_size, random_seed):
        self.num_agents = num_agents;
        self.memory = ReplayBuffer(action_size, BUFFER_SIZE, BATCH_SIZE, random_seed);
        self.agents = [Agent(state_size, action_size, self.memory, BATCH_SIZE, random_seed) for agent_posit in range(num_agents)];
    
    def reset(self):
        [agent.reset() for agent in self.agents];
    
    def step(self, states, actions, rewards, next_states, dones):
        [self.agents[posit].step(states[posit], actions[posit], rewards[posit], next_states[posit], dones[posit]) for posit in range(self.num_agents)];
    
    def act(self, states):
        actions = [self.agents[posit].act(np.array([states[posit]])) for posit in range(self.num_agents)];
        return actions;
    
    def save(self, key):
        for posit in range(self.num_agents):
            torch.save(self.agents[posit].actor_local.state_dict(), 'checkpoint_actor_%d_key_%s.pth'%(posit, key));
            torch.save(self.agents[posit].critic_local.state_dict(), 'checkpoint_critic_%d_key_%s.pth'%(posit, key));
            
    def load(self, key):
        for posit in range(self.num_agents):
            self.agents[posit].actor_local.load_state_dict(torch.load('checkpoints/checkpoint_actor_%d_key_%s.pth'%(posit, key), map_location='cpu'));
            self.agents[posit].critic_local.load_state_dict(torch.load('checkpoints/checkpoint_critic_%d_key_%s.pth'%(posit, key), map_location='cpu'));