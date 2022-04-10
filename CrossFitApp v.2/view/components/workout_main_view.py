from tkinter import *
from tkinter import ttk

from controller.workouts_controller import WorkoutController
from view.command.workouts.delete_workout_command import DeleteWorkoutCommand
from view.command.workouts.edit_workout_command import ShowEditWorkoutCommand
from view.command.workouts.show_add_workout import ShowAddWorkoutCommand
from view.components.item_list import ItemList
from view.utils.tkinter_utils import center_resize_window

DEFAULT_COLUMN_WIDTH_PX = 140
SCROLLBAR_WIDTH_PX = 20
BUTTONS_PANEL_HEIGHT_PX = 100


class WorkoutMainView(ttk.Frame):
    def __init__(self, parent, workout_controller: WorkoutController, show_add_workout_command: ShowAddWorkoutCommand,
                 edit_workout_command: ShowEditWorkoutCommand, delete_workout_command: DeleteWorkoutCommand):
        super().__init__(parent, padding='3 3 12 12')
        self.workout_controller = workout_controller
        self.show_add_workout_command = show_add_workout_command
        self.edit_workout_command = edit_workout_command
        self.delete_workout_command = delete_workout_command
        self.parent = parent
        self.grid(row=0, column=0, sticky='NSEW')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

        items = workout_controller.get_all_workouts()
        self.item_list = ItemList(self, items)
        self.grid(column=0, row=0, sticky='NSEW')

        self.item_list.update_idletasks()
        print(self.item_list.winfo_width(), self.item_list.winfo_height())
        center_resize_window(parent,
                             self.item_list.winfo_width(),
                             self.item_list.winfo_height() + BUTTONS_PANEL_HEIGHT_PX)

        buttons_frame = ttk.Frame(self, padding='20 10 20 10')
        buttons_frame.grid(column=0, row=1, sticky='NSEW')
        self.add_button = ttk.Button(buttons_frame, text='Add Workout', padding=10, command=self.show_add_workout_command)
        self.add_button.grid(column=1, row=0, sticky='N, E', padx=40, pady=40)
        self.add_button = ttk.Button(buttons_frame, text='Edit Workout', padding=10, command=self.edit_workout_command)
        self.add_button.grid(column=2, row=0, sticky='N, E', padx=40, pady=40)
        self.add_button = ttk.Button(buttons_frame, text='Delete Workout', padding=10, command=self.delete_workout_command)
        self.add_button.grid(column=3, row=0, sticky='N, E', padx=40, pady=40)

        rows, cols = buttons_frame.grid_size()
        for col in range(cols):
            buttons_frame.columnconfigure(col, minsize=300, pad=30)

    def delete_selected(self):
        items = self.item_list.get_selected_items()
        ids = list(map(lambda item: item[0], items))
        print(ids)

    def refresh(self):
        workouts = self.workout_controller.get_all_workouts()
        self.item_list.set_items(workouts)
