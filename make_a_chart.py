import xlsxwriter

workbook = xlsxwriter.workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
# define a serie of data
SeriesData01 = []
for i in range(0,10,1)
    SeriesData01.append(random.radient(1,20))
worksheet.write_column("A1", SeriesData01)
# create a new chart object
chart = workbook.add_chart({"type" : "line"})
# add a serie of data to the chart
chart.add_series({"values" : "=Sheet1!$A$1:$A$2",
                  "line" : {"color" : ""}
                  "name" : "Type Name"})
# Save Exce File
worksheet.insert_chart("C1", chart)
workbook.close()
