import random
import numpy as np

class QLearningAgent:
    def __init__(self, graph, start_node, end_node, learning_rate=0.1, discount_factor=0.9, epsilon=1.0, epsilon_decay=0.995, min_epsilon=0.01):
        self.graph = graph
        self.start_node = start_node
        self.end_node = end_node
        self.q_table = {}
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon
        self.initialize_q_table()

    def initialize_q_table(self):
        for node in self.graph:
            self.q_table[node] = {neighbor: 0 for neighbor in self.graph[node]}

    def choose_action(self, state):
        # Epsilon-greedy strategy for action selection
        if random.uniform(0, 1) < self.epsilon:
            return random.choice(list(self.graph[state]))
        else:
            return max(self.q_table[state], key=self.q_table[state].get)

    def update_q_value(self, state, action, reward, next_state):
        max_future_q = max(self.q_table[next_state].values()) if next_state in self.q_table else 0
        current_q = self.q_table[state][action]
        self.q_table[state][action] = current_q + self.learning_rate * (reward + self.discount_factor * max_future_q - current_q)

    def train(self, episodes=1000, save_interval=50):
        all_paths = []
        best_path = []
        best_length = float('inf')

        for episode in range(episodes):
            current_node = self.start_node
            path = [current_node]
            total_reward = 0

            while current_node != self.end_node:
                action = self.choose_action(current_node)
                next_node = action
                reward = -1  # Step penalty to encourage shorter paths

                if next_node == self.end_node:
                    reward = 100  # High reward for reaching the end node

                self.update_q_value(current_node, action, reward, next_node)
                path.append(next_node)
                total_reward += reward
                current_node = next_node

                if len(path) > best_length * 2:  # Break if path becomes excessively long
                    break

            # Save the path if it's the shortest found so far
            if len(path) < best_length:
                best_length = len(path)
                best_path = path

            # Decay epsilon
            self.epsilon = max(self.min_epsilon, self.epsilon * self.epsilon_decay)

            # Save paths at intervals
            if episode % save_interval == 0 or episode == episodes - 1:
                all_paths.append(path)

        return all_paths, best_path  # Return all paths and the best path
