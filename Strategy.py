class LearningStrategy:
    def learn(self):
        pass


class TaskBasedStrategy(LearningStrategy):
    def learn(self):
        print("Implementing task-based learning approach.")


class ChallengeBasedStrategy(LearningStrategy):
    def learn(self):
        print("Implementing challenge-based learning approach.")


class LearningContext:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def execute_learning(self):
        self._strategy.learn()


# Contoh penggunaan Strategy Pattern
context = LearningContext(TaskBasedStrategy())
context.execute_learning()

context.set_strategy(ChallengeBasedStrategy())
context.execute_learning()
