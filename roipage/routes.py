from roipage import app
from flask import render_template, request, url_for
from roipage.forms import ROIForm


#I may need to import redirect on line 2 and
#print the sum on a different page
@app.route("/", methods=["GET", "POST"])
def roi():
    roiForm = ROIForm()
    expenses = 0
    invest = 0
    income = 0
    if request.method == "POST":
        rent = int(roiForm.rent.data)
        other = int(roiForm.other.data)
        mortgage = int(roiForm.mortgage.data)
        tax = int(roiForm.tax.data)
        insur = int(roiForm.insur.data)
        util = int(roiForm.util.data)
        hoa = int(roiForm.hoa.data)
        lawnsnow = int(roiForm.lawnsnow.data)
        vacancy = int(roiForm.vacancy.data)
        repairs = int(roiForm.repairs.data)
        capex = int(roiForm.capex.data)
        management = int(roiForm.management.data)
        down = int(roiForm.down.data)
        closing = int(roiForm.closing.data)
        maint = int(roiForm.maint.data)
        misc = int(roiForm.misc.data)
        income = sum([rent, other])
        expenses = sum([mortgage, tax, insur, util, hoa, lawnsnow, vacancy, repairs, capex, management])
        invest = sum([down, closing, maint, misc])
        print(f"Your monthly cashflow is ${income - expenses}.")
        print(f"Your annual cash on cash ROI is {(income - expenses) * 12 / invest * 100}%.")
    return render_template("roi.html", roiform = roiForm, expenses = expenses, invest = invest, income = income)
