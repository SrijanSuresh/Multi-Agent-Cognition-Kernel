import temporal_memory
import agent_hub

class CoreKernel:
    def __init__(self):
        self.memory = temporal_memory.TemporalMemory()
        self.agent_hub = agent_hub.AgentHub()
        self.thought_log = []
        