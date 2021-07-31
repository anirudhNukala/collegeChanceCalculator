from django.http.response import HttpResponse
from django.shortcuts import render
from .models import College, AdmissionStats, Scores, Student
# Create your views here.
def list(request):
    colleges = College.objects.all()
    students = Student.objects.all()
    return render(request, "college.html", {"colleges":colleges, "students":students})

def chance(request):
    return render(request, "chance.html")

def studentlist(request):
    students = Student.objects.all()
    return render(request, "studentlist.html", {"students":students})

def stats(request):
    id = int(request.GET['id'])
    college = College.objects.get(pk=id)
    stats = college.AdmissionStats
    scores = college.scores
    return render(request, "stats.html", {"stats":stats, "scores":scores})

def studentstats(request):
    id = int(request.GET['id'])
    student = Student.objects.get(pk=id)
    return render(request, "studentdetail.html", {"student":student})

def create(request):
    print('dosa')
    return render(request, "create.html")

def statstudent(request, id):
    student = Student.objects.get(pk=id)
    colleges = College.objects.all()
    print(colleges)
    colors = []
    for college in colleges:
        stats = college.AdmissionStats
        scores = college.scores
        act_composite50 = (scores.act_compostite25 + scores.act_composite75) / 2
        act_english50 = (scores.act_english25 + scores.act_english75) / 2
        act_math50 = (scores.act_math25 + scores.act_math75) / 2
        if stats.male_selectivity < 15 or stats.male_yield > 60:
            colors.append('dreamcollege')
        elif student.act_composite > act_composite50 and student.act_english > act_english50 and student.act_math > act_math50 and stats.male_selectivity >= 15 and stats.male_selectivity <= 25:
            colors.append('corecollege')
        elif student.act_composite > act_composite50 and student.act_english > act_english50 and student.act_math > act_math50:
            colors.append('safecollege')
    print(colors)
    zippedlist = zip(colleges,colors)
    return render(request, "college_colors.html", {"colors":colors, "colleges":colleges, "zippedlist":zippedlist})

def studentchance(request):
    colleges = College.objects.all()
    colors = []
    if request.POST['sat_or_act'] == 'ACT':
        act_composite = int(request.POST['act_composite'])
        act_math = int(request.POST['act_math'])
        act_english = int(request.POST['act_english'])
        for college in colleges:
            stats = college.AdmissionStats
            scores = college.scores
            act_composite50 = (scores.act_compostite25 + scores.act_composite75) / 2
            act_english50 = (scores.act_english25 + scores.act_english75) / 2
            act_math50 = (scores.act_math25 + scores.act_math75) / 2
            if stats.male_selectivity < 15 or stats.male_yield > 60:
                colors.append('dreamcollege')
            elif act_composite > act_composite50 and act_english > act_english50 and act_math > act_math50 and stats.male_selectivity >= 15 and stats.male_selectivity <= 25:
                colors.append('corecollege')
            elif act_composite > act_composite50 and act_english > act_english50 and act_math > act_math50:
                colors.append('safecollege')
            else:
                colors.append('dreamcollege')
        zippedlist = zip(colleges,colors)
    else:
        sat_math = int(request.POST['sat_math'])
        sat_english = int(request.POST['sat_english'])
        sat_composite = sat_math + sat_english
        for college in colleges:
            stats = college.AdmissionStats
            scores = college.scores
            sat_composite50 = (scores.sat_compostite25 + scores.sat_composite75) / 2
            sat_english50 = (scores.sat_english25 + scores.sat_english75) / 2
            sat_math50 = (scores.sat_math25 + scores.sat_math75) / 2
            if stats.male_selectivity < 15 or stats.male_yield > 60:
                colors.append('dreamcollege')
            elif sat_composite > sat_composite50 and sat_english > sat_english50 and sat_math > sat_math50 and stats.male_selectivity >= 15 and stats.male_selectivity <= 25:
                colors.append('corecollege')
            elif sat_composite > sat_composite50 and sat_english > sat_english50 and sat_math > sat_math50:
                colors.append('safecollege')
            else:
                colors.append('dreamcollege')
        zippedlist = zip(colleges,colors)
    return render(request, "studentcolor.html", {"colors":colors, "colleges":colleges, "zippedlist":zippedlist})

