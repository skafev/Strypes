from tkinter import *
from tkinter import ttk

from controller.workouts_controller import WorkoutController
from view.command.exit_command import ExitCommand
from view.command.load_data_command import LoadDataCommand
from view.command.save_data_command import SaveDataCommand
from view.command.workouts.delete_workout_command import DeleteWorkoutCommand
from view.command.workouts.edit_workout_command import ShowEditWorkoutCommand
from view.command.workouts.list_workout_command import ListWorkoutCommand
from view.command.workouts.show_add_workout import ShowAddWorkoutCommand
from view.components.workout_main_view import WorkoutMainView
from view.utils.tkinter_utils import print_hierarchy


class MainView(ttk.Frame):
    def __init__(self, root, workout_controller: WorkoutController):
        super().__init__(root, padding='3 3 12 12')
        self.root = root
        self.workout_controller = workout_controller

        self.menubar = Menu(root)
        root['menu'] = self.menubar
        root.option_add('*tearOff', False)

        menu_file = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_file, label='File', underline=0)
        menu_file.add_command(label='Load Data', command=LoadDataCommand())
        menu_file.add_command(label='Save Data', command=SaveDataCommand())
        menu_file.add_separator()
        exit_command = ExitCommand(root)
        menu_file.add_command(label='Exit', command=exit_command, underline=1, accelerator='Ctrl-Shift-X')
        root.bind_all('<Control-Shift-KeyPass-X>', exit_command)

        self.show_add_workout_command = ShowAddWorkoutCommand(workout_controller)
        self.show_edit_workout_command = ShowEditWorkoutCommand(workout_controller)
        self.delete_workout_command = DeleteWorkoutCommand(workout_controller)
        self.list_workouts_command = ListWorkoutCommand(workout_controller)

        menu_workouts = Menu(self.menubar)
        self.menubar.add_cascade(menu=menu_workouts, label='Workouts', underline=0)
        menu_workouts.add_command(label='List Workouts', command=self.list_workouts_command)
        menu_workouts.add_separator()
        menu_workouts.add_command(label='Add Workout', command=self.show_add_workout_command)
        menu_workouts.add_command(label='Edit Workout', command=self.show_edit_workout_command)
        menu_workouts.add_command(label='Delete Workout', command=self.delete_workout_command)

        self.item_list = WorkoutMainView(self.root,self.workout_controller,self.show_add_workout_command,
                                         self.show_edit_workout_command, self.delete_workout_command)

        print_hierarchy(root)

    def refresh(self):
        self.item_list.refresh()




