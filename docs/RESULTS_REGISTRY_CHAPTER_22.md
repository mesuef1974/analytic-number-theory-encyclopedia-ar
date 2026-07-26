# سجل نتائج الفصل الثاني والعشرين

## الحالة

```text
CHAPTER               = 22
VERSION               = 0.26.0-dev
REGISTRY              = AUTHORED-DRAFT / REVIEW-CORRECTED
RESULTS               = 10 AUTHORED-DRAFT / NON-CITABLE
PASS-FOR-AUTHORING    = YES
AUTHORING             = COMPLETED
POST-AUTHORING-REVIEW = CHANGES-REQUIRED / 0 BLOCKERS
REVIEW-CORRECTIONS    = APPLIED
NARROW-RE-REVIEW      = PENDING
OWNER-ADOPTION        = NOT REQUESTED
MERGE                 = NOT AUTHORIZED
```

| المعرّف | الوصف | التصنيف | الحالة |
|---|---|---|---|
| ANT-DEF-22-01 | تعريف العزم المستمر \(I_k(T)\) | DEFINITION | AUTHORED-DRAFT / NON-CITABLE |
| ANT-PROP-22-01 | المعادلة الوظيفية التقريبية المتناظرة لدالة زيتا | PROVED-HERE | REVIEW-CORRECTED / NON-CITABLE |
| ANT-PROP-22-02 | صيغة القيمة المتوسطة لكثيرات حدود ديريشليه | PROVED-HERE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-22-01 | صيغة العزم الثاني لدالة زيتا | PROVED-HERE | REVIEW-CORRECTED / NON-CITABLE |
| ANT-THM-22-02 | صيغة العزم الرابع الكلاسيكية | CITED-CORE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-22-03 | حد Soundararajan للعزوم تحت RH | CITED-CORE / PEER-REVIEWED | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-22-04 | تحسين Harper للحدود العليا | CITED-CORE / PREPRINT | AUTHORED-DRAFT / NON-CITABLE |
| ANT-THM-22-05 | الحدود الدنيا المستمرة للعزوم | CITED-CORE | AUTHORED-DRAFT / NON-CITABLE |
| ANT-CONJ-22-01 | حدسية العزوم العامة لـKeating--Snaith | CONJECTURAL / HEURISTIC | AUTHORED-DRAFT / NON-CITABLE |
| ANT-OPEN-22-01 | القيم المتطرفة والصيغة القصوى العامة | OPEN / FRONTIER | AUTHORED-DRAFT / NON-CITABLE |

## حكم بوابة التأليف

```text
REVIEWED-HEAD      = 9f56ae57afaa1e37eee55c54dc94a5e01563b004
VERDICT            = PASS
BLOCKERS           = 0
PASS-FOR-AUTHORING = YES
```

## حكم المراجعة المستقلة بعد التأليف

```text
REVIEWED-HEAD   = 812ac2355d4ede8dba88354c02bc85c7bc3c9a4a
VERDICT         = CHANGES-REQUIRED
BLOCKERS        = 0
RESULTS-CITABLE = NO
```

أُغلقت الملاحظتان الكبيرتان والملاحظة التحريرية في الرأس المصحح:

- تصحيح حد خطأ `ANT-PROP-22-01` إلى \(O(x^{-1/2}+y^{-1/2})\).
- إدراج إسناد Ingham صراحة داخل قسم العزم الثاني، مع فصل الخلفية التاريخية لـHardy--Littlewood.
- إزالة علامة BOM من مطلع ملف الفصل.

لا يرقّي هذا الإغلاق النتائج إلى `CITABLE` قبل المراجعة الضيقة المستقلة الجديدة واعتماد المالك.

## حراس ما بعد التأليف

- لا تصبح أي نتيجة قابلة للاستشهاد قبل البناء والتدقيق والمراجعة المستقلة اللاحقة واعتماد المالك.
- `ANT-CONJ-22-01` لا يوضع في بيئة theorem ولا يوصف بأنه مثبت.
- كل نتيجة مشروطة بفرضية ريمان تحمل الشرط في نصها وعنوانها المختصر.
- `ANT-THM-22-04` يحمل وسم `PREPRINT` ولا يعرض بمكانة ببليوغرافية مساوية لمقالة Soundararajan المحكمة.
- `ANT-OPEN-22-01` لا يستنتج مباشرة من `ANT-THM-22-03` أو `ANT-THM-22-04`.
- ترتيب `ANT-PROP-22-01` و`ANT-PROP-22-02` يسبق منطقيًا `ANT-THM-22-01` في المتن.
- `MERGE = NOT AUTHORIZED` حتى اعتماد المالك الصريح.
