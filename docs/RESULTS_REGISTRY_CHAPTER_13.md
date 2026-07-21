# سجل نتائج الفصل الثالث عشر — مؤقت

```text
CHAPTER       = 13
CHAPTER-STATE = DRAFT
REGISTRY      = TEMPORARY / NON-CITABLE
RESULTS       = 11
```

هذا الملف جزء من نمط `RESULTS_REGISTRY*.md` الذي تفحصه الجودة، ويثبت أن كل
معرّف ظاهر في متن الفصل محجوز ومسجل. لا يجعل النتائج قابلة للاستشهاد قبل
تدقيق ما بعد التأليف ونقلها إلى السجل المركزي.

| المعرّف | النتيجة | الملف | الحالة | المصدر أو البرهان |
|---|---|---|---|---|
| `ANT-THM-13-01` | حزمة الغربال الكبير للشخصيات: التربيعية والثنائية العظمى | الفصل 13 | `DRAFT / CITED / COMPOSITE-INPUT / NON-CITABLE` | Bombieri (1965)؛ Montgomery--Vaughan II (2026)، المبرهنتان 19.16 و19.19 |
| `ANT-LEM-13-01` | هوية Vaughan | الفصل 13 | `DRAFT / PROVED-HERE / NON-CITABLE` | برهان التفاف ديريشليه؛ تدقيق الهوية PASS |
| `ANT-PROP-13-01` | تفكيك مجاميع فون مانغولت إلى Type I وType II | الفصل 13 | `DRAFT / PROVED-HERE / NON-CITABLE` | نتيجة من هوية Vaughan؛ تدقيق الدعم PASS |
| `ANT-LEM-13-02` | تقدير Type I | الفصل 13 | `DRAFT / PROVED-HERE / NON-CITABLE` | Pólya--Vinogradov والجمع الجزئي؛ تدقيق Type I PASS |
| `ANT-LEM-13-03` | تقدير Type II | الفصل 13 | `DRAFT / PROVED-HERE / NON-CITABLE` | المدخل الثنائي العظمى والتقسيم الديادي؛ تدقيق Type II PASS |
| `ANT-LEM-13-04` | متراجحة Pólya--Vinogradov للشخصيات البدائية | الفصل 13 | `DRAFT / PROVED-HERE / NON-CITABLE` | تحويل فورييه المنتهي ومجاميع غاوس من الفصل 7 |
| `ANT-THM-13-02` | مبرهنة القيمة المتوسطة للشخصيات البدائية مع `sup_{y<=x}` | الفصل 13 | `DRAFT / PROVED-HERE / NON-CITABLE` | هوية Vaughan وType I/II وحزمة الغربال الكبير المقتبسة |
| `ANT-THM-13-03` | مبرهنة Bombieri--Vinogradov في صيغة `psi` | الفصل 13 | `DRAFT / PROVED-HERE / INEFFECTIVE-CONSTANT / NON-CITABLE` | القيمة المتوسطة ورد الموصلات وSiegel--Walfisz للصغار |
| `ANT-COR-13-01` | النسخة الموافقة لـ`theta` | الفصل 13 | `DRAFT / PROVED-HERE / INEFFECTIVE-CONSTANT / NON-CITABLE` | ضبط القوى الأولية العليا من الفصل 9 |
| `ANT-COR-13-02` | النسخة الموافقة لـ`pi` | الفصل 13 | `DRAFT / PROVED-HERE / INEFFECTIVE-CONSTANT / NON-CITABLE` | الجمع الجزئي من `ANT-COR-13-01` |
| `ANT-COR-13-03` | نتيجة تقريبًا كل الترديدات | الفصل 13 | `DRAFT / PROVED-HERE / INEFFECTIVE-CONSTANT / NON-CITABLE` | متراجحة ماركوف من `ANT-THM-13-03` |

## شرط الإغلاق

بعد اجتياز تدقيق ما بعد التأليف والتحقق المرجعي والبناء، تنقل الصفوف إلى
`docs/RESULTS_REGISTRY.md` ويحذف هذا الملف المؤقت.
