from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Python Course - Day 05 (Lists)", ln=True, align='C')
pdf.ln(10)

content = '''
Python میں list ایک ایسا ڈیٹا ٹائپ ہے جس میں ہم کئی آئٹمز ایک ساتھ رکھ سکتے ہیں۔

🔹 List کیسے بنائی جاتی ہے؟
fruits = ["apple", "banana", "mango"]

🔹 List میں item شامل کرنا:
fruits.append("orange")

🔹 List سے item نکالنا:
fruits.remove("banana")

🔹 List میں تبدیلی کرنا:
fruits[1] = "grapes"

🧠 مشق:
1. پاکستانی شہروں کی فہرست بنائیں۔
2. ایک نیا شہر شامل کریں۔
3. ایک شہر کو تبدیل کریں۔
4. ایک شہر delete کریں۔
'''

for line in content.strip().split('\n'):
    pdf.multi_cell(0, 10, txt=line)

pdf.output("Python_Day05_Lists.pdf")
