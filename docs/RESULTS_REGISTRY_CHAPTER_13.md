# سجل نتائج الفصل الثالث عشر

```text
CHAPTER       = 13
CHAPTER-STATE = REVIEWED
REGISTRY      = ACTIVE / CHAPTER-SCOPED
RESULTS       = 11
REVIEWED      = YES
RELEASE-READY = NO
```

هذا الملف جزء من سجل النتائج المعتمد الذي تفحصه الجودة. تظهر النتائج هنا
بحالات منشئها الصحيحة بعد اجتياز التدقيق المنطقي والمرجعي وتدقيق ما بعد
التأليف وفحوص الجودة والبناء. بقاء الملف مستقلًا عن الجدول الطويل في
`docs/RESULTS_REGISTRY.md` تنظيمي فقط، ولا يغيّر درجة الاعتماد.

| المعرّف | النتيجة | الملف | الحالة | المصدر أو البرهان |
|---|---|---|---|---|
| `ANT-THM-13-01` | حزمة الغربال الكبير للشخصيات: التربيعية والثنائية العظمى | الفصل 13 | `CITED / COMPOSITE-INPUT` | Bombieri (1965)؛ Montgomery--Vaughan II (2026)، المبرهنتان 19.16 و19.19 |
| `ANT-LEM-13-01` | هوية Vaughan | الفصل 13 | `PROVED-HERE` | برهان التفاف ديريشليه؛ تدقيق الهوية PASS |
| `ANT-PROP-13-01` | تفكيك مجاميع فون مانغولت إلى Type I وType II | الفصل 13 | `PROVED-HERE` | نتيجة من هوية Vaughan؛ تدقيق الدعم PASS |
| `ANT-LEM-13-02` | تقدير Type I | الفصل 13 | `PROVED-HERE` | Pólya--Vinogradov والجمع الجزئي؛ تدقيق Type I PASS |
| `ANT-LEM-13-03` | تقدير Type II | الفصل 13 | `PROVED-HERE` | المدخل الثنائي العظمى والتقسيم الديادي؛ تدقيق Type II PASS |
| `ANT-LEM-13-04` | متراجحة Pólya--Vinogradov للشخصيات البدائية | الفصل 13 | `PROVED-HERE` | تحويل فورييه المنتهي ومجاميع غاوس من الفصل 7 |
| `ANT-THM-13-02` | مبرهنة القيمة المتوسطة للشخصيات البدائية مع `sup_{y<=x}` | الفصل 13 | `PROVED-HERE` | هوية Vaughan وType I/II وحزمة الغربال الكبير المقتبسة |
| `ANT-THM-13-03` | مبرهنة Bombieri--Vinogradov في صيغة `psi` | الفصل 13 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | القيمة المتوسطة ورد الموصلات وSiegel--Walfisz للصغار |
| `ANT-COR-13-01` | النسخة الموافقة لـ`theta` | الفصل 13 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | ضبط القوى الأولية العليا من الفصل 9 |
| `ANT-COR-13-02` | النسخة الموافقة لـ`pi` | الفصل 13 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | الجمع الجزئي من `ANT-COR-13-01` |
| `ANT-COR-13-03` | نتيجة تقريبًا كل الترديدات | الفصل 13 | `PROVED-HERE / INEFFECTIVE-CONSTANT` | متراجحة ماركوف من `ANT-THM-13-03` |

## الحالة الحاكمة

```text
LOGIC-AUDIT              = PASS
REFERENCE-VERIFICATION   = PASS
POST-AUTHORING-AUDIT     = PASS
QUALITY-CHECKS            = RUN-372 / SUCCESS
PDF-BUILD                 = RUN-366 / SUCCESS
INDEPENDENT-REVIEW        = COMPLETED / APPROVED-WITH-NONBLOCKING-CORRECTIONS
```
