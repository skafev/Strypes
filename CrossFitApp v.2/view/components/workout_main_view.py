from tkinter import *
from tkinter import ttk

from controller.workouts_controller import WorkoutController
from view.command.workouts.delete_workout_command import DeleteWorkoutCommand
from view.command.workouts.edit_workout_command import ShowEditWorkoutCommand
from view.command.workouts.show_add_workout import ShowAddWorkoutCommand


class WorkoutMainView(ttk.Frame):
    def __init__(self, parent, workout_controller: WorkoutController, show_add_workout_command: ShowAddWorkoutCommand,
                 edit_workout_command: ShowEditWorkoutCommand, delete_workout_command: DeleteWorkoutCommand):
        super().__init__(parent, padding='3 3 12 12')
        self.workout_controller = workout_controller
        self.show_add_workout_command = show_add_workout_command
        self.edit_workout_command = edit_workout_command
        self.delete_workout_command = delete_workout_command
        self.grid(row=0, column=0, sticky='NSEW')
        parent.rowconfigure(0, weight=1, minsize=300, pad=30)
        parent.columnconfigure(0, weight=1, minsize=300, pad=30)

        items = workout_controller.get_all_workouts()
        self.item_list = ItemList(self, items)
