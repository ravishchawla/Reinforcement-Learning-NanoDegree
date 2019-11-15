import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np


def hidden_init(layer):
    fan_in = layer.weight.data.size()[0]
    lim = 1. / np.sqrt(fan_in)
    return (-lim, lim)


class Actor(nn.Module):
    """Actor (Policy) Model."""

    def __init__(self, state_size, hidden_units, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            hidden_units (array): Number of nodes for layers
            seed (int): Random seed
            gate (function): activation function
            final_gate (function): final activation function
        """
        super(Actor, self).__init__()
        
        self.seed = torch.manual_seed(seed)
        
        self.input_layer = nn.Linear(state_size, hidden_units[0]);
        self.batchnorm_layer = nn.BatchNorm1d(hidden_units[0]);
        
        self.hidden_layer_1 = nn.Linear(hidden_units[0], hidden_units[1]);
        self.output_layer = nn.Linear(hidden_units[1], action_size);
        
        self.reset_parameters()

    def reset_parameters(self):
        self.input_layer.weight.data.uniform_(*hidden_init(self.input_layer));
        self.hidden_layer_1.weight.data.uniform_(*hidden_init(self.hidden_layer_1));
        
        self.output_layer.weight.data.uniform_(-3e-3, 3e-3);

    def forward(self, state):
        """Build an actor (policy) network that maps states -> actions."""
        
        out = self.input_layer(state);
        out = F.relu(self.batchnorm_layer(out));
        out = F.relu(self.hidden_layer_1(out));
        out = F.tanh(self.output_layer(out));
        return out;
    
class Critic(nn.Module):
    """Critic (Value) Model."""

    def __init__(self, state_size, hidden_units, action_size, seed):
        """Initialize parameters and build model.
        Params
        ======
            state_size (int): Dimension of each state
            action_size (int): Dimension of each action
            hidden_units (array): Number of nodes for layers
            seed (int): Random seed
            gate (function): activation function
        """
        super(Critic, self).__init__()
        self.seed = torch.manual_seed(seed)
        
        self.input_layer = nn.Linear(state_size, hidden_units[0]);
        
        self.batchnorm_layer = nn.BatchNorm1d(hidden_units[0]);
        self.hidden_layer_1 = nn.Linear(hidden_units[0] + action_size, hidden_units[1]);
        self.dropout_layer = nn.Dropout(p=0.2);
        self.output_layer = nn.Linear(hidden_units[1], action_size);
        self.reset_parameters()

    def reset_parameters(self):      
        self.input_layer.weight.data.uniform_(*hidden_init(self.input_layer));
        self.hidden_layer_1.weight.data.uniform_(*hidden_init(self.hidden_layer_1));
        
        self.output_layer.weight.data.uniform_(-3e-3, 3e-3);

    def forward(self, state, action):
        """Build a critic (value) network that maps (state, action) pairs -> Q-values."""
        x_state = self.input_layer(state);
        x_state = F.relu(self.batchnorm_layer(x_state));

        out = torch.cat((x_state, action), dim=1);
        out = F.relu(self.hidden_layer_1(out));
        #x = F.relu(self.hidden_layer_2(x));
        out = self.dropout_layer(out);
        out = self.output_layer(out);
        
        return out;