from roipage import app
from flask import render_template, request, url_for
from roipage.forms import ROIForm


#I may need to import redirect on line 2 and
#prfloat the sum on a different page
@app.route("/", methods=["GET", "POST"])
def roi():
    roiForm = ROIForm()
    expenses = 0
    invest = 0
    income = 0
    roi = 0
    if request.method == "POST":
        rent = float(roiForm.rent.data)
        other = float(roiForm.other.data)
        mortgage = float(roiForm.mortgage.data)
        tax = float(roiForm.tax.data)
        insur = float(roiForm.insur.data)
        util = float(roiForm.util.data)
        hoa = float(roiForm.hoa.data)
        lawnsnow = float(roiForm.lawnsnow.data)
        vacancy = float(roiForm.vacancy.data)
        repairs = float(roiForm.repairs.data)
        capex = float(roiForm.capex.data)
        management = float(roiForm.management.data)
        down = float(roiForm.down.data)
        closing = float(roiForm.closing.data)
        maint = float(roiForm.maint.data)
        misc = float(roiForm.misc.data)
        income = sum([rent, other])
        expenses = sum([mortgage, tax, insur, util, hoa, lawnsnow, vacancy, repairs, capex, management])
        invest = sum([down, closing, maint, misc])
        roi = round((income - expenses) * 12 / invest * 100, 2)
    return render_template("roi.html", roiform = roiForm, expenses = expenses, invest = invest, income = income, roi = roi)

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")