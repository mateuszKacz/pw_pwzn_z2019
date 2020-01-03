import tkinter as tk
from functools import partial
import pygame as pg

from lab_9.tools.calculator import Calculator


class CalculatorGUI(tk.Frame):
    def __init__(self, master=None, *args, **kwargs):
        tk.Frame.__init__(self, master, *args, **kwargs)

        self.variables = {}
        self.state = tk.BooleanVar(value=True)
        self.init_variables()
        self.calculator = Calculator(self)

        self.screen = tk.Label(self, bg='white')
        self.screen.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.bottom_pad = self.init_bottom_pad()
        self.bottom_pad.pack(side=tk.BOTTOM)

        # oblsuga klawiatury
        pg.init()
        pg.display.init()
        pg.display.set_mode((1, 1))
        self.check_key()


    def init_variables(self):
        self.variables['var_1'] = ''
        self.variables['var_2'] = ''
        self.variables['operator'] = ''
        self.state.set(True)

    def init_bottom_pad(self):
        bottom_pad = tk.Frame(self)

        functions_pad = tk.Frame(bottom_pad)
        functions_pad.pack(side=tk.LEFT)

        # klwiatura funckcji
        MC_b = tk.Button(functions_pad, text='MC', width=5, command=self.calculator.clean_memory).grid(row=0, column=0)
        MR_b = tk.Button(functions_pad, text='MR', width=5, command=self.calculator.in_memory).grid(row=1, column=0)
        Mplus_b = tk.Button(functions_pad, text='M+', width=5, command=self.calculator.memorize).grid(row=2, column=0)
        clear_b = tk.Button(functions_pad, text='C', width=5, command=self.clear).grid(row=4, column=0)

        # klawiatura numeryczna
        num_pad = tk.Frame(bottom_pad)
        num_pad.pack(side=tk.LEFT)
        ii = 0
        for ii, num in enumerate(range(9, 0, -1)):
            tk.Button(
                num_pad, text=num, width=5,
                command=partial(self.update_var, num)
            ).grid(row=ii // 3, column=(2-ii) % 3)
        ii += 1
        tk.Button(
            num_pad, text='.', width=5,
            command=partial(self.update_var, '.')
        ).grid(row=ii // 3, column=ii % 3)
        ii += 1
        tk.Button(
            num_pad, text='0', width=5,
            command=partial(self.update_var, '0')
        ).grid(row=ii // 3, column=ii % 3)
        ii += 1
        tk.Button(
            num_pad, text='=', width=5,
            command=self.calculate_result
        ).grid(row=ii // 3, column=ii % 3)

        # klawiatura operacji
        operation_pad = tk.Frame(bottom_pad)
        operation_pad.pack(side=tk.RIGHT)
        for ii, operation in enumerate(self.calculator.operations.keys()):
            tk.Button(
                operation_pad, text=operation, width=5,
                command=partial(self.set_operator, operation),
            ).grid(row=ii, column=0)

        return bottom_pad

    def update_screen(self):
        text = f"{self.variables['var_1']}"
        if self.variables['operator']:
            text += f" {self.variables['operator']}"
        if self.variables['var_2']:
            text += f" {self.variables['var_2']}"
        self.screen['text'] = text

    def clear(self):
        state = self.state.get()
        if state:
            self.variables['var_1'] = ''
        else:
            self.variables['var_2'] = ''
        self.update_screen()

    def update_var(self, num):
        state = self.state.get()
        if state:
            self.variables['var_1'] += str(num)
            self.variables['var_1'] = self.variables['var_1'].lstrip('0')
        else:
            self.variables['var_2'] += str(num)
            self.variables['var_2'] = self.variables['var_2'].lstrip('0')
        self.update_screen()

    def set_operator(self, operator):
        if self.variables['var_1']:
            self.variables['operator'] = operator
            self.state.set(not self.state.get())
            self.update_screen()

    def calculate_result(self):
        if self.variables['var_1'] and self.variables['var_2']:
            var_1 = float(self.variables['var_1'])
            var_2 = float(self.variables['var_2'])
            self.screen['text'] = self.calculator.run(
                self.variables['operator'], var_1, var_2
            )
            self.init_variables()

    def check_key(self):
        """Funckja obluguje klawiature"""
        events = pg.event.get()

        for event in events:
            if event.type == pg.KEYDOWN:

                if event.key == pg.K_0:
                    self.update_var(0)
                elif event.key == pg.K_1:
                    self.update_var(1)
                elif event.key == pg.K_2:
                    self.update_var(2)
                elif event.key == pg.K_3:
                    self.update_var(3)
                elif event.key == pg.K_4:
                    self.update_var(4)
                elif event.key == pg.K_5:
                    self.update_var(5)
                elif event.key == pg.K_6:
                    self.update_var(6)
                elif event.key == pg.K_7:
                    self.update_var(7)
                elif event.key == pg.K_8:
                    self.update_var(8)
                elif event.key == pg.K_9:
                    self.update_var(9)
                elif event.key == pg.K_ASTERISK:
                    self.set_operator('*')
                elif event.key == pg.K_SLASH:
                    self.set_operator('/')
                elif event.key == pg.K_PLUS:
                    self.set_operator('+')
                elif event.key == pg.K_MINUS:
                    self.set_operator('-')
                elif event.key == pg.K_KP_ENTER:
                    self.calculate_result()
                else:
                    print('Wrong key!')

        self.after(100, func=self.check_key)


if __name__ == '__main__':
    root = tk.Tk()
    CalculatorGUI(root).pack()
    root.mainloop()