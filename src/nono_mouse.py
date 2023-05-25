from services.field_factory import FieldFactory
from services.solver import Solver

if __name__ == '__main__':
    field = FieldFactory.create_mouse_example()
    Solver.print_field(field)

    # start solving...
    Solver.try_line(field, 5, True)
