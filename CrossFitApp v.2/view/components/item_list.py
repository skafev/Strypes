from tkinter import ttk
from tkinter import *

DEFAULT_COLUMN_WIDTH_PX = 140


class ItemList(ttk.Frame):
    def __init__(self, parent, items):
        super().__init__(parent, padding='3 3 12 12')
        self.parent = parent
        self.items = items
        self.item_pos_ids = None
        self.grid(row=0, column=0, sticky='NSEW')

        columns = tuple(self.items[0].__dict__.keys())
        self.tree = ttk.Treeview(self, columns=columns, selectmode='extended', show='headings')

        for column in columns:
            self.tree.heading(column, text=column.title())
            self.tree.column(column, width=DEFAULT_COLUMN_WIDTH_PX)

        self.tree.grid(row=0, column=0, sticky='NSEW')

        vsb = ttk.Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        vsb.grid(row=0, column=1, sticky='NSEW', padx=0)
        self.tree.configure(yscroll=vsb.set)

        self.tree.update_idletasks()
        print(self.tree.winfo_width(), self.tree.winfo_height())
        self.rowconfigure(0, weight=1, minsize=self.tree.winfo_height())
        self.columnconfigure(0, weight=1, minsize=self.tree.winfo_width())

        self.set_items(self.items)

    def set_items(self, items):
        def set_item(item):
            values = list(item.__dict__.values())
            for i, val in enumerate(values):
                if isinstance(val, (list, tuple)):
                    values[i] = ' '.join(val)
            return self.tree.insert('', END, values=tuple(values))

        if self.item_pos_ids is not None:
            self.tree.delete(*self.item_pos_ids)
        self.items = items
        self.item_pos_ids = list(map(set_item, self.items))
        self.update_idletasks()
        self.tree.see(self.item_pos_ids[-1])

    def get_selected_items(self):
        items = []
        for sel_item in self.tree.selection():
            items.append(self.tree.item(sel_item, 'values'))
        return items






