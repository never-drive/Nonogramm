from models.field import Field


class FieldFactory:

    @staticmethod
    def create_small_example():
        block_definitions = {
            'rows': [[5], [1, 1, 1], [5], [1], [1]],
            'cols': [[5], [1, 1], [3], [1, 1], [3]],
        }
        field = Field(5, block_definitions)
        field.update()
        return field

    @staticmethod
    def create_mouse_example():
        block_definitions = {
            'rows': [[2, 2], [1, 1, 1, 1], [1, 5, 1], [2, 1, 2], [5], [3, 3], [1, 8], [1, 8], [1, 8], [8]],
            'cols': [[3], [2, 1], [1, 1, 5], [1, 8], [2, 6], [3, 4], [2, 6], [1, 8], [1, 1, 5], [2, 3]],
        }
        field = Field(10, block_definitions)
        field.update()
        return field

    @staticmethod
    def create_default_example():
        block_definitions = {
            'rows': [[2, 2], [1, 1], [5], [1, 1, 2], [2, 1, 1, 2],
                     [2, 2, 1], [2, 8], [4, 2, 3], [3, 1], [1, 1, 1],
                     [3, 4, 2], [5, 2, 3, 1], [1, 1, 2, 2, 1], [3, 3, 1], [3, 1]],
            'cols': [[2], [4, 2], [1, 1, 2], [2, 1, 2, 1], [1, 1, 1, 8],
                     [3, 1, 1, 2], [1, 2, 2], [8, 2], [1, 2, 2], [1, 1, 1],
                     [1, 4], [1, 5], [1, 2, 1], [2, 5, 1], [4, 2, 2]],
        }
        field = Field(15, block_definitions)
        field.update()
        return field
