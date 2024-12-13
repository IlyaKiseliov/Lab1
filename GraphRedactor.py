import tkinter as tk
from tkinter import simpledialog

class Shape:

    def draw(self,canvas):
        raise NotImplementedError("Метод draw должен быть переопределен в подклассе")

class Point(Shape):
    def __init__(self, canvas, x, y):
        self.x = x
        self.y = y

    def draw(self,canvas):
        canvas.create_oval(self.x - 2, self.y - 2, self.x + 2, self.y + 2, fill='black')

class Circle(Shape):
    def __init__(self, canvas, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def draw(self,canvas):
        canvas.create_oval(self.x - self.radius, self.y - self.radius,
                                self.x + self.radius, self.y + self.radius,
                                outline='black')

class Square(Shape):
    def __init__(self, canvas, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def draw(self,canvas):
        canvas.create_rectangle(self.x - self.side / 2, self.y - self.side / 2,
                                      self.x + self.side / 2, self.y + self.side / 2,
                                      outline='black')

class GraphicEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Графический редактор")

        self.canvas = tk.Canvas(self.root, width=600, height=400, bg='white')
        self.canvas.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.dot_button = tk.Button(self.button_frame, text="Рисовать точку", command=self.add_point_mode)
        self.dot_button.pack(side=tk.LEFT)

        self.circle_button = tk.Button(self.button_frame, text="Рисовать круг", command=self.draw_circle_mode)
        self.circle_button.pack(side=tk.LEFT)

        self.square_button = tk.Button(self.button_frame, text="Рисовать квадрат", command=self.draw_square_mode)
        self.square_button.pack(side=tk.LEFT)

        self.connect_button = tk.Button(self.root, text="Соединить точки", command=self.connect_points)
        self.connect_button.pack()

        self.btn_clear = tk.Button(self.root, text="Очистить холст", command=self.clear_canvas)
        self.btn_clear.pack(side=tk.LEFT)

        self.mode = 'point'
        self.shapes = []  

        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def add_point_mode(self):
        self.mode = 'point'

    def draw_circle_mode(self):
        self.mode = 'circle'

    def draw_square_mode(self):
        self.mode = 'square'

    def on_canvas_click(self, event):
        if self.mode == 'point':
            point = Point(self.canvas, event.x, event.y)
            point.draw(self.canvas)
            self.shapes.append(point)
        elif self.mode == 'circle':
            radius = simpledialog.askinteger("Введите радиус", "Радиус круга:", minvalue=1)
            if radius is not None:
                circle = Circle(self.canvas, event.x, event.y, radius)
                circle.draw(self.canvas)
                self.shapes.append(circle)

        elif self.mode == 'square':
            side = simpledialog.askinteger("Введите размер", "Размер квадрата:", minvalue=1)
            if side is not None:
                square = Square(self.canvas, event.x, event.y, side)
                square.draw(self.canvas)
                self.shapes.append(square)

    def connect_points(self):
        points_to_connect = [(shape.x, shape.y) for shape in self.shapes if isinstance(shape, Point)]
        if len(points_to_connect) > 1:
            for i in range(len(points_to_connect) - 1):
                self.canvas.create_line(points_to_connect[i], points_to_connect[i + 1], fill='black')
                
    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes.clear()
        self.points.clear()


if __name__ == "__main__":
    root = tk.Tk()
    app = GraphicEditor(root)
    root.mainloop()
