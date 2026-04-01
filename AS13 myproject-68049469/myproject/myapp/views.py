from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db.models import Q  # เพิ่ม import Q เข้ามาสำหรับการค้นหาหลายฟิลด์
from myapp.models import Person

# --- ปรับปรุงฟังก์ชัน index ใหม่สำหรับ Lab 13 ---
def index(request):
    # 1. ดึงข้อมูลประชากรทั้งหมดมาก่อน (กรณีที่ยังไม่ได้ค้นหา)
    all_person = Person.objects.all()

    # 2. รับค่าคำค้นหาจากช่องค้นหา (name="q")
    query = request.GET.get('q')

    # 3. ตรวจสอบว่ามีค่าค้นหาถูกพิมพ์ส่งมาหรือไม่
    if query:
        # ถ้ามีคำค้นหา ให้นำ all_person มากรองข้อมูลเฉพาะคนที่ชื่อหรืออายุตรงกับคำค้นหา
        all_person = all_person.filter(Q(name__icontains=query) | Q(age__icontains=query))

    # 4. ส่งข้อมูลไปแสดงผลที่ template (ถ้าไม่มี query ก็จะแสดงทั้งหมดตามข้อ 1)
    return render(request, 'index.html', {"all_person": all_person})

# --- ของเดิมที่มีอยู่แล้ว ---
def about(request):
    return render(request, 'about.html')

def form(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = int(request.POST.get("age"))
        Person.objects.create(name=name, age=age)
        return redirect("/")
    else:
        return render(request, 'form.html')

# ฟังก์ชันลบข้อมูล
def delete(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/")

# ฟังก์ชันแสดงหน้าแก้ไข (ดึงข้อมูลเก่าไปแสดงที่ฟอร์ม)
def edit(request, id):
    person = Person.objects.get(id=id)
    return render(request, 'edit.html', {"person": person})

# ฟังก์ชันรับค่าที่แก้ไขแล้วไปบันทึกในฐานข้อมูล
def update(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        
        person = Person.objects.get(id=id)
        person.name = name
        person.age = age
        person.save() # สั่งบันทึกข้อมูลที่แก้ไขแล้ว
        return redirect("/")