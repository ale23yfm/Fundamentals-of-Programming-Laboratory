class FunctionCall:
    def __init__(self, function, *params):
        self._function = function
        self._params = params

    def call(self):
        self._function(*self._params)  # * to unpack the parameters

    def __call__(self, *args, **kwargs):
        self.call()

class Operation:
    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall):
        self.__undo = undo_function
        self.__redo = redo_function

    def undo(self):
        self.__undo.call()

    def redo(self):
        self.__redo.call()

class UndoService:
    def __init__(self):
        self._undo_stack = []
        self._redo_stack = []

    def record(self, operation):
        self._undo_stack.append(operation)
        self._redo_stack.clear()

    def undo(self):
        if not self._undo_stack:
            return False
        op = self._undo_stack.pop()
        op.undo()
        self._redo_stack.append(op)
        return True

    def redo(self):
        if not self._redo_stack:
            return False
        op = self._redo_stack.pop()
        op.redo()
        self._undo_stack.append(op)
        return True

class CascadedOperation:
    def __init__(self):
        self._operations = []

    def add(self, operation):
        self._operations.append(operation)

    def undo(self):
        for op in reversed(self._operations):
            op.undo()

    def redo(self):
        for op in self._operations:
            op.redo()