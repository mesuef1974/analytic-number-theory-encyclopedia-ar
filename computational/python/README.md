# تجارب بايثون القابلة لإعادة الإنتاج

يحتوي هذا المسار على تجارب عددية مساندة للموسوعة. لا تحل هذه التجارب محل البرهان الرياضي، ويجب تفسير كل مخرج داخل سقف الادعاء المسجل له.

## ANT-COMP-06-01: تحقق منخفض الارتفاع لدالة Hardy Z

الغرض هو التحقق من تنفيذ دالة
`Z(t)=exp(i theta(t)) zeta(1/2+it)`
وعزل عشرة أصفار منخفضة الارتفاع بواسطة تغيّر الإشارة. التجربة:

- لا تثبت اكتمال الأصفار في المجال الممسوح؛
- لا تكشف بالضرورة صفرًا ذا رتبة زوجية أو صفرين متقاربين داخل خطوة واحدة؛
- لا تبحث عن أصفار خارج الخط الحرج؛
- ليست دليلاً على فرضية ريمان؛
- ليست اختبارًا لإحصاءات GUE.

شغّل الأوامر من جذر المستودع.

### المتطلبات

- Python 3.12
- SciPy 1.17.0، مثبتة من الملف
  `computational/python/requirements-zeta.txt`

بيئة المخرجات المرجعية: Python 3.12.13 وSciPy 1.17.0.

### التشغيل على POSIX

```bash
python3 -m venv .venv-zeta
. .venv-zeta/bin/activate
python -m pip install -r computational/python/requirements-zeta.txt
python computational/python/hardy_z_low_zeros.py --config computational/python/config/hardy_z_first10.json
```

### التشغيل على Windows PowerShell

```powershell
py -3.12 -m venv .venv-zeta
.\.venv-zeta\Scripts\Activate.ps1
python -m pip install -r computational/python/requirements-zeta.txt
python computational/python/hardy_z_low_zeros.py --config computational/python/config/hardy_z_first10.json
```

### المدخلات والمخرجات

- التسجيل المسبق:
  `computational/python/config/hardy_z_first10.json`
- جدول الجذور:
  `computational/python/outputs/hardy_z_first10.csv`
- ملخص التحقق:
  `computational/python/outputs/hardy_z_first10.summary.json`

بصمة SHA-256 للتسجيل المسبق المرجعي:

```text
ed8f1b570afaafd72c744c26289c8156853fe12e8e680398357b223df0d20bf7
```

يعيد البرنامج كتابة ملفي المخرجات ويخرج برمز غير صفري إذا فشل أحد شروط القبول المسجلة: العدد المتوقع، صغر البواقي، الترتيب الصارم، أو اختلاف الإشارة على طرفي كل قوس. أما المرور فلا يرفع سقف الادعاء عن `NO_RH_EVIDENCE`.
