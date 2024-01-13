import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
from datetime import datetime

class EventSchedulingApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Event Scheduling App")
        self.window.geometry("700x500")
        self.event_data = {}
        self.responses = {}
        self.create_event_screen()

    def create_event_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        tk.Label(self.window, text="Event Title:").pack()
        self.event_title_entry = tk.Entry(self.window)
        self.event_title_entry.pack()

        tk.Label(self.window, text="Select Dates:").pack()
        self.calendar = Calendar(self.window, selectmode='day', font="Arial 14", 
                                 normalforeground='black', weekendforeground='red', 
                                 othermonthforeground='gray', othermonthwebackground='white',
                                 showweeknumbers=False, 
                                 selectbackground='blue', selectforeground='white')
        self.calendar.pack(padx=10, pady=10)

        self.selected_dates = []
        tk.Button(self.window, text="Add Date", command=self.add_date).pack()

        self.dates_frame = tk.Frame(self.window)
        self.dates_frame.pack()

        tk.Button(self.window, text="Start Scheduling", command=self.start_scheduling).pack()

    def add_date(self):
        date = self.calendar.get_date()
        formatted_date = self.format_date(date)
        if formatted_date not in self.selected_dates:
            self.selected_dates.append(formatted_date)
            self.refresh_dates_frame()

    def format_date(self, date_str):
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        return date_obj.strftime('%Y年%m月%d日')

    def refresh_dates_frame(self):
        for widget in self.dates_frame.winfo_children():
            widget.destroy()

        for date in self.selected_dates:
            date_frame = tk.Frame(self.dates_frame)
            tk.Label(date_frame, text=date).pack(side=tk.LEFT)
            tk.Button(date_frame, text="Delete", command=lambda d=date: self.delete_date(d)).pack(side=tk.LEFT)
            date_frame.pack()

    def delete_date(self, date):
        self.selected_dates.remove(date)
        self.refresh_dates_frame()

    def start_scheduling(self):
        title = self.event_title_entry.get()
        if not title or not self.selected_dates:
            messagebox.showerror("Error", "Please enter a title and select at least one date.")
            return

        self.event_data['title'] = title
        self.event_data['dates'] = self.selected_dates
        self.participant_input_screen()

    def participant_input_screen(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        tk.Label(self.window, text="Your Name:").pack()
        self.participant_name_entry = tk.Entry(self.window)
        self.participant_name_entry.pack()

        self.date_vars = {}
        for date in self.event_data['dates']:
            frame = tk.Frame(self.window)
            tk.Label(frame, text=date).pack(side=tk.LEFT)

            var = tk.StringVar(value='×')  # デフォルト値を「×」に設定
            self.date_vars[date] = var
            tk.Radiobutton(frame, text="○", variable=var, value='○').pack(side=tk.LEFT)
            tk.Radiobutton(frame, text="×", variable=var, value='×').pack(side=tk.LEFT)

            frame.pack()

        tk.Button(self.window, text="Submit Response", command=self.submit_response).pack()
        tk.Button(self.window, text="Show Results", command=self.show_results).pack()

    def submit_response(self):
        name = self.participant_name_entry.get()
        if not name:
            messagebox.showerror("Error","Please enter your name.")
            return
        response = {date: self.date_vars[date].get() == '○' for date in self.event_data['dates']}
        self.responses[name] = response

        messagebox.showinfo("Success", "Response submitted successfully!")
        self.participant_input_screen()

    def show_results(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        tk.Label(self.window, text=f"Results for '{self.event_data['title']}':").pack()
        date_counts = {date: sum(responses.get(date, False) for responses in self.responses.values()) for date in self.event_data['dates']}
        
        for date, count in date_counts.items():
            tk.Label(self.window, text=f"{date}: {count} participants").pack()

        max_date = max(date_counts, key=date_counts.get, default=None)
        if max_date is not None:
            tk.Label(self.window, text=f"Best date: {max_date} with {date_counts[max_date]} participants").pack()
        else:
            tk.Label(self.window, text="No dates were selected by participants").pack()

        tk.Button(self.window, text="Restart", command=self.create_event_screen).pack()
        tk.Button(self.window, text="Exit", command=self.window.quit).pack()

    def start(self):
        self.window.mainloop()

if __name__ == "__main__":
  app = EventSchedulingApp()
  app.start()
