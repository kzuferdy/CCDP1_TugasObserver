from abc import ABC, abstractmethod

class Expression(ABC):
    @abstractmethod
    def interpret(self, context):
        pass

class FloraExpression(Expression):
    def __init__(self, flora_name):
        self.flora_name = flora_name

    def interpret(self, context):
        return context.get_flora_info(self.flora_name)


class FaunaExpression(Expression):
    def __init__(self, fauna_name):
        self.fauna_name = fauna_name

    def interpret(self, context):
        return context.get_fauna_info(self.fauna_name)

class Context:
    def get_flora_info(self, flora_name):
        # Lakukan logika untuk mendapatkan informasi tentang flora berdasarkan nama flora
        return f"Informasi flora tentang {flora_name}"

    def get_fauna_info(self, fauna_name):
        # Lakukan logika untuk mendapatkan informasi tentang fauna berdasarkan nama fauna
        return f"Informasi fauna tentang {fauna_name}"

def main():
    # Membuat objek konteks
    context = Context()

    # Membuat objek-ekspresi untuk menafsirkan ekspresi pengguna
    flora_expression = FloraExpression("Mawar")
    fauna_expression = FaunaExpression("Harimau")

    # Menerjemahkan dan mengevaluasi ekspresi pengguna
    user_input = "flora:Mawar"
    if user_input.startswith("flora:"):
        expression = flora_expression
    elif user_input.startswith("fauna:"):
        expression = fauna_expression
    else:
        print("Ekspresi tidak valid.")
        return

    result = expression.interpret(context)
    print(result)


if __name__ == "__main__":
    main()
