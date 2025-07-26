# errors.py

class RiloError(Exception):
    """Clase base para errores de Rilo."""
    pass

class LexicalError(RiloError):
    def __init__(self, line, value):
        super().__init__(f"Error Léxico en línea {line}: símbolo inesperado '{value}'")
        self.line = line
        self.value = value

class SyntacticError(RiloError):
    def __init__(self, line, message):
        super().__init__(f"Error Sintáctico en línea {line}: {message}")
        self.line = line
        self.message = message

class SemanticError(RiloError):
    def __init__(self, line, message):
        super().__init__(f"Error Semántico en línea {line}: {message}")
        self.line = line
        self.message = message