def student(request):
    print('student')
    return render(request, "student.html")

def collegecolor(request):
    id = int(request.POST['studentlist'])
    print(id)
    return statstudent(request, id)
    #return render(request, "college.html")


def delete(request):
    colleges = College.objects.all()
    print(colleges)
    return render(request, "delete.html", {"colleges":colleges})

def studentdelete(request):
    students = Student.objects.all()
    return render(request, "studentdelete.html", {"students":students})

def submitdelete(request):
    if request.method == "POST":
        s = request.POST.getlist("college[]")
        for s1 in s:
            college = College.objects.get(pk=s1)
            college.delete()
        colleges = College.objects.all()
        return render(request,"college.html",{'colleges':colleges})

def studentsubmitdelete(request):
    if request.method == "POST":
        s = request.POST.getlist("student[]")
        for s1 in s:
            student = Student.objects.get(pk=s1)
            student.delete()
        students = Student.objects.all()
        return render(request,"studentlist.html",{'students':students})


def submitstudent(request):
    name = request.POST['name']
    act_composite = request.POST['act_composite']
    act_english = request.POST['act_english']
    act_math = request.POST['act_math']
    sat_composite = request.POST['sat_composite']
    sat_english = request.POST['sat_english']
    sat_math = request.POST['sat_math']
    student = Student()
    student.name = name
    student.act_composite = act_composite
    student.act_english = act_english
    student.act_math = act_math
    student.sat_composite = sat_composite
    student.sat_english = sat_english
    student.sat_math = sat_math
    student.save()
    students = Student.objects.all()
    return render(request,"studentlist.html",{'students':students})

def checkstatus(request):
    students = Student.objects.all()
    return render(request, "checkstatus.html", {"students":students})

def submit(request):
     name = request.POST['name']
     ipeds = request.POST['ipeds']
     act_compostite25 = request.POST['act_compostite25']
     act_composite75 = request.POST['act_composite75']
     act_math25 = request.POST['act_math25']
     act_math75 = request.POST['act_math75']
     act_english25 = request.POST['act_english25']
     act_english75 = request.POST['act_english75']
     sat_compostite25 = request.POST['sat_compostite25']
     sat_composite75 = request.POST['sat_composite75']
     sat_math25 = request.POST['sat_math25']
     sat_math75 = request.POST['sat_math75']
     sat_english25 = request.POST['sat_english25']
     sat_english75 = request.POST['sat_english75']
     male_yield = request.POST['male_yield']
     male_selectivity = request.POST['male_selectivity']
     female_yield = request.POST['female_yield']
     female_selectivity = request.POST['female_selectivity']
     scores = Scores()
     scores.act_compostite25 = act_compostite25
     scores.act_composite75 = act_composite75
     scores.act_english25 = act_english25
     scores.act_english75 = act_english75
     scores.act_math25 = act_math25
     scores.act_math75 = act_math75
     scores.sat_compostite25 = sat_compostite25
     scores.sat_composite75 = sat_composite75
     scores.sat_english25 = sat_english25
     scores.sat_english75 = sat_english75
     scores.sat_math25 = sat_math25
     scores.sat_math75 = sat_math75
     admissionstats = AdmissionStats()
     admissionstats.male_selectivity = male_selectivity
     admissionstats.male_yield = male_yield
     admissionstats.female_selectivity = female_selectivity
     admissionstats.female_yield = female_yield
     college = College()
     college.AdmissionStats = admissionstats
     college.scores = scores
     college.name = name
     college.ipeds = ipeds
     admissionstats.save()
     scores.save()
     college.save()
     return list(request)
     

