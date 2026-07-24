# سجل نتائج الفصل السادس عشر

آخر تحديث: 2026-07-24

```text
CHAPTER               = 16
VERSION               = 0.20.0-dev
STATUS                = REVIEWED
PRE-AUTHORING-GATE    = CLOSED
PASS-FOR-AUTHORING    = YES
INDEPENDENT-REVIEW    = APPROVED-WITH-NONBLOCKING-TYPOGRAPHY
OWNER-ADOPTION        = APPROVED
RESULTS               = 8 / REVIEWED
RELEASE-READY         = NO
```

| المعرّف | النوع | الوصف | التصنيف | الحالة |
|---|---|---|---|---|
| `ANT-DEF-16-01` | تعريف | فجوات الأوليات والكميات \(H_m\) | `PROVED-HERE` | `REVIEWED` |
| `ANT-THM-16-01` | مبرهنة | حد علوي لعد الأزواج الأولية ذات فرق ثابت | `PROVED-HERE` | `REVIEWED` |
| `ANT-COR-16-01` | نتيجة | تقارب مجموع برون للأزواج الأولية | `PROVED-HERE` | `REVIEWED` |
| `ANT-THM-16-02` | مبرهنة | مبرهنة تشن بصياغة \(p+P_2\) | `CITED` | `REVIEWED` |
| `ANT-THM-16-03` | مبرهنة | نتيجة GPY عن الفجوات الصغيرة نسبيًا | `CITED / EXPLAINED` | `REVIEWED` |
| `ANT-THM-16-04` | مبرهنة | مبرهنة Zhang عن الفجوات المحدودة | `CITED / EXPLAINED` | `REVIEWED` |
| `ANT-THM-16-05` | مبرهنة | مبرهنة Maynard عن الفجوات المحدودة و\(H_m<\infty\) | `CITED / EXPLAINED` | `REVIEWED` |
| `ANT-THM-16-06` | مبرهنة | حد Polymath8b المنشور \(H_1\le246\) | `CITED` | `REVIEWED` |

## قيود الحوكمة

- لا تُرقّى أي نتيجة إلى `ACTIVE` قبل الدمج في `main` وترقية الفصل إلى `RELEASE-READY`.
- النتائج المنسوبة إلى Chen وGPY وZhang وMaynard وPolymath تبقى `CITED` ولا يعاد تقديمها بوصفها براهين داخلية كاملة.
- أفضل ثابت عددي معاصر لا يوصف بأنه نهائي؛ الفصل يثبت فقط الحد المنشور الموثق \(H_1\le246\).
- لا يدعي الفصل حدسية الأوليات التوأم أو \(H_1=2\).
- اعتماد المالك لا يمنح إذنًا بدمج PR #30؛ الدمج وتعديل `main` يبقيان قرارًا منفصلاً للمالك.
