from . import temporal_memory
from . import agent_hub
import time

class CoreKernel:
    def __init__(self):
        self.memory = temporal_memory.TemporalMemory()
        self.agent_hub = agent_hub.AgentHub()
        self.thought_log = []
    
    def process_input(self, user_input):
        start = time.time()
        self.thought_log.append(f"[INPUT] {user_input}")
        
        memory_result = self.memory.search(user_input)
        self.thought_log.append(f"[MEMORY] Retrieved: {memory_result}")

        response = self.agent_hub.route(user_input, memory_result)
        self.thought_log.append(f"[AGENT] Response: {response}")

        end = time.time()
        self.thought_log.append(f"[METRIC] Processing time: {end - start:.2f}s")
        
        return response

    def print_log(self):
        print("\n".join(self.thought_log))
