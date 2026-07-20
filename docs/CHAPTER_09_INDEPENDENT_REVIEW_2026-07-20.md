# المراجعة المستقلة للفصل التاسع — مبرهنة الأعداد الأولية

## هوية النسخة الخاضعة للحكم

```text
CHAPTER       = 09 — مبرهنة الأعداد الأولية
BRANCH        = agent/chapter-09-prime-number-theorem-v0.13.0
FROZEN-COMMIT = 44dc9e433f262ac71ceb52f59ed5b59c77e58832
WORKING-TREE  = CLEAN (reviewed == committed == frozen)
REVIEWER-ROLE = Independent second review
```

تطابق الحكم مع النسخة المودعة عند الالتزام أعلاه. لا يتناول هذا الحكم أي تغييرات لاحقة إلا بعد إعادة فحصها.

## الحكم الرسمي

```text
VERDICT = APPROVED
```

النسخة المجمّدة معتمدة كما هي، ولا توجد تصحيحات إلزامية معلقة.

## أساس الحكم

- دُققت النتائج الثماني خطوة بخطوة: حد تشيبيشيف، وضبط القوى الأولية العليا، وتمثيل ستيلتيس، والمتراجحة الموزونة، وعدم الانعدام على الخط `Re(s)=1`، وتطبيق Wiener--Ikehara، والانتقال إلى `theta` و`pi`.
- خريطة الاعتماد خالية من الدور؛ ولا تستعمل لمّة تشيبيشيف مبرهنة الأعداد الأولية.
- المعرفات والحالات والإحالات والمراجع والبناء سليمة.
- يعتمد الفصل على نتائج ذات حالات مسموحة، ولا يعتمد على نتيجة `DRAFT`.
- يميز الفصل بوضوح بين `PROVED-HERE` و`CITED`، ولا يدعي حد خطأ فعالًا أو مسار Selberg--Erdős.

## تصفية الملاحظات

### NOTE-1 — معرفا اللمّتين

```text
STATUS = CLOSED / RETAINED-BY-DESIGN
```

الأمران `ANT-LEM-09-01` و`ANT-LEM-09-02` معرفان علميان مستقران مستقلان عن ترتيب العرض التلقائي. حُجز `ANT-LEM-09-01` للمتراجحة الموزونة قبل إدراج لمّة تشيبيشيف؛ لذلك تبقى المعرفات كما هي، وسُحبت توصية التبديل.

### NOTE-2 — Korevaar

```text
STATUS                           = CLOSED / VERIFIED
KOREVAAR-THEOREM-NUMBER          = VERIFIED
KOREVAAR-PAGES                   = VERIFIED
KOREVAAR-PNT-APPLICATION         = VERIFIED
```

تحققت صيغة Wiener--Ikehara في `Theorem 1.1`، الصفحات 1107--1108، وتحقق تطبيقها على مبرهنة الأعداد الأولية في الصفحات 1108--1109.

### NOTE-3 — توحيد أسماء الأعلام

```text
STATUS = NON-BLOCKING / EDITORIAL-DEFERRED
```

هذا تحسين تحريري اختياري لا يمنع الاعتماد.

## نطاق الحكم وحدوده

يثبت الفصل مبرهنة الأعداد الأولية نوعيًا عبر المسار التاوبيري:

```text
psi(x) ~ x  =>  theta(x) ~ x  =>  pi(x) ~ x/log x
```

ولا يشهد الحكم بحد خطأ فعال، ولا ببرهان داخلي لمبرهنة Wiener--Ikehara، ولا بإكمال مسار Selberg--Erdős. هذه الحدود معلنة في الفصل.

## الأثر الحوكمي

```text
CHAPTER-09 = REVIEWED
PR-13      = DRAFT / UNMERGED
ISSUE-14   = APPROVED
MERGE      = REQUIRES EXPLICIT OWNER ORDER
```

يسمح الحكم برفع الفصل من `VERIFIED` إلى `REVIEWED` وإعادة فحوص الجودة وبناء PDF. لا يسمح بدمج PR #13 من دون أمر صريح من مالك المشروع.
