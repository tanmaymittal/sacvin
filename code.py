import pandas as pd

class MainClass:

    def data_range(**kwargs):
        n = {"name":["Start Date","End Date"],"value":["Jan-2018","Sep-2020"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient = "records")
    def sheet(**kwargs):
        n = {"name":[""],"value":["Please upload your daily production sheet here"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient = "records")

    def lastdaysum(**kwargs):
        n = {"name":["Total Units Produced","Machines Active","Machines Inactive","Total Downtime (hh:mm:ss)"],"value":["6500","23","7","04:20:02"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient = "records")

    def lastmonthrevenue(**kwargs):
        n = {"name":["Last Month's Revenue in NGN"],"value":["1,803,567,450"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient = "records")


    def card_unit_ytd(**kwargs):

        return [{'sum':"10,000,000"}]

    def unit_productivity(**kwargs):

        return [{'sum':"92.40 %"}]

    def active_machine(**kwargs):
        return [{'sum':"34"}]

    def downtime_hour(**kwargs):
        df = pd.DataFrame()
        df['Month'] = ['January','February','March','April','May','June','July','August']
        df['Downtime Hours'] = [45,55,48,75,60,20,32,56]
        return df.to_dict(orient='records')

    def p_m(**kwargs):

        df = pd.DataFrame()
        df['Month'] = ['Jan-20', 'Feb-20', 'Mar-20', 'Apr-20', 'May-20', 'Jun-20', 'Jul-20', 'Aug-20']
        df['Actual Maintenance Cost'] = [241536, 146594, 203685, 230917, 135383, 184334, 279276, 235283]
        df['Predicted Maintenance Cost'] = [254098, 140323, 230034, 223234, 150234, 180342, 223453, 232325]
        return df.to_dict(orient='records')

    def unit_made(**kwargs):

        df = pd.DataFrame()
        df['Machine'] = ['Machine 1', 'Machine 2', 'Machine 3', 'Machine 4', 'Machine 5']
        df['Units Made'] = [4500, 6000, 5500, 4200, 5900]
        return df.to_dict(orient='records')

    def r_m(**kwargs):

        df = pd.DataFrame()
        df['Machine'] = ['Machine 1', 'Machine 2', 'Machine 3', 'Machine 4', 'Machine 5']
        df['Copper'] = [256, 325, 285, 265, 315]
        df['Aluminium'] = [512, 650, 570, 530, 630]
        df['Plastic'] = [384, 488, 428, 398, 473]
        return df.to_dict(orient= 'records')

    def target(**kwargs):

        n = {"name":["Item name","Target units", "Deadline"], "value":["Basins Big","26,100", "Oct-2020"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient="records")

    def info(**kwargs):
        n = {"name":["Predicted Unit Loss", "Predicted Aluminum Lost", "Predicted Copper Lost", "Predicted Plastic Lost", "Predicted Downtime"], "value":["4,231 Units", "5 kgs", "2.5 kgs", "4.5 kgs", "154 Hours"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient="records")

    def stock(**kwargs):
        n = {"name": ["Current Stock", "Warehouse Stock"], "value": ["3,678", "5,659"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient="records")

    def fyp(**kwargs):
        val = 91
        return [{'gauge': val}]

    def machine_used(**kwargs):

        n = {"name": ["Machine 1", "Machine 2", "Machine 3", "Machine 4", "Machine 5"], "value": ["124 hours", "156 hours", "145 hours", "123 hours", "156 hours"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient='records')

    def pmc(**kwargs):
        n = {"name": ["Predicted Cost"], "value": ["231,546"]}
        df=pd.DataFrame(n)
        return df.to_dict(orient='records')
