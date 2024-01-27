#Exp Sea Truck and Air Rate Caculator
#Tim Williams
#01-19-2024
#Python

import tkinter as tk
import ttkbootstrap as tb
from tkinter import ttk

class beginApp:

    def openWindow(self):
        #openWindow has built in python libaries helping to display the GUI (Graphical User Interface)

        self.Caculating_App = tb.Window(themename="darkly")
        self.Caculating_App.geometry("220x385")
        self.Caculating_App.title("Exp Rates")
        self.Caculating_App.iconbitmap("favicon.ico")
        self.gatherEntryApps()
        self.Caculating_App.mainloop() #Keeps the App running

    def gatherEntryApps(self):

        #Distance Label
        self.distance = tb.Label(self.Caculating_App, text="Distance Truck Traveled KM:")
        self.distance.pack()

        #Distance Entry 
        self.DistanceKM = ["1 - 50", "51 - 100", "101 - 250", "251 - 500", "501 - 1000", "1000 +"]
        self.dist_combobox = ttk.Combobox(self.Caculating_App, values=self.DistanceKM)
        self.dist_combobox.pack()

        #Weight Label
        self.weight = tb.Label(self.Caculating_App, text="Weight of product:")
        self.weight.pack()

        #Weight Entry
        self.weight_enter = tb.Entry(self.Caculating_App)
        self.weight_enter.pack()

        #Import Lane Labels
        self.import_lanes = tb.Label(self.Caculating_App, text="Traveling From:")
        self.import_lanes.pack()

        #Traveling From Import Lanes
        self.import_EXP = ["SEA", "ANK", "AUH", "BUH", "DAC", "DOH", "DXB", "IST", "IZM", "KWI", "MCT", "TLV", "TPE"]
        self.importdest_combobox = ttk.Combobox(self.Caculating_App, values=self.import_EXP)
        self.importdest_combobox.pack()

        #Export Lane Labels
        self.export_lanes = tb.Label(self.Caculating_App, text="Traveling To:")
        self.export_lanes.pack()

        #Traveling In Export Lanes
        self.destinations_EXP = ["DXB", "IST", "AUH", "TPE", "DOH", "TLV", "MCT", "KWI", 
                                "ANK", "DAC", "BUH", "TLL", "LHR", "SEA"] 
        self.dest_combobox = ttk.Combobox(self.Caculating_App, values=self.destinations_EXP) #These Indicate the Export Lanes for Exp Sea, --- More Needed for Import Lanes
        self.dest_combobox.pack()

        #Urgency 
        self.UrgencyLevel = tb.Label(self.Caculating_App, text="Air Urgency")
        self.UrgencyLevel.pack()

        self.urgencyPoints = ["Critical", "Direct", "Consolidated"]
        self.urgency_combobox = ttk.Combobox(self.Caculating_App, values=self.urgencyPoints)
        self.urgency_combobox.pack()

        #Truck Updating Label Result
        self.trucking_value_label = tb.Label(self.Caculating_App, text="SEATTLE Trucking Value:")
        self.trucking_value_label.pack()

        #Air Updating Label Result
        self.air_value_label = tb.Label(self.Caculating_App, text="Air Value:")
        self.air_value_label.pack()

        #Fuel Updating Label Result
        self.fuel_updatingLabel = tb.Label(self.Caculating_App, text="Fuel Charge:")
        self.fuel_updatingLabel.pack()

        #Security Screening Updating Label Result
        self.ScreeningChargeLabel = tb.Label(self.Caculating_App, text="Screening Charge:")
        self.ScreeningChargeLabel.pack()

        #ISS Updating Label Result
        self.ISSRate_Label = tb.Label(self.Caculating_App, text="ISS Rate Charge:")
        self.ISSRate_Label.pack()

        #Updating Label for Total Value of Shipment
        self.totalAirAndTruckValue = tb.Label(self.Caculating_App, text="Total Value:")
        self.totalAirAndTruckValue.pack()

        #Button that Caculates the Values
        self.calculate_button = tk.Button(self.Caculating_App, text="Calculate", command=self.calculateValues)
        self.calculate_button.pack()

        

    def calculateValues(self):
        # Call both trucking and air calculations when the Calculate button is clicked
        self.Caculations()
        self.AirRateCaculations()

        #Fuel Charge Logic #Common Rate for fuel
        fuel_rate = 0.62
        fuel_charge = self.weightTotal * fuel_rate

        #Fuel Rate For IST
        if self.LaneTravelingIn == "IST": 
            fuel_rate = 0.68 
            fuel_charge = self.weightTotal * fuel_rate

        #Fuel Rate For TPE
        if self.LaneTravelingIn =="TPE":
            fuel_rate = 0.54
            fuel_charge = self.weightTotal * fuel_rate

        #Screening Charge Logic
        screen_rate = 0.09
        screen_charge = self.weightTotal * screen_rate

        #ISS Charge Logic
        ISS_rate = 0.29
        ISS_charge = self.weightTotal * ISS_rate

        #Updating Total, Fuel, Screen, Iss - Labels
        total_value = self.totalTruckingValue + self.airTotalValue + ISS_charge + screen_charge + fuel_charge
        self.totalAirAndTruckValue.config(text=f"Total Value: {total_value:.2f}")
        self.fuel_updatingLabel.config(text=f"Fuel Charge: {fuel_charge:.2f}")
        self.ScreeningChargeLabel.config(text=f"Screening Charge: {screen_charge:.2f}")
        self.ISSRate_Label.config(text=f"ISS Rate Charge: {ISS_charge:.2f}")
        


    def Caculations(self):

        #Declare Weight and Total 
        self.totalTruckingValue = 0
        self.weightTotal = float(self.weight_enter.get())
        self.distanceTotal = self.dist_combobox.get()

        #Declare Rates in Variables to Make Easier to Read
        Min_Trucking_Charge = 42.00
        TruckDistancecharge1 = 0.19  # 1 - 50

        TruckDistancecharge2 = 52.00  # Min Rate for over 51 KM
        TruckDistancecharge3 = 0.21  # 51 - 100

        TruckDistancecharge4 = 62.75  # Min Rate for over 101 KM
        TruckDistancecharge5 = 0.24  # 101 - 250

        TruckDistancecharge6 = 141.00  # Min Rate for over 251 KM
        TruckDistancecharge7 = 0.64  # 251 - 1000

        
        
        
        #If logic for Trucking Distance Selected
        if self.distanceTotal == "1 - 50":
            self.distanceTotal = "1 - 50"

        if self.distanceTotal == "51 - 100":
            self.distanceTotal = "51 - 100"

        if self.distanceTotal == "101 - 250":
            self.distanceTotal = "101 - 250"
        
        if self.distanceTotal == "251 - 500" or self.distanceTotal == "501 - 1000" or self.distanceTotal == "1000 +":
            self.distanceTotal = "251 - 500"
            self.distanceTotal = "501 - 1000"
            self.distanceTotal = "1000 +"
        
        


        # If Statement to find the logic calculated based on the selected option
            
        #1 - 50
        if self.distanceTotal == "1 - 50":
        #Caculates Charge
            if (self.weightTotal * TruckDistancecharge1) > Min_Trucking_Charge:
                self.totalTruckingValue = self.weightTotal * TruckDistancecharge1
            else:
                self.totalTruckingValue = Min_Trucking_Charge

        #51 - 100
        if self.distanceTotal == "51 - 100":
        #Caculates Charge
            if (self.weightTotal * TruckDistancecharge3) > TruckDistancecharge2:
                self.totalTruckingValue = self.weightTotal * TruckDistancecharge3
            else:
                self.totalTruckingValue = TruckDistancecharge2

        #101 - 250
        if self.distanceTotal == "101 - 250":
        #Caculates Charge
            if (self.weightTotal * TruckDistancecharge5) > TruckDistancecharge4:
                self.totalTruckingValue = self.weightTotal * TruckDistancecharge5
            else:
                self.totalTruckingValue = TruckDistancecharge4
        
        #251 - 1000+ 
        if self.distanceTotal == "251 - 500" or self.distanceTotal == "501 - 1000" or self.distanceTotal == "1000 +":
        #Caculates Charge
            if (self.weightTotal * TruckDistancecharge7) > TruckDistancecharge6:
                self.totalTruckingValue = self.weightTotal * TruckDistancecharge7
            else:
                self.totalTruckingValue = TruckDistancecharge6
 
    # Update the label with the calculated value
        self.trucking_value_label.config(text=f"SEATTLE Trucking Value: {self.totalTruckingValue:.2f}")

    def AirRateCaculations(self):
        
        #Get the Urgency and Lane Freight is Traveling in
        self.LaneTravelingFrom = self.importdest_combobox.get()
        self.UrgeLev = self.urgency_combobox.get()
        self.LaneTravelingIn = self.dest_combobox.get()
        self.weightValue = float(self.weight_enter.get())
        self.airTotalValue = 0

        #If logic for getting the Urgency Level Correctly
        if self.UrgeLev == "Critical":
            self.UrgeLev = "Critical"

        if self.UrgeLev == "Direct":
            self.UrgeLev = "Direct"
        
        if self.UrgeLev == "Consolidated":
            self.UrgeLev = "Consolidated"

        #If Logic for Lane Traveling From(IMPORTING)
        if self.LaneTravelingFrom == "SEA":
            self.LaneTravelingFrom = "SEA"

        #If Logic for Lane Traveling In(EXPORTING)
        if self.LaneTravelingIn == "DXB":
            self.LaneTravelingIn = "DXB"

        if self.LaneTravelingIn == "IST":
            self.LaneTravelingIn = "IST"

        if self.LaneTravelingIn == "AUH":
            self.LaneTravelingIn = "AUH"

        if self.LaneTravelingIn == "TPE":
            self.LaneTravelingIn = "TPE"

        if self.LaneTravelingIn == "DOH":
            self.LaneTravelingIn = "DOH"

        if self.LaneTravelingIn == "TLV":
            self.LaneTravelingIn = "TLV"

        if self.LaneTravelingIn == "MCT":
            self.LaneTravelingIn = "MCT"

        if self.LaneTravelingIn == "KWI":
            self.LaneTravelingIn = "KWI"

        if self.LaneTravelingIn == "ANK":
            self.LaneTravelingIn = "ANK"

        if self.LaneTravelingIn == "DAC":
            self.LaneTravelingIn = "DAC"

        if self.LaneTravelingIn == "BUH":
            self.LaneTravelingIn = "BUH"

        if self.LaneTravelingIn == "TLL":
            self.LaneTravelingIn = "TLL"

        if self.LaneTravelingIn == "LHR":
            self.LaneTravelingIn = "LHR"

        if self.LaneTravelingIn == "SEA":
            self.LaneTravelingIn = "SEA"

        #DXB Critical Rates
        DXBCriticalRate_min = 250.00

        DXBCriticalRate1 = 5.92 #35- and 35+ 

        DXBCriticalRate2 = 3.87 #70+

        DXBCriticalRate3 = 3.27 #150+

        DXBCriticalRate4 = 3.12 #300+

        DXBCriticalRate5 = 3.04 #500+

        DXBCriticalRate6 = 2.87 #1000+

        #DXB Direct Rates
        DXBDirectRate_min = 195.00

        DXBDirectRate1 = 3.52 #35- and 35+

        DXBDirectRate2 = 2.61 #70+

        DXBDirectRate3 = 2.14 #150+

        DXBDirectRate4 = 2.01 #300+

        DXBDirectRate5 = 1.91 #500+

        DXBDirectRate6 = 1.86 #1000+

        #DXB Consolidated Rates
        DXBConsolidatedRate_min = 185.00

        DXBConsolidatedRate1 = 3.42 #35- and 35+
        
        DXBConsolidatedRate2 = 2.51 #70+

        DXBConsolidatedRate3 = 2.04 #150+

        DXBConsolidatedRate4 = 1.91 #300+

        DXBConsolidatedRate5 = 1.81 #500+

        DXBConsolidatedRate6 = 1.76 #1000+

        #IST Critical Rates
        ISTCriticalRate_min = 91.11 #IST Only has One Rate For All THREE Charges

        ISTCriticalONLYRate = 1.10

        #IST Direct Rates
        ISTDirectRate_min = 81.52 #IST Only has One Rate For All THREE Charges

        ISTDirectONLYRate = 1.01

        #IST Consolidated Rates
        ISTConsolidatedRate_min = 71.93 #IST Only has One Rate For All THREE Charges

        ISTConsolidatedONLYRate = 0.91

        #AUH Critical Rates
        AUHCriticalRate_min = 385.00

        AUHCriticalRate1 = 6.87 #35- and 35+

        AUHCriticalRate2 = 5.16 #70+

        AUHCriticalRate3 = 3.71 #150+

        AUHCriticalRate4 = 3.11 #300+

        AUHCriticalRate5 = 3.01 #500+

        AUHCriticalRate6 = 2.91 #1000+

        #AUH Direct Rates
        AUHDirectRate_min = 287.70

        AUHDirectRate1 = 6.77 #35- and 35+

        AUHDirectRate2 = 5.06 #70+

        AUHDirectRate3 = 3.61 #150+

        AUHDirectRate4 = 3.01 #300+

        AUHDirectRate5 = 2.91 #500+

        AUHDirectRate6 = 2.81 #1000+

        #AUH Consolidated Rates
        AUHConsolidatedRate_min = 278.11

        AUHConsolidatedRate1 = 6.67 #35- and 35+

        AUHConsolidatedRate2 = 4.96 #70+

        AUHConsolidatedRate3 = 3.51 #150+

        AUHConsolidatedRate4 = 2.91 #300+

        AUHConsolidatedRate5 = 2.81 #500+

        AUHConsolidatedRate6 = 2.71 #1000+

        #TPE Critical Rates
        TPECriticalRate_min = 546.63

        TPECriticalRate1 = 11.51 #Under 35

        TPECriticalRate2 = 11.05 #Above 35

        TPECriticalRate3 = 9.46 #70 +

        TPECriticalRate4 = 8.55 #Above 150 and Above 300

        TPECriticalRate5 = 7.41 #500 +

        TPECriticalRate6 = 6.95 #1000 +

        #TPE Direct Rates
        TPEDirectRate_min = 81.52

        TPEDirectRate_ONLY = 1.31

        #TPE Consolidated Rates
        TPEConsolidatedRate_min = 71.93

        TPEConsolidatedRate_ONLY = 1.22

        #DOH Critical Rates
        DOHCriticalRate_min = 546.63

        DOHCriticalRate1 = 11.51 #Under 35

        DOHCriticalRate2 = 11.05 #Above 35

        DOHCriticalRate3 = 9.46 #70 +

        DOHCriticalRate4 = 8.55 #Above 150 and Above 300

        DOHCriticalRate5 = 7.41 #500 +

        DOHCriticalRate6 = 6.95 #1000 +

        #DOH Direct Rates
        DOHDirectRate_min = 287.70

        DOHDirectRate1 = 8.02 #35- and 35+

        DOHDirectRate2 = 5.59 #70 +

        DOHDirectRate3 = 3.84 #150+

        DOHDirectRate4 = 3.16 #300+

        DOHDirectRate5 = 2.94 #500+

        DOHDirectRate6 = 2.84 #1000+

        #DOH Consolidated Rates
        DOHConsolidatedRate_min = 287.11

        DOHConsolidatedRate1 = 7.92 #35- and 35+

        DOHConsolidatedRate2 = 5.49 #70 +

        DOHConsolidatedRate3 = 3.74 #150+

        DOHConsolidatedRate4 = 3.06 #300+

        DOHConsolidatedRate5 = 2.84 #500+

        DOHConsolidatedRate6 = 2.74 #1000+

        #TLV Critical Rates
        TLVCriticalRate_min = 546.63

        TLVCriticalRate1 = 11.51 #Under 35

        TLVCriticalRate1 = 11.05 #Above 35

        TLVCriticalRate1 = 9.46 #70 +

        TLVCriticalRate1 = 8.55 #Above 150 and Above 300

        TLVCriticalRate1 = 7.41 #500 +

        TLVCriticalRate1 = 6.95 #1000 +

        #TLV Direct Rates
        


        #DXB Critical If Logic

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * DXBCriticalRate1) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate1
                else:
                    self.airTotalValue = DXBCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * DXBCriticalRate1) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate1
                else:
                    self.airTotalValue = DXBCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * DXBCriticalRate2) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate2
                else:
                    self.airTotalValue = DXBCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * DXBCriticalRate3) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate3
                else:
                    self.airTotalValue = DXBCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * DXBCriticalRate4) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate4
                else:
                    self.airTotalValue = DXBCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * DXBCriticalRate5) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate5
                else:
                    self.airTotalValue = DXBCriticalRate_min
        
        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * DXBCriticalRate6) > DXBCriticalRate_min:
                    self.airTotalValue = self.weightValue * DXBCriticalRate6
                else:
                    self.airTotalValue = DXBCriticalRate_min
        

       #DXB Direct If Logic 

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * DXBDirectRate1) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate1
                else:
                    self.airTotalValue = DXBDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * DXBDirectRate1) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate1
                else:
                    self.airTotalValue = DXBDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * DXBDirectRate2) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate2
                else:
                    self.airTotalValue = DXBDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * DXBDirectRate3) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate3
                else:
                    self.airTotalValue = DXBDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * DXBDirectRate4) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate4
                else:
                    self.airTotalValue = DXBDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * DXBDirectRate5) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate5
                else:
                    self.airTotalValue = DXBDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * DXBDirectRate6) > DXBDirectRate_min:
                    self.airTotalValue = self.weightValue * DXBDirectRate6
                else:
                    self.airTotalValue = DXBDirectRate_min
        
        #DXB Consolidated If Logic

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * DXBConsolidatedRate1) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate1
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * DXBConsolidatedRate1) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate1
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * DXBConsolidatedRate2) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate2
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * DXBConsolidatedRate3) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate3
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * DXBConsolidatedRate4) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate4
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * DXBConsolidatedRate5) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate5
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DXB" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * DXBConsolidatedRate6) > DXBConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DXBConsolidatedRate6
                else:
                    self.airTotalValue = DXBConsolidatedRate_min

        #IST Critical If Logic
        
        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "IST" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 0.01:
                if (self.weightValue * ISTCriticalONLYRate) > ISTCriticalRate_min:
                    self.airTotalValue = self.weightValue * ISTCriticalONLYRate
                else:
                    self.airTotalValue = ISTCriticalRate_min

        #IST Direct If Logic
                    
        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "IST" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 0.01:
                if (self.weightValue * ISTDirectONLYRate) > ISTDirectRate_min:
                    self.airTotalValue = self.weightValue * ISTDirectONLYRate
                else:
                    self.airTotalValue = ISTDirectRate_min

        #IST Consolidated If Logic
                    
        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "IST" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 0.01:
                if (self.weightValue * ISTConsolidatedONLYRate) > ISTConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * ISTConsolidatedONLYRate
                else:
                    self.airTotalValue = ISTConsolidatedRate_min
        
        #AUH Critical If Logic
        
        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * AUHCriticalRate1) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate1
                else:
                    self.airTotalValue = AUHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * AUHCriticalRate1) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate1
                else:
                    self.airTotalValue = AUHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * AUHCriticalRate2) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate2
                else:
                    self.airTotalValue = AUHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * AUHCriticalRate3) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate3
                else:
                    self.airTotalValue = AUHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * AUHCriticalRate4) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate4
                else:
                    self.airTotalValue = AUHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * AUHCriticalRate5) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate5
                else:
                    self.airTotalValue = AUHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * AUHCriticalRate6) > AUHCriticalRate_min:
                    self.airTotalValue = self.weightValue * AUHCriticalRate6
                else:
                    self.airTotalValue = AUHCriticalRate_min
        
        #AUH Direct If Logic
                    
        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * AUHDirectRate1) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate1
                else:
                    self.airTotalValue = AUHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * AUHDirectRate1) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate1
                else:
                    self.airTotalValue = AUHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * AUHDirectRate2) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate2
                else:
                    self.airTotalValue = AUHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * AUHDirectRate3) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate3
                else:
                    self.airTotalValue = AUHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * AUHDirectRate4) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate4
                else:
                    self.airTotalValue = AUHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * AUHDirectRate5) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate5
                else:
                    self.airTotalValue = AUHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * AUHDirectRate6) > AUHDirectRate_min:
                    self.airTotalValue = self.weightValue * AUHDirectRate6
                else:
                    self.airTotalValue = AUHDirectRate_min
        
        #AUH Consolidated If Logic
                    
        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * AUHConsolidatedRate1) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate1
                else:
                    self.airTotalValue = AUHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * AUHConsolidatedRate1) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate1
                else:
                    self.airTotalValue = AUHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * AUHConsolidatedRate2) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate2
                else:
                    self.airTotalValue = AUHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * AUHConsolidatedRate3) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate3
                else:
                    self.airTotalValue = AUHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * AUHConsolidatedRate4) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate4
                else:
                    self.airTotalValue = AUHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * AUHConsolidatedRate5) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate5
                else:
                    self.airTotalValue = AUHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "AUH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * AUHConsolidatedRate6) > AUHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * AUHConsolidatedRate6
                else:
                    self.airTotalValue = AUHConsolidatedRate_min
        
        #TPE Critical If Logic
        
        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue < 35:
                if (self.weightValue * TPECriticalRate1) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate1
                else:
                    self.airTotalValue = TPECriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue > 35 and self.weightValue < 70:
                if (self.weightValue * TPECriticalRate2) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate2
                else:
                    self.airTotalValue = TPECriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * TPECriticalRate3) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate3
                else:
                    self.airTotalValue = TPECriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * TPECriticalRate4) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate4
                else:
                    self.airTotalValue = TPECriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * TPECriticalRate4) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate4
                else:
                    self.airTotalValue = TPECriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue > 500 and self.weightValue < 1000:
                if (self.weightValue * TPECriticalRate5) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate5
                else:
                    self.airTotalValue = TPECriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * TPECriticalRate6) > TPECriticalRate_min:
                    self.airTotalValue = self.weightValue * TPECriticalRate6
                else:
                    self.airTotalValue = TPECriticalRate_min

        #TPE Direct If Logic
        
        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 0.01:
                if (self.weightValue * TPEDirectRate_ONLY) > TPEDirectRate_min:
                    self.airTotalValue = self.weightValue * TPEDirectRate_ONLY
                else:
                    self.airTotalValue = TPEDirectRate_min

        #TPE Consolidated If Logic
        
        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "TPE" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 0.01:
                if (self.weightValue * TPEConsolidatedRate_ONLY) > TPEConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * TPEConsolidatedRate_ONLY
                else:
                    self.airTotalValue = TPEConsolidatedRate_min

        #DOH Critical If Logic
        
        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * DOHCriticalRate1) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate1
                else:
                    self.airTotalValue = DOHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * DOHCriticalRate1) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate1
                else:
                    self.airTotalValue = DOHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * DOHCriticalRate2) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate2
                else:
                    self.airTotalValue = DOHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * DOHCriticalRate3) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate3
                else:
                    self.airTotalValue = DOHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * DOHCriticalRate4) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate4
                else:
                    self.airTotalValue = DOHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * DOHCriticalRate5) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate5
                else:
                    self.airTotalValue = DOHCriticalRate_min

        if self.UrgeLev == "Critical" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * DOHCriticalRate6) > DOHCriticalRate_min:
                    self.airTotalValue = self.weightValue * DOHCriticalRate6
                else:
                    self.airTotalValue = DOHCriticalRate_min

        #DOH Direct If Logic
                    
        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * DOHDirectRate1) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate1
                else:
                    self.airTotalValue = DOHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * DOHDirectRate1) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate1
                else:
                    self.airTotalValue = DOHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * DOHDirectRate2) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate2
                else:
                    self.airTotalValue = DOHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * DOHDirectRate3) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate3
                else:
                    self.airTotalValue = DOHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * DOHDirectRate4) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate4
                else:
                    self.airTotalValue = DOHDirectRate_min
                
        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * DOHDirectRate5) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate5
                else:
                    self.airTotalValue = DOHDirectRate_min

        if self.UrgeLev == "Direct" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * DOHDirectRate6) > DOHDirectRate_min:
                    self.airTotalValue = self.weightValue * DOHDirectRate6
                else:
                    self.airTotalValue = DOHDirectRate_min

        #DOH Consolidated If Logic
                    
        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue <= 35:
                if (self.weightValue * DOHConsolidatedRate1) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate1
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 35 and self.weightValue < 70:
                if (self.weightValue * DOHConsolidatedRate1) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate1
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 70 and self.weightValue < 150:
                if (self.weightValue * DOHConsolidatedRate2) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate2
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 150 and self.weightValue < 300:
                if (self.weightValue * DOHConsolidatedRate3) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate3
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 300 and self.weightValue < 500:
                if (self.weightValue * DOHConsolidatedRate4) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate4
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 500 and self.weightValue < 1000:
                if (self.weightValue * DOHConsolidatedRate5) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate5
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        if self.UrgeLev == "Consolidated" and self.LaneTravelingIn == "DOH" and self.LaneTravelingFrom == "SEA":
            if self.weightValue >= 1000:
                if (self.weightValue * DOHConsolidatedRate6) > DOHConsolidatedRate_min:
                    self.airTotalValue = self.weightValue * DOHConsolidatedRate6
                else:
                    self.airTotalValue = DOHConsolidatedRate_min

        self.air_value_label.config(text=f"Air Value: {self.airTotalValue:.2f}")



if __name__ =="__main__":

    start_app = beginApp()
    start_app.openWindow()
    start_app.gatherEntryApps()
    start_app.gatherEntryApps()