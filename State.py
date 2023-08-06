class LearningContext:
    def __init__(self, state):
        self._state = state

    def set_state(self, state):
        self._state = state

    def perform_action(self):
        self._state.execute()


class EasyLearningState:
    def execute(self):
        print("Displaying more explanations and hints for easy learning.")


class DifficultLearningState:
    def execute(self):
        print("Providing challenging exercises and minimal explanations for difficult learning.")

# Contoh penggunaan State Pattern
context = LearningContext(EasyLearningState())
context.perform_action()

context.set_state(DifficultLearningState())
context.perform_action()

