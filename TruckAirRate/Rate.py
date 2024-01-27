import ttkbootstrap as tb
import tkinter as tk
from tkinter import ttk

class Start:
    def OpenWindow(self):
        self.weight = 0
        self.total = 0
        self.air_total = 0
        StartApp = tb.Window(themename="darkly")
        StartApp.geometry("300x300")
        StartApp.title("Rate Calculator")
        StartApp.iconbitmap("CacuCutie.ico")

        # Trucking Cal
        Truck_label = tk.Label(text="Expeditors Seattle Trucking Calculator")
        Truck_label.pack()
        
        

        # Weight
        weight_label = tk.Label(text="Weight:")
        weight_label.pack()
        self.weight_entry = tk.Entry(StartApp)  # Make weight_entry an instance variable
        self.weight_entry.pack()

        # Distance drop down
        self.Distance = ["1- 50", "51 - 100", "101 - 250", "251 - 500", "501 - 1000", "1000 +"]
        self.dist_combobox = ttk.Combobox(StartApp, values=self.Distance)
        self.dist_combobox.pack()

        # Create a button
        calculate_button = tk.Button(StartApp, text="Calculate", command=self.calculate)
        calculate_button.pack()

        # Initialize a label for displaying the result
        self.resultTruck_label = tk.Label(StartApp, text="")
        self.resultTruck_label.pack()

        dest_label = tk.Label(text="Destinations")
        dest_label.pack()

        self.destinations = ["DXB", "IST", "AUH", "TPE", "DOH", "TLV", "MCT", "KWI",
                        "ANK", "DAC", "BUH", "TLL", "LHR"]
        self.dest_combobox = ttk.Combobox(StartApp, values=self.destinations)
        self.dest_combobox.pack()

        # Urgency
        urgency_label = tk.Label(text="Urgency")
        urgency_label.pack()

        self.urgency = ["Critical", "Direct", "Consolidated"]
        self.urgency_combobox = ttk.Combobox(StartApp, values=self.urgency)
        self.urgency_combobox.pack()

        # Create a button
        calculate_button = tk.Button(StartApp, text="Calculate", command=self.AirandUrgency)
        calculate_button.pack()

        # Initialize a label for displaying the result
        self.resultAir_label = tk.Label(StartApp, text="")
        self.resultAir_label.pack()

        

        #Label for Trucking + Air Rate 
        self.total_amount_label = tk.Label(StartApp, text="")
        self.total_amount_label.pack()

        StartApp.mainloop()

    

    def calculate(self):
        try:
            selected_distance = self.dist_combobox.get()
            total = 0
            self.weight = float(self.weight_entry.get())  # Get the weight from the Entry widget as a float

            Min_Trucking_Charge = 42.00
            TruckDistancecharge1 = 0.19  # 1 - 50

            TruckDistancecharge2 = 52.00  # Min Rate for over 51 KM
            TruckDistancecharge3 = 0.21  # 51 - 100

            TruckDistancecharge4 = 62.75  # Min Rate for over 101 KM
            TruckDistancecharge5 = 0.24  # 101 - 250

            TruckDistancecharge6 = 141.00  # Min Rate for over 251 KM
            TruckDistancecharge7 = 0.64  # 251 - 1000
            easy = "Trucking"

            if selected_distance == "1 - 50":
                if (self.weight * TruckDistancecharge1) > Min_Trucking_Charge:
                    total = self.weight * TruckDistancecharge1
                    self.resultTruck_label.config(text=easy + f" Charge: {total:.2f}") 
                else:
                    total = self.weight + Min_Trucking_Charge 
                    self.resultTruck_label.config(text=easy + f" Charge: {total:.2f}")
            else:
                self.resultTruck_label.config(text="Invalid Weight")

                self.TotalValue()
                self.AirandUrgency()
        except ValueError:
            self.resultTruck_label.config(text="Invalid Input")


    def AirandUrgency(self):
        try:
            selected_destination = self.dest_combobox.get()
            selected_urgency = self.urgency_combobox.get()
            
            # DXB Rates Direct
            min_rate = 195.00
            charge2DXBDirect = 3.52
            charge3DXBDirect = 2.61
            charge4DXBDirect = 2.14
            charge5DXBDirect = 2.01
            charge6DXBDirect = 1.91
            charge7DXBDirect = 1.86

            if selected_destination == "DXB" and selected_urgency == "Direct":
                if 1 <= self.weight < 35:
                    air_total = self.weight * charge2DXBDirect
                    self.resultAir_label.config(text=f"Air Charge: {air_total:.2f}")
                elif 1 > self.weight:
                    air_total = self.weight + min_rate
                    self.resultAir_label.config(text=f"Air Charge: {air_total:.2f}")
                else:
                    self.resultAir_label.config(text="Invalid Weight")
                self.TotalValue()

        except ValueError:
            self.resultAir_label.config(text="Invalid Input")

    def TotalValue(self):
        air_total = 0
        truck_total = 0

        try:
            air_total = float(self.resultAir_label.cget("text").split(":")[1])  # Extract air_total from the Air Charge label
            truck_total = float(self.resultTruck_label.cget("text").split(":")[1])  # Extract trucking total from the Trucking Charge label
            total_value = air_total + truck_total
            self.total_amount_label.config(text=f"Total Amount: {total_value:.2f}")
        except ValueError:
            self.total_amount_label.config(text="Invalid Input")

       


Application = Start()
Application.OpenWindow()
