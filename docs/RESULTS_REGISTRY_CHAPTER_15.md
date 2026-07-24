# سجل نتائج الفصل الخامس عشر

آخر مراجعة: 2026-07-24

```text
CHAPTER                = 15
VERSION                = 0.19.0-dev
AUTHORING              = COMPLETE-AS-DRAFT
PASS-FOR-AUTHORING     = YES
CHAPTER-STATE          = AUTHORED-DRAFT / INDEPENDENT-REVIEW-CHANGES-REQUIRED
POST-AUTHORING-AUDIT   = PASS
REFERENCE-AUDIT        = PASS
INDEPENDENT-REVIEW     = CHANGES-REQUIRED
RELEASE-READY          = NO
```

| المعرّف | النتيجة | الحالة الحالية | المصدر أو البرهان |
|---|---|---|---|
| `ANT-DEF-15-01` | بيانات الغربال المجردة: \(P(z)\)، و\(S(\mathcal A,\mathcal P,z)\)، والتفكيك \(|\mathcal A_d|=Xg(d)+r_d\) | `DEFINITION / AUTHORED-DRAFT` | اصطلاح الفصل المثبت في تدقيق التطبيع |
| `ANT-LEM-15-01` | متراجحة المربع: \(S(\mathcal A,\mathcal P,z)\le\sum_{n\in\mathcal A}(\sum_{d\mid(n,P(z))}\lambda_d)^2\) عند \(\lambda_1=1\) | `PROVED-HERE / CORRECTED-DRAFT` | برهان مباشر من كون الوزن يساوي 1 على العناصر المنخولة |
| `ANT-THM-15-01` | الحد العلوي المنتهي لغربال سيلبرغ: \(S\le X/G(R,z)+\sum_{d<R^2}3^{\omega(d)}|r_d|\) | `PROVED-HERE / INDEPENDENTLY-CHECKED` | التقطير الكامل، عكس موبيوس، كوشي--شفارتس، وصيغة معاملات سيلبرغ المثلى |
| `ANT-THM-15-02` | تقدير مقام سيلبرغ في بعد \(\kappa\): \(G(z,z)=e^{\gamma\kappa}V(z)^{-1}/\Gamma(\kappa+1)\,(1+O(1/\log z))\) | `CITED / TEXT-LOCATION-VERIFIED / NORMALIZATION-MATCHED` | Heath-Brown ص. 21؛ Halberstam--Richert (5.3.1) |
| `ANT-THM-15-03` | اللمّة الأساسية العامة بصيغة أحادية \(S=XV(z)(1+O(\rho(s)))+\text{بواقي}\) | `CITED / CHAPTER-PAGE-RANGE-VERIFIED / NOT-USED-IN-PAIR-APPLICATION` | Diamond--Halberstam--Galway، الفصل 4، ص 29--42 |
| `ANT-PROP-15-01` | الكثافة المحلية للأزواج \(n,n+h\): \(\rho_h(p)=2\) إذا \(p\nmid h\)، و\(1\) إذا \(p\mid h\)، مع انعدام الحالة الفردية بعد غربلة 2 | `PROVED-HERE / CORRECTED-DRAFT` | حساب فئات البواقي ومبرهنة الباقي الصيني |
| `ANT-PROP-15-02` | للحالة الزوجية \(h\ne0\)، يكون البعد الغربالي \(\kappa=2\) و\(V_h(z)\asymp_h(\log z)^{-2}\) | `PROVED-HERE / CORRECTION-REQUIRED` | يجب إضافة تحقق صريح من شرط (15.6): \(\sum_{w\le p<z}g_h(p)\log p=2\log(z/w)+O_h(1)\) |
| `ANT-THM-15-04` | لكل ثابت زوجي \(h\ne0\): \(S_h(x,z)\ll_h x/(\log z)^2\) بانتظام في \(3\le z\le x^{1/4}\) | `PROOF-GAP-BLOCKING / NOT-YET-REVIEWED` | الاستدعاء الحالي لـ`ANT-THM-15-02` يحتاج أولًا إلى إثبات شرط (15.6) لـ\(g_h\)؛ الثابت فعّال من حيث المبدأ |
| `ANT-DIAG-15-01` | عائق التكافؤ: بيانات القواسم المحلية التقليدية لا تميز وحدها بما يكفي بين تكافؤ عدد العوامل الأولية | `DIAGNOSTIC / TEXT-LOCATION-VERIFIED` | Friedlander--Iwaniec، ص 1042 و1044--1045 |

## حدود التسجيل

- لا تسجل حدسية الأوليات التوأم أو أي حد سفلي لعدد الأزواج الأولية.
- لا تسجل الفجوات المحدودة نتيجة للفصل.
- لا تسجل Brun--Titchmarsh ضمن المسار المركزي.
- لا تسجل صيغ \(F_\kappa(s),f_\kappa(s)\) بوصفها اللمّة الأساسية.
- لا تصبح حالة الفصل `REVIEWED` قبل إصلاح فجوة شرط (15.6)، وإعادة البناء، وإعادة فحص المراجعة المستقلة.

```text
RESULTS-AUTHORED        = 9
MATHEMATICAL-BLOCKERS   = 1
REFERENCE-BLOCKERS      = 0
GOVERNANCE-BLOCKERS     = 1 / CHAPTER-TEXT-STATUS-STILL-STALE
TEXTUAL-BLOCKERS        = 0
POST-AUTHORING-AUDIT    = PASS
REFERENCE-AUDIT         = PASS
INDEPENDENT-REVIEW      = CHANGES-REQUIRED
NEXT-ACTION             = PATCH-PAIR-REGULARITY + SYNC-CHAPTER-STATUS + REBUILD + REVIEW-RECHECK
```
