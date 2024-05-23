from typeguard import typechecked


@typechecked
class Stack:
    SIZE = 5

    def __init__(self, *elements: int):
        self.__stack_data = []
        if len(elements) > self.SIZE:
            raise MemoryError(f"La pila no puede exceder el límite de tamaño. Límite: {self.SIZE}")
        for element in elements:
            if isinstance(element, int):
                self.__stack_data.append(element)
            else:
                raise ValueError("Has introducido un valor incorrecto.")

    def length(self):
        return len(self.__stack_data)

    def is_empty(self):
        if self.length() == 0:
            return True
        else:
            return False

    def clear_out(self):
        self.__stack_data.clear()

    def push(self, element: int):
        if self.length() + 1 > self.SIZE:
            raise MemoryError("La pila ha llegado a su tamaño máximo, no puedes añadir más elementos.")
        self.__stack_data.append(element)

    def pop(self):
        if self.length() - 1 < 0:
            raise MemoryError("La pila ha llegado a su tamaño mínimo, no puedes eliminar más elementos.")
        element = self.__stack_data[self.length() - 1]
        self.__stack_data.pop()
        return element

    def top(self):
        if self.is_empty():
            raise MemoryError("La pila está vacía.")
        return self.__stack_data[self.length() - 1]

    def __str__(self):
        if len(self.__stack_data) != 0:
            self.__stack_data.reverse()
            data = "------\n PILA \n------\n"
            for i in self.__stack_data:
                data += f"{i:3}\n"
            data += "------"
            self.__stack_data.reverse()
            return data
        else:
            return "---------------------\n La pila esta vacía.\n---------------------"

    def __repr__(self):
        if len(self.__stack_data) != 0:
            data = f"Stack("
            i = 1
            for element in self.__stack_data:
                if len(self.__stack_data) != i:
                    data += f"{element}, "
                else:
                    data += f"{element}"
                i += 1
            data += ")"
            return data
        else:
            return "Stack()"

    def __add__(self, other: 'Stack'):
        size = self.length() + other.length()
        if size > self.SIZE:
            raise MemoryError(f"La pila no puede exceder el límite de tamaño. Límite: {self.SIZE}")
        new_stack = Stack()
        for element in self.__stack_data:
            new_stack.push(element)
        for element in other.__stack_data:
            new_stack.push(element)
        return new_stack

    def __sub__(self, other: int):
        while other in self.__stack_data:
            self.__stack_data.remove(other)
