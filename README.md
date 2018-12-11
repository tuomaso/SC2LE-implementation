# SC2LE-implementation
An implementation of the fully convolutional agent for playing minigames in the Starcraft 2 learning environment introduced in https://arxiv.org/abs/1708.04782. Based on xhujoy's implementation https://github.com/xhujoy/pysc2-agents.

Adapted to work with version 2 of pysc2, requires cloning the most recent master branch from https://github.com/deepmind/pysc2, not compatible with the 2.0.1 version installed with pip. Includes several changes to make it closer to the network used in the original paper, most notably using the full state and action space as well as choosing action based on the policy function instead of epsilon greedy exploration.
