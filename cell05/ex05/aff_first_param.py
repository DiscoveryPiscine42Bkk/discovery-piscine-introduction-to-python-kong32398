import sys

# ตรวจสอบว่ามีพารามิเตอร์หรือไม่
if len(sys.argv) > 1:
    # มีพารามิเตอร์ - แสดงพารามิเตอร์แรก
    print(sys.argv[1])
else:
    # ไม่มีพารามิเตอร์ - แสดง "none"
    print("none")