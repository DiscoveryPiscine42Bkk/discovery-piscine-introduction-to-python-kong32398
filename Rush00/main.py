 # โปรแกรมการจัดการฟาร์มงานนักศึกษา
# Student Task Farm Management System

def show_menu():
    """แสดงเมนูหลักของโปรแกรม"""
    print("\n" + "="*50)
    print("🌾 โปรแกรมการจัดการฟาร์มงานนักศึกษา 🌾")
    print("="*50)
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")
    print("="*50)

def add_task(task_list):
    """เพิ่มงานใหม่ในฟาร์ม"""
    print("\n--- เพิ่มงานในฟาร์ม ---")
    
    # รับข้อมูลงานจากผู้ใช้
    task_name = input("ชื่องาน: ").strip()
    if not task_name:
        print("❌ กรุณาใส่ชื่องาน!")
        return
    
    print("\nประเภทงาน:")
    print("1. การปลูก")
    print("2. การดูแล")
    print("3. การเก็บเกี่ยว")
    print("4. การขาย")
    print("5. อื่นๆ")
    
    try:
        category_choice = int(input("เลือกประเภทงาน (1-5): "))
        categories = {
            1: "การปลูก",
            2: "การดูแล", 
            3: "การเก็บเกี่ยว",
            4: "การขาย",
            5: "อื่นๆ"
        }
        
        if category_choice not in categories:
            print("❌ กรุณาเลือกประเภทงานที่ถูกต้อง!")
            return
            
        category = categories[category_choice]
        
    except ValueError:
        print("❌ กรุณาใส่ตัวเลข!")
        return
    
    priority = input("ระดับความสำคัญ (สูง/กลาง/ต่ำ): ").strip()
    if priority.lower() not in ['สูง', 'กลาง', 'ต่ำ']:
        priority = "กลาง"  # ค่าเริ่มต้น
    
    # สร้างงานใหม่
    task = {
        'id': len(task_list) + 1,
        'name': task_name,
        'category': category,
        'priority': priority,
        'status': 'รอดำเนินการ'
    }
    
    task_list.append(task)
    print(f"✅ เพิ่มงาน '{task_name}' เรียบร้อยแล้ว!")

def show_all_tasks(task_list):
    """แสดงรายการงานทั้งหมด"""
    print("\n--- รายการงานทั้งหมด ---")
    
    if not task_list:
        print("📋 ยังไม่มีงานในฟาร์ม")
        return
    
    print(f"{'ID':<3} {'ชื่องาน':<20} {'ประเภท':<15} {'ความสำคัญ':<10} {'สถานะ'}")
    print("-" * 70)
    
    for task in task_list:
        print(f"{task['id']:<3} {task['name']:<20} {task['category']:<15} {task['priority']:<10} {task['status']}")

def delete_task(task_list):
    """ลบงานออกจากฟาร์ม"""
    print("\n--- ลบงาน ---")
    
    if not task_list:
        print("📋 ยังไม่มีงานในฟาร์ม")
        return
    
    # แสดงรายการงานปัจจุบัน
    show_all_tasks(task_list)
    
    try:
        task_id = int(input("\nใส่ ID งานที่ต้องการลบ: "))
        
        # หางานที่ต้องการลบ
        task_to_delete = None
        for task in task_list:
            if task['id'] == task_id:
                task_to_delete = task
                break
        
        if task_to_delete:
            task_name = task_to_delete['name']
            task_list.remove(task_to_delete)
            
            # อัพเดท ID ใหม่
            for i, task in enumerate(task_list):
                task['id'] = i + 1
                
            print(f"✅ ลบงาน '{task_name}' เรียบร้อยแล้ว!")
        else:
            print("❌ ไม่พบงานที่มี ID นี้!")
            
    except ValueError:
        print("❌ กรุณาใส่ตัวเลข!")

def show_summary(task_list):
    """สรุปงานในแต่ละประเภท"""
    print("\n--- สรุปงานในแต่ละประเภท ---")
    
    if not task_list:
        print("📋 ยังไม่มีงานในฟาร์ม")
        return
    
    # นับจำนวนงานในแต่ละประเภท
    category_count = {}
    priority_count = {'สูง': 0, 'กลาง': 0, 'ต่ำ': 0}
    
    for task in task_list:
        # นับตามประเภท
        category = task['category']
        if category in category_count:
            category_count[category] += 1
        else:
            category_count[category] = 1
        
        # นับตามความสำคัญ
        priority = task['priority']
        if priority in priority_count:
            priority_count[priority] += 1
    
    print(f"📊 จำนวนงานทั้งหมด: {len(task_list)} งาน\n")
    
    print("🏷️  สรุปตามประเภทงาน:")
    print("-" * 30)
    for category, count in category_count.items():
        print(f"   {category}: {count} งาน")
    
    print("\n⭐ สรุปตามความสำคัญ:")
    print("-" * 30)
    for priority, count in priority_count.items():
        if count > 0:
            print(f"   {priority}: {count} งาน")

def main():
    """ฟังก์ชันหลักของโปรแกรม"""
    task_list = []
    
    print("🌟 ยินดีต้อนรับสู่โปรแกรมการจัดการฟาร์มงานนักศึกษา! 🌟")
    
    while True:
        show_menu()
        
        try:
            choice = input("\nเลือกเมนู (1-5): ").strip()
            
            if choice == '1':
                add_task(task_list)
            elif choice == '2':
                show_all_tasks(task_list)
            elif choice == '3':
                delete_task(task_list)
            elif choice == '4':
                show_summary(task_list)
            elif choice == '5':
                print("\n🌾 ขอบคุณที่ใช้โปรแกรม! 🌾")
                print("👋 ลาก่อน!")
                break
            else:
                print("❌ กรุณาเลือกเมนู 1-5 เท่านั้น!")
                
        except KeyboardInterrupt:
            print("\n\n🌾 ขอบคุณที่ใช้โปรแกรม! 🌾")
            print("👋 ลาก่อน!")
            break
        
        # หยุดรอให้ผู้ใช้กดปุ่มเพื่อดำเนินการต่อ
        input("\nกด Enter เพื่อดำเนินการต่อ...")

# เรียกใช้โปรแกรม
if __name__ == "__main__":
    main()