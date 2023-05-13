import tkinter
from tkinter import ttk

class Formatter:
    def __init__(self, input_text):
        self.input_text = input_text

# Site details extracter function
    def extract_data(self):
        lines = self.input_text.strip().split("\n")
        data = {}
        for line in lines:
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
        return Site(data['Host'], data['Ip'], data['Message'], data['Location'])

# Site details extracted to a site class
class Site:
    def __init__(self, host, ip, message, location):
        self.host = host
        self.ip = ip
        self.message = message
        self.location = location

# Email template builder
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

# Whatsapp template builder
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

window = tkinter.Tk()
window.title("PnP Tool v0.6")

# Main Container Frame
frame = tkinter.Frame(window)
frame.pack()

# Top Container Frame
top_container_frame = tkinter.Frame(frame)
top_container_frame.grid(row= 0, column= 0, sticky="news", padx=20, pady=10)

for widget in top_container_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# User Signature Frame
user_signature_frame = tkinter.LabelFrame(top_container_frame, text="Signature")
user_signature_frame.grid(row= 0, column= 0, sticky="news", padx=20, pady=10)

user_name_label = tkinter.Label(user_signature_frame, text="Name")
user_name_label.grid(row=0, column=0)

user_name_entry = tkinter.Entry(user_signature_frame)
user_name_entry.grid(row=0, column=1)

for widget in user_signature_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Nested Actions Frame
nested_actions_frame = tkinter.LabelFrame(top_container_frame, text="Options")
nested_actions_frame.grid(row=0, column=1, sticky="news", padx=20, pady=10)

run_formatter_btn = tkinter.Button(nested_actions_frame, text="Run", command="#")
run_formatter_btn.grid(row=0, column=0)

clear_all_btn = tkinter.Button(nested_actions_frame, text="Clear All", command="#")
clear_all_btn.grid(row=0, column=1)

for widget in nested_actions_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Site Data Container Frame
site_data_frame = tkinter.LabelFrame(frame, text="Site Data")
site_data_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

clipboard_data_label = tkinter.Label(site_data_frame, text="Clipboard")
clipboard_data_label.grid(row=0, column=0)

site_clipboard_data = tkinter.Text(site_data_frame, height=20, width=30)
site_clipboard_data.grid(row=1, column=0)

for widget in site_data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Site Nested Data Frame
nested_site_data_frame = tkinter.Frame(site_data_frame)
nested_site_data_frame.grid(row=1, column=1, sticky="news", padx=20, pady=10)

ticket_ref_label = tkinter.Label(nested_site_data_frame, text="4me Ref:")
ticket_ref_label.grid(row=0, column=0)

ticket_ref_entry = tkinter.Entry(nested_site_data_frame)
ticket_ref_entry.grid(row=0, column=1)

site_contact_label = tkinter.Label(nested_site_data_frame, text="Site Contact:")
site_contact_label.grid(row=1, column=0)

site_contact_entry = tkinter.Entry(nested_site_data_frame)
site_contact_entry.grid(row=1, column=1)

site_feedback_label = tkinter.Label(nested_site_data_frame, text="Site Feedback:")
site_feedback_label.grid(row=2, column=0)

site_feedback_cmb = ttk.Combobox(nested_site_data_frame, values=[" ", "Unable to confirm power", "No contact provided", "Power related issues", "Network related issues"])
site_feedback_cmb.grid(row=2, column=1)

for widget in nested_site_data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Output Container Frame
output_data_frame = tkinter.LabelFrame(frame, text="Output Data")
output_data_frame.grid(row=1, column=1, sticky="news", padx=20, pady=10)

email_output_data_label = tkinter.Label(output_data_frame, text="Formatted eMail:")
email_output_data_label.grid(row=0, column=0)

email_output_data = tkinter.Text(output_data_frame, height=20, width=30)
email_output_data.grid(row=1, column=0)

whatsapp_output_data_label = tkinter.Label(output_data_frame, text="Formatted Whatsapp Message:")
whatsapp_output_data_label.grid(row=0, column=1)

whatsapp_output_data = tkinter.Text(output_data_frame, height=20, width=30)
whatsapp_output_data.grid(row=1, column=1)

for widget in output_data_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)


    def format_input(self):
        # Get the input text from the input widgets
        input_text = self.input_text.get("1.0", "end")
        site_contact = self.site_contact_input.get()
        site_feedback = self.site_feedback_input.get()
        fourme_ref = self.fourme_ref_input.get()
        current_user = self.current_user_input.get()

        # Create a Formatter instance and extract the data
        formatter = Formatter(input_text)
        try:
            site = formatter.extract_data()
        except Exception as e:
            print(f"Error extracting data: {e}")
            return

        # Format the output and display it in the output widget
        try:
            output_text = site.format_output(site_contact, site_feedback, fourme_ref)
        except Exception as e:
            print(f"Error formatting output: {e}")
            return
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", output_text)
        self.output_text.config(state="disabled")

        # Format the output and display it in the new output widget
        try:
            formatted_output_text = site.format_formatted_output(site_contact, site_feedback, fourme_ref, current_user)
        except Exception as e:
            print(f"Error formatting formatted output: {e}")
            return
        self.formatted_output_text.config(state="normal")
        self.formatted_output_text.delete("1.0", "end")
        self.formatted_output_text.insert("1.0", formatted_output_text)
        self.formatted_output_text.config(state="disabled")


    def add_reset_button(self):
        self.reset_button = tk.Button(self, text="Reset", font=("Helvetica", 10), command=self.reset)
        self.reset_button.pack(side="top", fill="x", padx=10, pady=(0, 10))


    def reset(self):
        self.input_text.delete("1.0", tk.END)
        self.output_text.config(state="normal")
        self.output_text.delete("1.0", tk.END)
        self.output_text.config(state="disabled")
        self.formatted_output_text.config(state="normal")
        self.formatted_output_text.delete("1.0", tk.END)
        self.formatted_output_text.config(state="disabled")
        self.site_contact_input.delete(0, tk.END)
        self.site_feedback_input.delete(0, tk.END)
        self.fourme_ref_input.delete(0, tk.END)

window.mainloop()