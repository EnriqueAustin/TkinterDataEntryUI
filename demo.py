import tkinter as tk
from tkinter import ttk

class Formatter:
    def __init__(self, input_text):
        self.input_text = input_text

    def extract_data(self):
        lines = self.input_text.strip().split("\n")
        data = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
        return Site(data['Host'], data['Ip'], data['Message'], data['Location'])

class Site:
    def __init__(self, host, ip, message, location):
        self.host = host
        self.ip = ip
        self.message = message
        self.location = location

    def format_output(self, site_contact, site_feedback, fourme_ref):
        output_text = "Hi all,\n\nThe following site is reporting down/unreachable:\n\n"
        output_text += f"Site contact: {site_contact}\nSite feedback: {site_feedback}\n\n"
        output_text += f"Host: {self.host}\n"
        output_text += f"Ip: {self.ip}\n"
        output_text += f"Message: {self.message}\n"
        output_text += f"Location: {self.location}\n\n"
        output_text += f"4me Ref: {fourme_ref}\n"
        output_text += "Assigned to: DD Networks"
        return output_text

    def format_formatted_output(self, site_contact, site_feedback, fourme_ref, current_user):
        formatted_output_text = "Hi all,\n\nThe following site is reporting down/unreachable:\n\n"
        formatted_output_text += f"Site contact: {site_contact}\nSite feedback: {site_feedback}\n\n"
        formatted_output_text += f"Host: {self.host}\n"
        formatted_output_text += f"Ip: {self.ip}\n"
        formatted_output_text += f"Message: {self.message}\n"
        formatted_output_text += f"Location: {self.location}\n\n"
        formatted_output_text += f"4me Ref: {fourme_ref}\n"
        formatted_output_text += "Assigned to: DD Networks\n\n"
        formatted_output_text += f"Kind regards,\n{current_user}"
        return formatted_output_text

class App:
    def __init__(self, window):
        self.window = window
        self.window.title("PnP Tool v0.6")
        self.create_widgets()

    def create_widgets(self):
        # Main Container Frame
        self.frame = tk.Frame(self.window)
        self.frame.pack()

        # Top Container Frame
        self.top_container_frame = tk.Frame(self.frame)
        self.top_container_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        # User Signature Frame
        self.user_signature_frame = tk.LabelFrame(self.top_container_frame, text="Signature")
        self.user_signature_frame.grid(row=0, column=0, sticky="news", padx=20, pady=10)

        self.user_name_label = tk.Label(self.user_signature_frame, text="Name")
        self.user_name_label.grid(row=0, column=0)

        self.user_name_entry = tk.Entry(self.user_signature_frame)
        self.user_name_entry.grid(row=0, column=1)

        # Nested Actions Frame
        self.nested_actions_frame = tk.LabelFrame(self.top_container_frame, text="Options")
        self.nested_actions_frame.grid(row=0, column=1, sticky="news", padx=20, pady=10)

        self.run_formatter_btn = tk.Button(self.nested_actions_frame, text="Run", command=self.format_input)
        self.run_formatter_btn.grid(row=0, column=0)

        self.clear_all_btn = tk.Button(self.nested_actions_frame, text="Clear All", command=self.reset)
        self.clear_all_btn.grid(row=0, column=1)

        # Site Data Container Frame
        self.site_data_frame = tk.LabelFrame(self.frame, text="Site Data")
        self.site_data_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

        self.clipboard_data_label = tk.Label(self.site_data_frame, text="Clipboard")
        self.clipboard_data_label.grid(row=0, column=0)

        self.site_clipboard_data = tk.Text(self.site_data_frame, height=20, width=30)
        self.site_clipboard_data.grid(row=1, column=0)

        # Site Nested Data Frame
        self.nested_site_data_frame = tk.Frame(self.site_data_frame)
        self.nested_site_data_frame.grid(row=1, column=1, sticky="news", padx=20, pady=10)

        self.ticket_ref_label = tk.Label(self.nested_site_data_frame, text="4me Ref:")
        self.ticket_ref_label.grid(row=0, column=0)

        self.ticket_ref_entry = tk.Entry(self.nested_site_data_frame)
        self.ticket_ref_entry.grid(row=0, column=1)

        self.site_contact_label = tk.Label(self.nested_site_data_frame, text="Site Contact:")
        self.site_contact_label.grid(row=1, column=0)

        self.site_contact_entry = tk.Entry(self.nested_site_data_frame)
        self.site_contact_entry.grid(row=1, column=1)

        self.site_feedback_label = tk.Label(self.nested_site_data_frame, text="Site Feedback:")
        self.site_feedback_label.grid(row=2, column=0)

        self.site_feedback_cmb = ttk.Combobox(self.nested_site_data_frame,
                                              values=[" ", "Unable to confirm power", "No contact provided",
                                                      "Power related issues", "Network related issues"])
        self.site_feedback_cmb.grid(row=2, column=1)

        # Output Container Frame
        self.output_data_frame = tk.LabelFrame(self.frame, text="Output Data")
        self.output_data_frame.grid(row=1, column=1, sticky="news", padx=20, pady=10)
        self.email_output_data_label = tk.Label(self.output_data_frame, text="Formatted eMail:")
        self.email_output_data_label.grid(row=0, column=0)

        self.email_output_data = tk.Text(self.output_data_frame, height=20, width=30)
        self.email_output_data.grid(row=1, column=0)

        self.whatsapp_output_data_label = tk.Label(self.output_data_frame, text="Formatted Whatsapp Message:")
        self.whatsapp_output_data_label.grid(row=0, column=1)

        self.whatsapp_output_data = tk.Text(self.output_data_frame, height=20, width=30)
        self.whatsapp_output_data.grid(row=1, column=1)

        # Configure grid padding for all widget in all frames
        for frame in [self.top_container_frame, self.user_signature_frame, self.nested_actions_frame,
                      self.site_data_frame, self.nested_site_data_frame, self.output_data_frame]:
            for widget in frame.winfo_children():
                widget.grid_configure(padx=10, pady=5)

    def format_input(self):
        # Get the input text from the input widgets
        input_text = self.site_clipboard_data.get("1.0", "end")
        site_contact = self.site_contact_entry.get()
        site_feedback = self.site_feedback_cmb.get()
        fourme_ref = self.ticket_ref_entry.get()
        current_user = self.user_name_entry.get()

        # Create a Formatter instance and extract the data
        formatter = Formatter(input_text)
        try:
            site = formatter.extract_data()
        except Exception as e:
            print(f"Error extracting data: {e}")
            return

        # Format the output and display it in the email output widget
        try:
            output_text = site.format_output(site_contact, site_feedback, fourme_ref)
        except Exception as e:
            print(f"Error formatting output: {e}")
            return
        self.email_output_data.delete("1.0", "end")
        self.email_output_data.insert("1.0", output_text)

        # Format the output and display it in the whatsapp output widget
        try:
            formatted_output_text = site.format_formatted_output(site_contact, site_feedback, fourme_ref, current_user)
        except Exception as e:
            print(f"Error formatting formatted output: {e}")
            return
        self.whatsapp_output_data.delete("1.0", "end")
        self.whatsapp_output_data.insert("1.0", formatted_output_text)

    def reset(self):
        self.site_clipboard_data.delete("1.0", "end")
        self.email_output_data.delete("1.0", "end")
        self.whatsapp_output_data.delete("1.0", "end")
        self.site_contact_entry.delete(0, "end")
        self.site_feedback_cmb.set("")
        self.ticket_ref_entry.delete(0, "end")
        #self.user_name_entry.delete(0, "end")

window = tk.Tk()
app = App(window)
window.mainloop()